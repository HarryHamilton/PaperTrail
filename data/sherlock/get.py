import os

# TODO: Date searches (somehow) to allow for data pruning if storage capacity runs low.
OUTPUT_DIRECTORY = "searches"


def query(usernames=None):
    """
    :param usernames: A list of usernames with length > 0 to search.
    :return: A list of dictionaries containing two
    keys, `user` and `hits` with the following format: x = [{user: <user>, hits: [<hit0>, <hit1>, ...]},
    ...]. Returns None if `usernames` is empty.
    """
    if usernames is not None:
        users = ""
        for user in usernames:
            users += user
            users += " "

        command = f"python3 sherlock/sherlock --csv --folderoutput {OUTPUT_DIRECTORY} {users}"
        init_reqs()
        os.system(command)
        return format_output(usernames)
    return None


def format_output(usernames=None):
    """
    :param usernames: A list of usernames with length > 0 to search.
    :return: A list of dictionaries containing two
    keys, `user` and `hits` with the following format: x = [{user: <user>, hits: [<hit0>, <hit1>, ...]},
    ...]. Returns None if `usernames` is empty.
    """
    if usernames is not None:
        output = []
        for user in usernames:
            tmp = {"user": user}
            with open(f"{user}.txt", "r") as file:
                tmp["hits"] = [x.strip("\n") for x in file.readlines()]
            output.append(tmp)

        return output
    return None


def init_reqs():
    os.system("python3 -m pip install -r sherlock/requirements.txt")
