from datetime import datetime
from dataclasses import dataclass, field

from steamdb.models.library import GameLibrary
from steamdb.models.base import BaseModel


@dataclass
class User(BaseModel):
    steamid: str
    community_visibility_state: int = field(default_factory=int)
    time_created: datetime = field(default=None)
    loccountrycode: str = field(default_factory=str)
    library: GameLibrary = field(default_factory=GameLibrary)
