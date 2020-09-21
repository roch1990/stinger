import asyncio
from typing import Dict

from aiohttp import web
from aiohttp.web_exceptions import HTTPBadRequest, HTTPInternalServerError, HTTPOk

from config import Config
from log import get_logger
from src.thread.concurrent_call import ConcurrentCall

logger = get_logger()


class AiohttpApi:

    def __init__(self, jobs: Dict[str, ConcurrentCall]):
        self.app = web.Application()
        self.jobs = jobs

    def init_routes(self):
        self.app.add_routes(
            [
                web.get('/status', self.status),
                web.patch('/restart/{name}', self.restart_thread),
            ],
        )

    def aiohttp_server(self):
        return web.AppRunner(self.app)

    def run_server(self, runner: web.AppRunner):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(runner.setup())
        site = web.TCPSite(runner, Config.api_host, Config.api_port)
        loop.run_until_complete(site.start())
        logger.info(f'HTTP API serve at {Config.api_host}:{Config.api_port}')
        loop.run_forever()

    async def status(self, request):
        result = {}
        for name, job in self.jobs.items():
            result.update(
                **{name: job.status()}
            )
        return web.json_response(data=result)

    async def restart_thread(self, request):
        thread_name = request.match_info.get('name')
        thread = self.jobs.get(thread_name)
        if not thread_name:
            raise HTTPBadRequest
        thread.daemon = True
        thread.start()
        if not thread.status():
            raise HTTPInternalServerError
        raise HTTPOk
