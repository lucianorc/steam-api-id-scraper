from datetime import datetime
from dataclasses import dataclass, field


@dataclass
class AppCategory(object):
    id: int
    description: str


@dataclass
class AppGenre(object):
    id: int
    description: str


@dataclass
class App(object):
    appid: int
    type: str = field(default_factory=str)
    free: bool = field(default_factory=bool)
    name: str = field(default_factory=str)
    categories: list[AppCategory] = field(default_factory=list)
    genres: list[AppGenre] = field(default_factory=list)
    release_date: datetime = field(default=None)

    def is_game(self):
        return self.type == "game"
