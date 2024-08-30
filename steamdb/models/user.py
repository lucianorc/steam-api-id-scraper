from requests import Session

from steamdb.entities import User
from steamdb.api.client import APIClient
from .base import BaseModel


class UserModel(BaseModel):
    def __init__(self, client: APIClient):
        super().__init__(client.user_oauth_resource, client.session)
        self.api_session.params = {
            "access_token": "eyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEY4Ql8yNEM5RDIzM181M0VCRiIsICJzdWIiOiAiNzY1NjExOTgxOTM5MDE0NTAiLCAiYXVkIjogWyAid2ViOmNvbW11bml0eSIgXSwgImV4cCI6IDE3MjUwNzA5ODUsICJuYmYiOiAxNzE2MzQzMTgwLCAiaWF0IjogMTcyNDk4MzE4MCwgImp0aSI6ICIxMDVEXzI0RjdGNzNDXzFGODhCIiwgIm9hdCI6IDE3MjE5NDA1NzEsICJydF9leHAiOiAxNzQwMzY5NDczLCAicGVyIjogMCwgImlwX3N1YmplY3QiOiAiMTM4LjIwNC4yNS4yOSIsICJpcF9jb25maXJtZXIiOiAiMTkzLjE5LjIwNS4xNTYiIH0.hVgi30QwjJjCW05PZ5zv2JbriksXFfc48f1-EbDyEw61MyVwHTVSrs8lELzGz2cNxOVC9_n0S5Tvem6rorHLBg",
        }
        self.url += "/GetUserSummaries/v1"

    def get_user(self, steam_id: str) -> User:
        self.api_session.params["steamids"] = [steam_id]
        response = self.api_session.get(self.url)
        return response.json()["players"][0]

    def get_many_users(self, steam_ids: list[str]) -> list[User]:
        self.api_session.params["steamids"] = ",".join(steam_ids)
        response = self.api_session.get(self.url)
        return response.json()["players"]
