import logging
from logging.config import dictConfig

from settings import LOGGING_CONFIG
from where_to.input_normaliser import InputNormaliser

dictConfig(LOGGING_CONFIG)
logger = logging.getLogger()


class User(InputNormaliser):
    def __init__(self, name, wont_eat, drinks):
        self.name = name
        self.wont_eat = wont_eat
        self.drinks = drinks
        self.normalised_wont_eat = self.normalise_list_of_strings(lst=self.wont_eat)
        logger.info("Normalised '{wont_eat}' for user '{user}' into "
                    "'{normalised_wont_eat}'".format(user=self,
                                                     wont_eat=self.wont_eat,
                                                     normalised_wont_eat=self.normalised_wont_eat))
        self.normalised_drinks = self.normalise_list_of_strings(lst=self.drinks)
        logger.info("Normalised '{drinks}' for user '{user}' into "
                    "'{normalised_drinks}'".format(user=self,
                                                   drinks=self.drinks,
                                                   normalised_drinks=self.normalised_drinks))

    def get_available_food(self, venue):
        available_food = []
        for food in venue.get_available_food():
            if food not in self.normalised_wont_eat:
                available_food.append(food)
        logger.info("Available food for user '{user}' at venue '{venue}' is"
                    "'{available_food}'".format(user=self,
                                                venue=venue,
                                                available_food=available_food))
        return available_food

    def get_available_drinks(self, venue):
        available_drinks = []
        for drink in venue.get_available_drinks():
            if drink in self.normalised_drinks:
                available_drinks.append(drink)
        logger.info("Available drinks for user '{user}' at venue '{venue}' are "
                    "'{available_drinks}'".format(user=self,
                                                  venue=venue,
                                                  available_drinks=available_drinks))
        return available_drinks

    def __repr__(self):
        return self.name
