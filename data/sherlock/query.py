import os
import secrets


class SherlockQuery:
    # TODO: Date searches (somehow) to allow for data pruning if storage capacity runs low.
    __ROOT_DIRECTORY = os.path.dirname(__file__)
    __OUTPUT_DIRECTORY = "searches"
    __results = None

    def __init__(self, usernames=None):
        self.__usernames = usernames

    def query(self):
        """
        :return: A list of dictionaries containing two
        keys, `user` and `hits` with the following format: x = [{user: <user>, hits: [<hit0>, <hit1>, ...]},
        ...]. Returns None if `usernames` is empty.
        """
        if self.__usernames is not None:
            users = ""
            for user in self.__usernames:
                users += user
                users += " "

            query_command = f"python3 {self.__ROOT_DIRECTORY}/sherlock/sherlock --csv --folderoutput {self.__ROOT_DIRECTORY}/{self.__OUTPUT_DIRECTORY} {users}"
            os.system(query_command)

            for user in self.__usernames:
                cleanup_command = f"rm {self.__ROOT_DIRECTORY}/{self.__OUTPUT_DIRECTORY}/{user}.csv"
                os.system(cleanup_command)

            results = self.__format_output()
            self.__results = results
            return results
        return None

    def __format_output(self):
        """
        :return: A list of dictionaries containing two
        keys, `user` and `hits` with the following format: x = [{user: <user>, hits: [<hit0>, <hit1>, ...]},
        ...]. Returns None if `usernames` is empty.
        """
        if self.__usernames is not None:
            output = []
            for user in self.__usernames:
                base = {"user": user}
                urls_with_id = []
                with open(f"{self.__ROOT_DIRECTORY}/{self.__OUTPUT_DIRECTORY}/{user}.txt", "r") as file:
                    url_list = [x.strip("\n") for x in file.readlines()[:-1]]
                    used_ids = []
                    for url in url_list:
                        unique_id = None
                        while not unique_id:
                            x = secrets.token_hex(16)
                            if x not in used_ids:
                                unique_id = x
                                used_ids.append(x)

                        urls_with_id.append({"url": url, "id": unique_id})

                base["urls"] = urls_with_id
                output.append(base)

            return output
        return None

    def set_usernames(self, new_usernames):
        self.__usernames = new_usernames

    def get_results(self):
        return self.__results
