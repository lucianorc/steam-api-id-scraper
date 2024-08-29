from dataclasses import dataclass, field
import requests


class BaseClient(object):
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()


class APIClient(BaseClient):
    def __init__(self):
        super().__init__("https://api.steampowered.com")

    @property
    def player_resource(self) -> str:
        return "%s/IPlayerService" % self.base_url

    @property
    def user_oauth_resource(self) -> str:
        return "%s/ISteamUserOAuth" % self.base_url

    @property
    def user_oauth_resource(self) -> str:
        return "%s/ISteamUserOAuth" % self.base_url


class StoreClient(BaseClient):
    def __init__(self):
        super().__init__("http://store.steampowered.com/api")

    @property
    def app_resource(self) -> str:
        return "%s/appdetails" % self.base_url
