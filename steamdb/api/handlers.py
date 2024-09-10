from dataclasses import dataclass, field

from .client import APIClient, StoreClient
from steamdb.repositories import AppRepository, GameLibraryRepository, UserRepository
from steamdb.entities import App, User


class APIHandler(object):
    def __init__(self) -> None:
        self.api_client = APIClient()
        self.store_client = StoreClient()

        self.app_repo = AppRepository(self.store_client)
        self.lib_repo = GameLibraryRepository(self.api_client)
        self.user_repo = UserRepository(self.api_client)

    def get_app(self, app_id: str) -> App:
        return self.app_repo.get_app_info(app_id)

    def get_user(self, user_id: str) -> User:
        return self.user_repo.get_user(user_id)

    def get_many_user(self, user_ids: list[str]) -> User:
        return self.user_repo.get_many_user(user_ids)
