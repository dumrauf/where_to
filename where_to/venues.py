import logging
from logging.config import dictConfig

from settings import LOGGING_CONFIG
from where_to.errors import DuplicateVenueError
from where_to.json_file_reader import JSONFileReader
from where_to.venue import Venue

dictConfig(LOGGING_CONFIG)
logger = logging.getLogger()


class Venues(JSONFileReader):
    def _get_venues(self, venues_file):
        venues = []
        venues_data = self._get_json(f=venues_file)
        for venue_data in venues_data:
            name = venue_data['name']
            food = venue_data['food']
            drinks = venue_data['drinks']
            venue = Venue(name=name,
                          food=food,
                          drinks=drinks)
            if venue in venues:
                raise DuplicateVenueError("'A venue '{venue}' already exists in the list of venues "
                                          "'{venues}'".format(venue=venue,
                                                              venues=venues))
            venues.append(venue)
        return venues

    def __init__(self, venues_file):
        self.venues = self._get_venues(venues_file=venues_file)
        logger.info("List of all venues: {venues}".format(venues=self))

    def all(self):
        return self.venues

    def __repr__(self):
        return str(self.venues)
