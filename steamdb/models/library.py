from dataclasses import dataclass, field

from steamdb.models.app import App


@dataclass
class GameLibrary(object):
    game_count: int = field(default_factory=int)
    games: list[App] = field(default_factory=list)
