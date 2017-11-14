import os
import sys
from unittest import TestCase

from just_one import main
from settings import BASE_DIR
from tests.testing_utils import capture
from where_to.errors import DuplicateVenueError


class TestJustOne(TestCase):
    @staticmethod
    def _get_path_inside_test_directory(*args):
        return os.path.join(BASE_DIR, 'tests', 'inputs', *args)

    @staticmethod
    def _get_expected_output(f):
        with open(f, "r") as expected_output_file:
            expected_output = expected_output_file.read()
        return expected_output

    ####################################################################################################################
    # Arguments Tests
    ####################################################################################################################
    def test_cli_input_parameters_venues_missing(self):
        sys.argv = ['just_one.py',
                    '--users', 'inputs/users.json']
        self.assertRaises(SystemExit, main)

    def test_cli_input_parameters_users_missing(self):
        sys.argv = ['just_one.py',
                    '--venues', 'inputs/venues.json']
        self.assertRaises(SystemExit, main)

    ####################################################################################################################
    # Error Code Handling Tests
    ####################################################################################################################
    def test_venues_with_same_name(self):
        sys.argv = ['just_one.py',
                    '--users', self._get_path_inside_test_directory('venues_with_same_name', 'users.json'),
                    '--venues', self._get_path_inside_test_directory('venues_with_same_name', 'venues.json')]
        self.assertRaises(DuplicateVenueError, main)

    ####################################################################################################################
    # End to End Tests
    ####################################################################################################################
    def test_case_insensitive_food(self):
        sys.argv = ['just_one.py',
                    '--users', self._get_path_inside_test_directory('case_insensitive_food', 'users.json'),
                    '--venues', self._get_path_inside_test_directory('case_insensitive_food', 'venues.json')]
        expected_output = self._get_expected_output(f=self._get_path_inside_test_directory('case_insensitive_food',
                                                                                           'expected_output.txt'))
        with capture(main) as output:
            pass
        main()
        self.assertEqual(expected_output,
                         output)

    def test_case_insensitive_drinks(self):
        sys.argv = ['just_one.py',
                    '--users', self._get_path_inside_test_directory('case_insensitive_drinks', 'users.json'),
                    '--venues', self._get_path_inside_test_directory('case_insensitive_drinks', 'venues.json')]
        expected_output = self._get_expected_output(f=self._get_path_inside_test_directory('case_insensitive_drinks',
                                                                                           'expected_output.txt'))
        with capture(main) as output:
            pass
        main()
        self.assertEqual(expected_output,
                         output)

    def test_no_drinks(self):
        sys.argv = ['just_one.py',
                    '--users', self._get_path_inside_test_directory('no_drinks', 'users.json'),
                    '--venues', self._get_path_inside_test_directory('no_drinks', 'venues.json')]
        expected_output = self._get_expected_output(f=self._get_path_inside_test_directory('no_drinks',
                                                                                           'expected_output.txt'))
        with capture(main) as output:
            pass
        main()
        self.assertEqual(expected_output,
                         output)

    def test_no_food(self):
        sys.argv = ['just_one.py',
                    '--users', self._get_path_inside_test_directory('no_food', 'users.json'),
                    '--venues', self._get_path_inside_test_directory('no_food', 'venues.json')]
        expected_output = self._get_expected_output(f=self._get_path_inside_test_directory('no_food',
                                                                                           'expected_output.txt'))
        with capture(main) as output:
            pass
        main()
        self.assertEqual(expected_output,
                         output)

    def test_food_but_no_drinks_for_at_least_one(self):
        sys.argv = ['just_one.py',
                    '--users', self._get_path_inside_test_directory('food_but_no_drinks_for_at_least_one', 'users.json'),
                    '--venues', self._get_path_inside_test_directory('food_but_no_drinks_for_at_least_one', 'venues.json')]
        expected_output = self._get_expected_output(f=self._get_path_inside_test_directory('food_but_no_drinks_for_at_least_one',
                                                                                           'expected_output.txt'))
        with capture(main) as output:
            pass
        main()
        self.assertEqual(expected_output,
                         output)

    def test_drinks_but_no_food_for_at_least_one(self):
        sys.argv = ['just_one.py',
                    '--users', self._get_path_inside_test_directory('drinks_but_no_food_for_at_least_one', 'users.json'),
                    '--venues', self._get_path_inside_test_directory('drinks_but_no_food_for_at_least_one', 'venues.json')]
        expected_output = self._get_expected_output(f=self._get_path_inside_test_directory('drinks_but_no_food_for_at_least_one',
                                                                                           'expected_output.txt'))
        with capture(main) as output:
            pass
        main()
        self.assertEqual(expected_output,
                         output)

    def test_sample_input(self):
        sys.argv = ['just_one.py',
                    '--users', self._get_path_inside_test_directory('sample_input', 'users.json'),
                    '--venues', os.path.join(BASE_DIR, 'tests', 'inputs', 'sample_input', 'venues.json')]
        expected_output = self._get_expected_output(f=self._get_path_inside_test_directory('sample_input',
                                                                                           'expected_output.txt'))
        with capture(main) as output:
            pass
        main()
        self.assertEqual(expected_output,
                         output)
