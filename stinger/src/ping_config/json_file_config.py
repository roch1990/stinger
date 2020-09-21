import json

from jsonschema import validate, ValidationError

from log import get_logger
from src.ping_config.json_schema import schema

logger = get_logger()


class JsonFileConfig:

    def __init__(
            self,
            config_addr: str,
    ):
        self.body: str = config_addr

    def as_str(self) -> str:
        with open(self.body, 'r') as config:
            file = config.read()
        return file

    def as_dict(self, config: str) -> dict:
        try:
            config_as_dict = json.loads(config)
            validate(instance=config_as_dict, schema=schema)
        except (json.JSONDecodeError, ValidationError) as err:
            logger.error(f'Invalid configuration: {self.body}')
            logger.error(err)
            return {}
        return json.loads(config)
