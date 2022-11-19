import os

import requests


class BingQuery:
    try:
        API_Key = os.environ.get('BING_WEB_SEARCH_API_KEY')
        assert API_Key
    except AssertionError:
        print("API Key Unavailable")

    SEARCH_URL = "https://api.bing.microsoft.com/v7.0/search"

    def __init__(self, individual):
        self.individual = individual

    def query(self):
        params = {
            "q": self.__generate_queries()
        }
        headers = {
            "Ocp-Apim-Subscription-Key": self.API_Key
        }

        response = requests.get(self.SEARCH_URL, headers=headers, params=params)

        return response.json()

    def __generate_queries(self):
        organisation_query = f"\"{self.individual.name}\" and "
        organisations = [f"\"{organisation}\"" for organisation in self.individual.organisations]
        organisation_query += f"({organisations})"

        personal_site_query = " and ".join([f"\"{site}\"" for site in self.individual.domains])

        query = f"({personal_site_query}) or ({organisation_query})"
        return query
