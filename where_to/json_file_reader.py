import json
import logging
from logging.config import dictConfig

from settings import LOGGING_CONFIG

dictConfig(LOGGING_CONFIG)
logger = logging.getLogger()


class JSONFileReader(object):
    @staticmethod
    def _get_json(f):
        with open(f, "r") as json_file:
            data = json.load(json_file)
            logger.info("Parsed '{f}' into JSON: {data}".format(f=f,
                                                                data=data))
        return data
