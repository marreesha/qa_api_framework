import allure
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from config.settings import BACKOFF, RETRIES
from src.utils.logger import logger


class BaseClient:
    def __init__(self, base_url: str, timeout: int = 5, api_key: str = None):
        self.base_url = base_url
        self.timeout = timeout
        self.api_key = api_key

        self.session = requests.Session()
        retries = Retry(
            total=RETRIES,
            backoff_factor=BACKOFF,
            status_forcelist=[500, 502, 503, 504],
            allowed_methods=["GET", "POST"],
        )
        adapter = HTTPAdapter(max_retries=retries)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    def _headers(self):
        headers = {}
        if self.api_key:
            headers["x-api-key"] = self.api_key
        return headers

    @allure.step("{method} {path}")
    def _request(self, method: str, path: str, **kwargs):
        url = f"{self.base_url}{path}"

        logger.info(f"{method} {url}")
        logger.info(f"Request body: {kwargs.get('json')}")
        allure.attach(url, name="Request URL", attachment_type=allure.attachment_type.TEXT)
        allure.attach(str(kwargs.get("json")), name="Request Body", attachment_type=allure.attachment_type.JSON)

        headers = kwargs.pop("headers", {})
        headers.update(self._headers())

        response = self.session.request(method, url=url, timeout=self.timeout, headers=headers, **kwargs)

        logger.info(f"Response: {response.status_code} | {response.text[:200]}")
        allure.attach(str(response.status_code), name="Response Status", attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.JSON)

        return response

    def _get(self, path: str, **kwargs):
        return self._request("GET", path, **kwargs)

    def _post(self, path: str, **kwargs):
        return self._request("POST", path, **kwargs)
