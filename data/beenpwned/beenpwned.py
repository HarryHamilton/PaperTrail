import requests

api_url = "https://haveibeenpwned.com/api/v3/breach/"  # add site url after /breach/
test_urls = ["facebook", "000webhost"]

def beenpwned(site):
    dicts = []
    for url in site:
        request_url = api_url + url
        response = requests.get(request_url)
        response_json = response.json()  # convert response to json
        site_name = ""
        domain = ""
        breach_date = ""
        for key, value in response_json.items():
            # print(key, value)   # prints all the key, value pairs
            if key == "Name":
                site_name = value
            if key == "Domain":
                domain = value
            if key == "BreachDate":
                breach_date = value

        print(site_name)
        print(domain)
        print(breach_date)

        data = {"site_name": site_name,
                "domain": domain,
                "breach_date": breach_date}

        dicts.append(data)

        print(dicts)



beenpwned(test_urls)
