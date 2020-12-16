import pytest
from aiohttp import web

import tests.unit.mock.fake_cli as fake_cli
from src.thread.concurrent_call import ConcurrentCall


@pytest.mark.parametrize(
    'test_result,route,status_code,jobs,res',
    [
        # success request
        (
            True,
            '/status',
            200,
            {'test': ConcurrentCall(None, None)},
            {'test': True}
        ),
        (
            False,
            '/status',
            200,
            {},
            {}
        ),
    ]
)
async def test_status(
        fake_cli: fake_cli.FakeCliStruct,
        mocker,
        test_result: bool,
        route: str,
        status_code: int,
        jobs: dict,
        res: dict
):
    fake_cli.api.jobs = jobs
    mocker.patch(
        'src.thread.concurrent_call.ConcurrentCall.status',
        return_value=res.get('test')
    )

    req: web.Response = await fake_cli.cli.get(route)
    response = await req.json()
    assert req.status == status_code
    assert response == res
