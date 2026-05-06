import os

BASE_URL = os.getenv("BASE_URL", "https://reqres.in/api")
API_KEY = os.getenv("API_KEY")
TIMEOUT = 5

RETRIES = 3
BACKOFF = 0.5
