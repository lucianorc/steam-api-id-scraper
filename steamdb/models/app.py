from steamdb.api.client import StoreClient
from .base import BaseModel
from steamdb.entities import App


class AppModel(BaseModel):
    def __init__(self, client: StoreClient):
        super().__init__(client.app_resource, client.session)

    def get_app_info(self, app_id: str) -> App:
        response = self.api_session.get(self.url, params={"appids": app_id})
        return response.json()[app_id]["data"]
