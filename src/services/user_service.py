from src.clients.user_client import UserClient


class UserService:
    def __init__(self, client: UserClient):
        self.client = client

    def get_user(self, user_id: int):
        response = self.client.get_user(user_id)
        return response.json()

    def create_user(self, name: str, job: str):
        payload = {"name": name, "job": job}
        response = self.client.create_user(payload)
        return response.json()
