import logging
from logging.config import dictConfig

from settings import LOGGING_CONFIG
from where_to.users import Users
from where_to.venues import Venues

dictConfig(LOGGING_CONFIG)
logger = logging.getLogger()


USER_KEY = 'USER'
AVAILABLE_FOOD_KEY = 'AVAILABLE_FOOD'
AVAILABLE_DRINKS_KEY = 'AVAILABLE_DRINKS'


class VenueRecommender(object):
    def __init__(self, users_file, venues_file):
        self.users = Users(users_file=users_file)
        self.venues = Venues(venues_file=venues_file)

    def _get_venues_verdicts(self):
        venues_verdicts = {}
        for venue in self.venues.all():
            venue_verdict = []
            for user in self.users.all():
                available_food = user.get_available_food(venue=venue)
                available_drinks = user.get_available_drinks(venue=venue)
                user_verdict = {
                    USER_KEY: user,
                    AVAILABLE_FOOD_KEY: available_food,
                    AVAILABLE_DRINKS_KEY: available_drinks,
                }
                venue_verdict.append(user_verdict)
            venues_verdicts[venue] = venue_verdict
        return venues_verdicts

    def _is_suitable_for_all_users(self, venue_verdict):
        for user_verdict in venue_verdict:
            if not user_verdict[AVAILABLE_FOOD_KEY] or not user_verdict[AVAILABLE_DRINKS_KEY]:
                logger.info("User verdict {user_verdict} in venue verdict {venue_verdict} makes venue "
                            "UNSUITABLE!".format(venue_verdict=venue_verdict,
                                                 user_verdict=user_verdict))
                return False
        logger.info("Venue verdict {venue_verdict} is suitable for all users".format(venue_verdict=venue_verdict))
        return True

    def _get_places_to_go(self, venues_verdicts):
        places_to_go = []
        for venue, venue_verdict in venues_verdicts.items():
            if self._is_suitable_for_all_users(venue_verdict=venue_verdict):
                places_to_go.append(venue)
        logger.info("Places to go: {places_to_go}".format(places_to_go=places_to_go))
        return places_to_go

    def _get_string_of_places_to_go(self, venues_verdicts):
        places_to_go = self._get_places_to_go(venues_verdicts=venues_verdicts)
        if not places_to_go:
            s = "No places to go.\n"
        else:
            s = "Places to go:\n"
            for venue in places_to_go:
                s += ' - {venue_name}\n'.format(venue_name=venue.name)
        return s

    def _get_places_to_avoid(self, venues_verdicts):
        places_to_avoid = []
        for venue, venue_verdict in venues_verdicts.items():
            if not self._is_suitable_for_all_users(venue_verdict=venue_verdict):
                places_to_avoid.append(venue)
        logger.info("Places to avoid: {places_to_avoid}".format(places_to_avoid=places_to_avoid))
        return places_to_avoid

    def _get_string_of_places_to_avoid(self, venues_verdicts):
        places_to_avoid = self._get_places_to_avoid(venues_verdicts=venues_verdicts)
        if not places_to_avoid:
            s = "No places to avoid.\n"
        else:
            s = "Places to avoid:\n"
            for venue in places_to_avoid:
                s += ' - {venue_name}\n'.format(venue_name=venue.name)
                for user_verdict in venues_verdicts[venue]:
                    user = user_verdict[USER_KEY]
                    if not user_verdict[AVAILABLE_DRINKS_KEY]:
                        s += '     * There is nothing to drink for {user_name}\n'.format(user_name=user.name)
                    if not user_verdict[AVAILABLE_FOOD_KEY]:
                        s += '     * There is nothing to eat for {user_name}\n'.format(user_name=user.name)
        return s

    def print_recommendations(self):
        venues_verdicts = self._get_venues_verdicts()
        places_to_go = self._get_string_of_places_to_go(venues_verdicts=venues_verdicts)
        places_to_avoid = self._get_string_of_places_to_avoid(venues_verdicts=venues_verdicts)
        print "{places_to_go}{places_to_avoid}".format(places_to_go=places_to_go,
                                                       places_to_avoid=places_to_avoid),  # Note the comma in order to avoid the newline! (see also <https://stackoverflow.com/a/11685717>)
