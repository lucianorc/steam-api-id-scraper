from dataclasses import dataclass
from datetime import datetime
import requests

from steamdb.models import App
from steamdb.models.app import AppCategory, AppGenre


@dataclass
class AppRepository(object):
    base_url: str = "http://store.steampowered.com/api/appdetails"

    def app_info(self, appid: str) -> App:
        response = self.__create_request({"appids": appid})
        return self.__create_app(response)

    def __create_request(self, payload: dict) -> dict:
        r = requests.get("http://store.steampowered.com/api/appdetails", params=payload)
        if r.status_code != 200:
            raise Exception("App not found")

        app_id = payload["appids"]
        return r.json()[app_id]["data"]

    def __create_app(self, obj: dict):
        try:
            return App(
                appid=obj["steam_appid"],
                type=obj["type"],
                free=obj["is_free"],
                name=obj["name"],
                categories=self.__categories(obj["categories"]),
                genres=self.__genres(obj["genres"]),
                release_date=self.__release_date(obj["release_date"]["date"]),
            )
        except Exception as xcp:
            xcp.add_note("Error creating app obj for AppId: %s" % obj["steam_appid"])
            raise xcp

    def __categories(self, cat: list) -> list[AppCategory]:
        cat_list = list()
        for obj in cat:
            cat_list.append(AppCategory(**obj))

        return cat_list

    def __genres(self, genres: list) -> list[AppGenre]:
        genres_list = list()

        for obj in genres:
            genres_list.append(AppGenre(**obj))

        return genres_list

    def __release_date(self, date: str) -> datetime:
        date_formats = [
            "%d %b, %Y",
            "%d/%b./%Y",
        ]

        for datefmt in date_formats:
            try:
                return datetime.strptime(date, datefmt)
            except:
                pass

        raise Exception("No date format available for %s" % date)
