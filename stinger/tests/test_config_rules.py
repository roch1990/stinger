import json

from jsonschema import validate, ValidationError

from src.ping_config.json_file_config import JsonFileConfig
from src.ping_config.json_folder import JsonFolder
from src.ping_config.json_schema import schema


def test_configs():
    configs_addrs_tuple = JsonFolder.config_as_tuple()
    for config_addrs in configs_addrs_tuple:
        config = JsonFileConfig(config_addrs)
        config = config.as_str()
        try:
            config_as_dict = json.loads(config)
            validate(instance=config_as_dict, schema=schema)
        except (json.JSONDecodeError, ValidationError) as err:
            raise err
