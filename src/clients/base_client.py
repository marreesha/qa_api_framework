import requests


class BaseClient:
    def __init__(self, base_url: str, timeout: int = 5, api_key: str = None):
        self.base_url = base_url
        self.timeout = timeout
        self.api_key = api_key

    def _headers(self):
        headers = {}
        if self.api_key:
            headers["x-api-key"] = self.api_key
        return headers

    def _get(self, path: str, **kwargs):
        return requests.get(
            f"{self.base_url}{path}",
            timeout=self.timeout,
            headers=self._headers(),
            **kwargs,
        )

    def _post(self, path: str, **kwargs):
        return requests.post(
            f"{self.base_url}{path}",
            timeout=self.timeout,
            headers=self._headers(),
            **kwargs,
        )
