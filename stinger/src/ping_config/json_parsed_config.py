from typing import Optional


class JsonParsedConfig:

    def __init__(
            self,
            uri: str,
            name: str,
            route: str,
            method: str,
            timeout: int,
            port: Optional[int] = '',
            headers: Optional[dict] = None,
            payload: Optional[dict] = None,
    ):
        self.base_url = f'{uri}{route}'
        self.name = name
        self.method = method
        self.headers = headers
        self.port = port
        self.payload = payload
        self.timeout = timeout
