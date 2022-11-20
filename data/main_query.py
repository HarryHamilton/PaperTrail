from data.bing.query import BingQuery
from data.sherlock.query import SherlockQuery
from data.beenpwned.query import BeenPwnedQuery


class MainQuery:
    def __init__(self, individual):
        self.__individual = individual
        self.__bing_results = []
        self.__sherlock_results = []
        self.__beenpwned_results = []
        self.__results = []

    def query(self):
        self.__do_sherlock_query()
        self.__do_beenpwned_query()
        self.__do_bing_query()

        results = {
            "bing_results": self.__bing_results,
            "sherlock_results": self.__sherlock_results,
            "beenpwned_results": self.__beenpwned_results
        }

        self.__results = results
        return results

    def __do_bing_query(self):
        self.__bing_results = BingQuery(self.__individual).query()

    def __do_sherlock_query(self):
        self.__sherlock_results = SherlockQuery(self.__individual.usernames).query()

    def __do_beenpwned_query(self):
        for user in self.__sherlock_results:
            self.__beenpwned_results.append(BeenPwnedQuery(user["urls"]))
