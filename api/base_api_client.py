# File: `features/api/base_api_client.py`
from urllib.parse import urljoin
import requests
import logging
from typing import Optional

logger = logging.getLogger(__name__)

class BaseAPIClient:
    """
    Simple HTTP client that normalizes base_url and safely joins paths.
    Usage:
      client = BaseAPIClient("https://api.vineetkr.com")
      resp = client.get("/api/users")
    """
    def __init__(self, base_url: str, session: Optional[requests.Session] = None):
        self.base_url = base_url.rstrip('/') + '/'
        self.session = session or requests.Session()

    def _build_url(self, path: str) -> str:
        return urljoin(self.base_url, path.lstrip('/'))

    def request(self, method: str, path: str, params: Optional[dict] = None,
                json: Optional[dict] = None, data: Optional[dict] = None,
                headers: Optional[dict] = None, **kwargs) -> requests.Response:
        url = self._build_url(path)
        logger.info("%s %s", method.upper(), url)
        return self.session.request(method=method.upper(), url=url,
                                    params=params, json=json, data=data,
                                    headers=headers or {}, **kwargs)

    def get(self, path: str, **kwargs) -> requests.Response:
        return self.request("GET", path, **kwargs)

    def post(self, path: str, **kwargs) -> requests.Response:
        return self.request("POST", path, **kwargs)

    def put(self, path: str, **kwargs) -> requests.Response:
        return self.request("PUT", path, **kwargs)

    def delete(self, path: str, **kwargs) -> requests.Response:
        return self.request("DELETE", path, **kwargs)
