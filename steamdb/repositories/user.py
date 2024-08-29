from dataclasses import dataclass, field
from datetime import datetime
import requests

from steamdb.repositories.library import LibraryRepository
from steamdb.models import User


@dataclass
class UserRepository(object):
    access_token = "eyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEY4Ql8yNEM5RDIzM181M0VCRiIsICJzdWIiOiAiNzY1NjExOTgxOTM5MDE0NTAiLCAiYXVkIjogWyAid2ViOnN0b3JlIiBdLCAiZXhwIjogMTcyNDk2MzU0NywgIm5iZiI6IDE3MTYyMzU0ODUsICJpYXQiOiAxNzI0ODc1NDg1LCAianRpIjogIjEwNURfMjRGN0Y3MjRfNTRBNTIiLCAib2F0IjogMTcyMTk0MDU3MSwgInJ0X2V4cCI6IDE3NDAzNjk0NzMsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICIxMzguMjA0LjI1LjI5IiwgImlwX2NvbmZpcm1lciI6ICIxOTMuMTkuMjA1LjE1NiIgfQ.SobsN0JjuG8XvGC-rJHlEluozxqbTrUee26W06YVEkJDaiodmfO5qa49kAiYp0QJqN_00f95EDcy1HFYylWfBw"
    library_repo: LibraryRepository = field(default_factory=LibraryRepository)

    def get_user(self, steamid: str) -> User:
        response = self.__create_request(
            {"access_token": self.access_token, "steamids": [steamid]}
        )

        return self.__create_user(response[0])

    def get_many_user(self, steamids: list[str]) -> list[User]:
        response = self.__create_request(
            {"access_token": self.access_token, "steamids": steamids}
        )

        user_list = list()
        for user_raw in response:
            user = self.__create_user(user_raw)
            user_list.append(user)

    def __create_request(self, payload: dict):
        r = requests.get(
            "https://api.steampowered.com/ISteamUserOAuth/GetUserSummaries/v1",
            params=payload,
        )

        if r.status_code != 200:
            raise Exception("User not found")

        return r.json()["players"]

    def __create_user(self, user: dict) -> User:
        return User(
            steamid=user["steamid"],
            community_visibility_state=user["communityvisibilitystate"],
            loccountrycode=user["loccountrycode"],
            time_created=self.__time_created(user["timecreated"]),
            library=self.library_repo.get_user_game_library(user["steamid"]),
        )

    def __time_created(self, timestamp: int) -> datetime:
        return datetime.fromtimestamp(timestamp)
