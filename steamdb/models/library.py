from .base import BaseModel
from steamdb.api.client import APIClient
from steamdb.entities import GameLibrary


class GameLibraryModel(BaseModel):
    def __init__(self, client: APIClient):
        super().__init__(client.player_resource, client.session)
        self.api_session.params = {
            "key": "D5F90A4D67793F987CFF390E7641A722",
            "format": "json",
        }

    def get_user_library(self, user_id: str) -> GameLibrary:
        url = f"{self.url}/GetOwnedGames/v0001"

        self.api_session.params["steamid"] = [user_id]
        response = self.api_session.get(url)

        return response.json()["response"]
