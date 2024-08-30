from requests import Session


class BaseModel(object):
    api_session: Session
    url: str

    def __init__(
        self,
        url: str,
        api_session: Session,
    ):
        self.url = url
        self.api_session = api_session
