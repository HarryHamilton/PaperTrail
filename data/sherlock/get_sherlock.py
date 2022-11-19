import os

# TODO: Date searches (somehow) to allow for data pruning if storage capacity runs low.
OUTPUT_DIRECTORY = "searches"


def get_results(usernames=None):
    """
    :param usernames: A list of usernames with length > 0 to search.
    :return: True if successful and CSV file created in `searches`, otherwise False.
    """
    if usernames is not None:
        users = ""
        for user in usernames:
            users += user
            users += " "

        command = f"python3 sherlock/sherlock --csv --folderoutput {OUTPUT_DIRECTORY} {users}"
        init_reqs()
        os.system(command)
        return True
    return False


def init_reqs():
    os.system("python3 -m pip install -r sherlock/requirements.txt")
