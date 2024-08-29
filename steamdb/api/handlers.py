from dataclasses import dataclass, field

from .client import APIClient
from steamdb.repositories import AppRepository, LibraryRepository, UserRepository


@dataclass
class Handlers(object):
    client: APIClient
    app_repo: AppRepository
    lib_repo: LibraryRepository
    user_repo: UserRepository

    def get_app(self, app_id: str):
        return self.app_repo.app_info(app_id)
