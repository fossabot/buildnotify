class ServerConfig:
    def __init__(self, url, excluded_projects, timezone, prefix, username, password):
        self.url = url
        self.excluded_projects = excluded_projects
        self.timezone = timezone
        self.prefix = prefix
        self.username = username
        self.password = password

    def has_creds(self):
        return self.username != '' and self.username is not None