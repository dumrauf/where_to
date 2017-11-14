import argparse
import sys

from where_to.venue_recommender import VenueRecommender


def _parse_args(args):
    parser = argparse.ArgumentParser(description='Just One - Finds Venues Suitable for all Users')
    parser.add_argument('--venues',
                        required=True,
                        type=unicode,
                        help='The file containing the venues as JSON')
    parser.add_argument('--users',
                        required=True,
                        type=unicode,
                        help='The file containing the users as JSON')
    args = parser.parse_args()
    return args


def main():
    parser = _parse_args(sys.argv[1:])
    venue_recommender = VenueRecommender(users_file=parser.users,
                                         venues_file=parser.venues)
    venue_recommender.print_recommendations()


if __name__ == "__main__":
    main()
