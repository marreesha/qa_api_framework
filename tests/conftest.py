import pytest

from config.settings import API_KEY, BASE_URL, TIMEOUT
from src.clients.user_client import UserClient
from src.services.user_service import UserService


@pytest.fixture
def user_service():
    client = UserClient(BASE_URL, TIMEOUT, API_KEY)
    return UserService(client)
