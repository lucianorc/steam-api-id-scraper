from steamdb.api.client import APIClient, StoreClient
from steamdb.entities import App, GameLibrary
from steamdb.models import GameLibraryModel
from steamdb.repositories import AppRepository


class GameLibraryRepository(object):
    def __init__(self, client: APIClient) -> None:
        self.lib_model = GameLibraryModel(client)
        self.app_repo = AppRepository(StoreClient())

    def __create_entity(self, lib: GameLibrary) -> GameLibrary:
        return GameLibrary(
            game_count=lib["game_count"],
            games=self.__create_game_entity_list(lib["games"]),
        )

    def __create_game_entity_list(self, games: list) -> list[App]:
        game_entities = list()
        for game in games[:2]:
            app_id = str(game["appid"])

            game_entity = self.app_repo.get_app_info(app_id)
            if game_entity.is_game:
                game_entities.append(game_entity)

        return game_entities

    def get_user_library(self, user_id: str) -> GameLibrary:
        lib = self.lib_model.get_user_library(user_id)
        lib_entity = self.__create_entity(lib)
        return lib_entity
