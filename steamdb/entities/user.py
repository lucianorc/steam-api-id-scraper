from datetime import datetime
from dataclasses import dataclass, field

from steamdb.entities.library import GameLibrary
from steamdb.entities.base import BaseModel


@dataclass
class User(BaseModel):
    steamid: str
    community_visibility_state: int = field(default_factory=int)
    time_created: datetime = field(default=None)
    loccountrycode: str = field(default_factory=str)
    library: GameLibrary = field(default_factory=GameLibrary)
