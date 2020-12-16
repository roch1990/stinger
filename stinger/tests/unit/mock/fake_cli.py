from typing import TypeVar

import pytest

from src.api.status import AiohttpApi


class FakeCliStruct:

    def __init__(
            self,
            api: AiohttpApi,
            cli: TypeVar
    ):
        self.cli = cli
        self.api = api


@pytest.fixture
def fake_cli(loop, aiohttp_client) -> FakeCliStruct:
    http_api = AiohttpApi(jobs=dict())
    http_api.init_routes()
    return FakeCliStruct(
        api=http_api,
        cli=loop.run_until_complete(
            aiohttp_client(
                http_api.app
            )
        )
    )
