import os
import requests


class BingQuery:

    try:
        API_Key = os.environ.get('BING_WEB_SEARCH_API_KEY')
        assert API_Key
    except AssertionError:
        print("API Key Unavailable")

    SEARCH_URL = "https://api.bing.microsoft.com/v7.0/search"
