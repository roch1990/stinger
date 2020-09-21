from os import listdir
from os.path import isfile, join

from config import Config


class JsonFolder:

    @staticmethod
    def config_as_tuple():
        onlyfiles = [f'{Config.config_path}{f}' for f in listdir(Config.config_path) if isfile(join(Config.config_path, f))]
        return tuple(onlyfiles)
