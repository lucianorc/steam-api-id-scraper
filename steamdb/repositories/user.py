from datetime import datetime
from copy import deepcopy

from steamdb.api.client import APIClient
from steamdb.repositories import GameLibraryRepository
from steamdb.models import UserModel
from steamdb.entities import User


class UserRepository(object):
    def __init__(self, client: APIClient) -> None:
        self.user_model = UserModel(client)
        self.lib_repo = GameLibraryRepository(deepcopy(client))

    def __create_user(self, user: dict) -> User:
        return User(
            steamid=user["steamid"],
            community_visibility_state=user["communityvisibilitystate"],
            loccountrycode=user["loccountrycode"],
            time_created=datetime.fromtimestamp(user["timecreated"]),
            library=self.lib_repo.get_user_library(user["steamid"]),
        )

    def get_user(self, steam_id: str) -> User:
        user = self.user_model.get_user(steam_id)
        user_entity = self.__create_user(user)
        return user_entity

    def get_many_users(self, steam_ids: list[str]) -> list[User]:
        users = self.user_model.get_many_users(steam_ids)
        entity_list = list()

        for user in users:
            user = self.__create_user(user)
            entity_list.append(user)

        return entity_list
