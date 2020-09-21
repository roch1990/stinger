import log
from src.api.status import AiohttpApi
from src.client.sync_client import SyncClient
from src.ping_config.json_file_config import JsonFileConfig
from src.ping_config.json_folder import JsonFolder
from src.ping_config.json_parsed_config import JsonParsedConfig
from src.thread.concurrent_call import ConcurrentCall

logger = log.get_logger()


def parse_config_folder():
    config_list = []
    configs_addrs_tuple = JsonFolder.config_as_tuple()
    for config_addrs in configs_addrs_tuple:
        config = JsonFileConfig(config_addrs)

        config_as_dict = config.as_dict(
            config.as_str(),
        )
        if not config_as_dict:
            continue
        json_config = JsonParsedConfig(
            **config_as_dict
        )

        config_list.append(json_config)
    return config_list


def start_background_ping_jobs(config_list):
    jobs = {}
    logger.info('Start background jobs')
    for config in config_list:
        client = SyncClient(
            config,
        )
        call = ConcurrentCall(name=f'{config.base_url}', target=client.do_request)
        call.start()
        jobs.update(
            **{f'{config.name}': call}
        )
    return jobs


def start_http_api(jobs):
    logger.info('HTTP API start')
    http_api = AiohttpApi(jobs=jobs)
    http_api.init_routes()
    call = ConcurrentCall(name='api', target=http_api.run_server(http_api.aiohttp_server()))
    call.start()


try:
    start_http_api(
        start_background_ping_jobs(
            parse_config_folder(),
        ),
    )
except (KeyboardInterrupt, SystemExit):
    logger.warning('Manual interruption')
