from src.clients.base_client import BaseClient


class UserClient(BaseClient):

    def get_user(self, user_id: int):
        return self._get(f"/users/{user_id}")

    def create_user(self, data: dict):
        return self._post("/users", json=data)
