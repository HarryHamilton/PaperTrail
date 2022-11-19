import requests
import tldextract

api_url = "https://haveibeenpwned.com/api/v3/breach/"  # add site url after /breach/
test_urls = [ {
        'url': 'https://discussions.apple.com/profile/gwo0d', 'id': '66fa8b9736ce198067f5adfaf9ff507f'
    }, {
        'url': 'https://www.codecademy.com/profiles/gwo0d', 'id': '11f17d39763bf6ed48dd3955e0ad4e2f'
    }, {
        'url': 'https://www.codewars.com/users/gwo0d', 'id': '7cd1265b478bb5fa0d795659a8b14578'
    }, {
        'url': 'https://www.duolingo.com/profile/gwo0d', 'id': 'c09afd93efeac6ffdb2f47222656d383'
    }, {
        'url': 'https://www.facebook.com/gwo0d', 'id': '174c238a0af8df72532a7a201179b306'
    }, {
        'url': 'https://fortnitetracker.com/profile/all/gwo0d', 'id': '6ca57e902f100081ec629a9995b395ce'
    }, {
        'url': 'https://genius.com/gwo0d', 'id': '70b9b8e806a5f07bd70af974b4debabb'
    }, {
        'url': 'https://www.000webhost.com/gwo0d', 'id': 'dd709a8a615ce2b2807da758cdc9e9a5'
    }
    ]

def beenpwned(list_of_sites):
    """
    what this function expects:
    - a list of dictionaries
    each dictionary is comprised of:
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


beenpwned(test_urls)
