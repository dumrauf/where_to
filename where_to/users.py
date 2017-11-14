import logging
from logging.config import dictConfig

from settings import LOGGING_CONFIG
from where_to.json_file_reader import JSONFileReader
from where_to.user import User

dictConfig(LOGGING_CONFIG)
logger = logging.getLogger()


class Users(JSONFileReader):
    def _get_users(self, users_file):
        users = []
        users_data = self._get_json(f=users_file)
        for user_data in users_data:
            name = user_data['name']
            wont_eat = user_data['wont_eat']
            drinks = user_data['drinks']
            user = User(name=name,
                        wont_eat=wont_eat,
                        drinks=drinks)
            users.append(user)
        return users

    def __init__(self, users_file):
        self.users = self._get_users(users_file=users_file)
        logger.info("List of all users: {users}".format(users=self))

    def all(self):
        return self.users

    def __repr__(self):
        return str(self.users)
