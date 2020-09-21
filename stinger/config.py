import os


class Config:

    config_path = os.getenv('CONFIG_PATH', './stinger/configs/')
    log_level = os.getenv('LOG_LEVEL', 'INFO')

    api_host = os.getenv('API_HOST', '127.0.0.1')
    api_port = os.getenv('API_PORT', 8080)
