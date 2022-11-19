import os
import requests
import typing
from src.models import Individual
import urllib.parse

class BingQuery:

    try:
        API_Key = os.environ.get('BING_WEB_SEARCH_API_KEY')
        assert API_Key
    except AssertionError:
        print("API Key Unavailable")

    SEARCH_URL = "https://api.bing.microsoft.com/v7.0/search"

    def __init__(self, individual: Individual):
        self.individual = individual

    def __generate_queries(self):
        organisation_query = f"\"{self.individual.name}\" and "
        organisations = [f"\"{organisation}\"" for organisation in self.individual.organisations]
        organisation_query += f"({organisations})"

        personal_site_query = " and ".join([f"\"{site}\"" for site in self.individual.domains])

        query = f"({personal_site_query}) or ({organisation_query})"
        return urllib.parse.quote_plus(query)

