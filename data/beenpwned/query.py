import requests
import tldextract


api_url = "https://haveibeenpwned.com/api/v3/breach/"  # add site url after /breach/


def BeenPwnedQuery(list_of_sites):
    """
    what this function expects:
    - a list of dictionaries
    each dictionary is composed of:
    - key = website url
    - val = id
    :param list_of_sites:
    :return: a list of dictionaries
    """
    dicts = []

    # Loop through all of the websites
    for website in list_of_sites:
        # strip domain name from URL
        domain = tldextract.extract(website["url"])
        domain = domain.domain

        request_url = api_url + domain  # full url that we will POST
        response = requests.get(request_url)
        # Checks if website has been pwned. If it has, POST req will return a 200 response code.
        # if the response code is not 200, it hasn't been pwned
        if response.status_code == 200:
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
                    "breach_date": breach_date,
                    "id": website["id"]}

            dicts.append(data)

    print(dicts)


BeenPwnedQuery(test_urls)
