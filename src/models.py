class Individual:
    def __init__(self, usernames, name, organisations, domains):
        self.usernames = usernames
        self.name = name
        self.organisations = organisations
        self.domains = domains

class AccountSite:
    def __init__(self, username, url, pwned):
        self.url = url
        self.username = username
        self.pwned = pwned

    def __repr__(self):
        return self.url

    def __str__(self):
        return self.url

class LinkSite:
    def __init__(self, url, name, snippet):
        self.url = url
        self.name = name
        self.snippet = snippet

    def __repr__(self):
        return self.url

    def __str__(self):
        return self.url

