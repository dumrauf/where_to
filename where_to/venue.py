import logging
from logging.config import dictConfig

from settings import LOGGING_CONFIG
from where_to.input_normaliser import InputNormaliser

dictConfig(LOGGING_CONFIG)
logger = logging.getLogger()


class Venue(InputNormaliser):
    def __init__(self, name, food, drinks):
        self.name = name
        self.food = food
        self.drinks = drinks
        self.normalised_food = self.normalise_list_of_strings(lst=self.food)
        logger.info("Normalised '{food}' at venue '{venue}' into "
                    "'{normalised_food}'".format(venue=self,
                                                 food=self.food,
                                                 normalised_food=self.normalised_food))
        self.normalised_drinks = self.normalise_list_of_strings(lst=self.drinks)
        logger.info("Normalised '{drinks}' at venue '{venue}' into "
                    "'{normalised_drinks}'".format(venue=self,
                                                   drinks=self.drinks,
                                                   normalised_drinks=self.normalised_drinks))

    def get_available_food(self):
        return self.normalised_food

    def get_available_drinks(self):
        return self.normalised_drinks

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return self.name
