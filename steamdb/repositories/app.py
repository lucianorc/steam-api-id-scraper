from datetime import datetime

from steamdb.api.client import StoreClient
from steamdb.entities.app import AppCategory, AppGenre
from steamdb.models import AppModel
from steamdb.entities import App
from steamdb.entities.app import AppCategory, AppGenre


class AppRepository(object):
    app_model: AppModel

    def __init__(self, client: StoreClient):
        self.app_model = AppModel(client)

    def __create_entity(self, app: dict) -> App:
        return App(
            appid=app["steam_appid"],
            type=app["type"],
            free=app["is_free"],
            name=app["name"],
            categories=self.__categories(app["categories"]),
            genres=self.__genres(app["genres"]),
            release_date=self.__release_date(app["release_date"]["date"]),
        )

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

    def get_app_info(self, app_id: str) -> App:
        app = self.app_model.get_app_info(app_id)
        app_entity = self.__create_entity(app)
        return app_entity
