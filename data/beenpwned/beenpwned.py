import requests

api_url = "https://haveibeenpwned.com/api/v3/breach/"  # add site url after /breach/
test_urls = ["facebook", "000webhost"]

def beenpwned(list_of_sites):
    dicts = []

    # Loop through all of the websites
    for website in list_of_sites:
        request_url = api_url + website  # full url that we will POST
        response = requests.get(request_url)
        response_json = response.json()  # convert response to json

        site_name = ""
        domain = ""
        breach_date = ""
        # Loop through the dictionary that we get from POST request
        for key, value in response_json.items():
            # print(key, value)   # prints all the key, value pairs
            if key == "Name":
                site_name = value
            if key == "Domain":
                domain = value
            if key == "BreachDate":
                breach_date = value

        # save necessary variables in a dictionary
        data = {"site_name": site_name,
                "domain": domain,
                "breach_date": breach_date}

        dicts.append(data)


beenpwned(test_urls)
