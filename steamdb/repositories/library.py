from dataclasses import dataclass, field

import requests

from steamdb.repositories.app import AppRepository
from steamdb.models import App, GameLibrary


@dataclass
class LibraryRepository(object):
    key: str = "D5F90A4D67793F987CFF390E7641A722"
    app_repo: AppRepository = field(default_factory=AppRepository)

    def __create_request(self, payload: dict) -> any:
        r = requests.get(
            "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001",
            params=payload,
        )

        if r.status_code != 200:
            raise Exception("Games from User %s not found" % self.steamid)

        return r.json()["response"]

    def get_user_game_library(self, user_id: str) -> GameLibrary:
        response = self.__create_request(
            payload={
                "key": self.key,
                "steamid": user_id,
                "format": "json",
            }
        )

        game_library = GameLibrary()
        game_library.game_count = response["game_count"]

        for obj in response["games"][:20]:
            app_id = str(obj["appid"])
            try:
                return self.__get_game(app_id)
            except:
                pass

        return game_library

    def __get_game(self, app_id: str) -> App | None:
        app = self.app_repo.app_info(app_id)
        if app.is_game():
            return app

        return None
