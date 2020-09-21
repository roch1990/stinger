import time

import requests

import log
from src.ping_config.json_parsed_config import JsonParsedConfig

logger = log.get_logger()


class SyncClient:

    def __init__(
            self,
            config: JsonParsedConfig,
    ):
        self.config = config
        super().__init__()

    def do_request(self):
        """
        Infinite request loop.
        :return: None
        """
        retry_attempt = 0

        while True:
            start = time.time()
            session = requests.Session()

            if self.config.headers and self.config.headers.get('Content-Type') == 'application/json':
                req = requests.Request(
                    method=self.config.method,
                    url=self.config.base_url,
                    headers=self.config.headers,
                    json=self.config.payload,
                )
            else:
                req = requests.Request(
                    method=self.config.method,
                    url=self.config.base_url,
                    headers=self.config.headers,
                    data=self.config.payload,
                )
            try:
                response = session.send(
                    request=req.prepare(),
                    verify=False,
                    timeout=2,
                )
                stop = time.time()
                logger.info(
                    f'{self.config.base_url} request result: {response.status_code}, '
                    f'response time: {stop - start} sec',
                )
                retry_attempt = 0
            except requests.exceptions.ReadTimeout as err:
                logger.warning(f'{self.config.base_url} request error: {err}')
                if retry_attempt < 10:
                    retry_attempt += 1
                else:
                    raise err

            time.sleep(self.config.timeout)
