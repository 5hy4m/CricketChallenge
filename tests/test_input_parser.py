import unittest
import os
import sys
from unittest.mock import patch
from unittest import mock

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from constants import ChallengeSelectionChoices
import input_parser as InputParser
from tests.test_constants import PredictOutComeConstants, SuperOverConstants
from super_over import PredictSuperOver
from predict_outcome import PredictOutcome


class TestInputParser(unittest.TestCase):
    def setUp(self):
        self.parser = InputParser

    @mock.patch("builtins.input")
    def test_challenge_selection_parser(self, mock_input):
        """
        Check valid input for challenge selection input parser.
        """
        mock_input.return_value = ChallengeSelectionChoices.PREDICT_OUTCOME_CHALLENGE
        selection = self.parser.parse_challenge_selection()
        self.assertEqual(
            selection,
            ChallengeSelectionChoices.PREDICT_OUTCOME_CHALLENGE,
        )

    @mock.patch("builtins.input")
    def test_predict_outcome_input_parser(self, mock_input):
        """
        Check valid input for predict outcome input parser.
        """
        mock_input.return_value = PredictOutComeConstants.MOCK_INPUT
        bowl, played_shot, played_timing = self.parser.parse_input_with_printable_name()
        self.assertEqual(
            bowl,
            {
                "name": PredictOutComeConstants.MOCK_INPUT.split(" ")[0],
                "key": PredictOutComeConstants.MOCK_INPUT.split(" ")[0].upper(),
            },
        )
        self.assertEqual(
            played_shot,
            {
                "name": PredictOutComeConstants.MOCK_INPUT.split(" ")[1],
                "key": PredictOutComeConstants.MOCK_INPUT.split(" ")[1].upper(),
            },
        )
        self.assertEqual(
            played_timing,
            {
                "name": PredictOutComeConstants.MOCK_INPUT.split(" ")[2],
                "key": PredictOutComeConstants.MOCK_INPUT.split(" ")[2].upper(),
            },
        )

    @mock.patch("input_parser.parse_input_with_printable_name")
    def test_errors_of_predict_outcome_using_shot_timing(self, mock_input):
        """
        Check KeyError in predict_outcome_input_parser
        when invalid input is provided.
        """
        mock_input.return_value = PredictOutComeConstants.ERROR_INPUT3
        with self.assertRaises(KeyError):
            PredictOutcome().predict_outcome_using_shot_timing()

    @mock.patch("builtins.input")
    def test_errors_of_predict_outcome_input_parser(self, mock_input):
        """
        Check KeyError in predict_outcome_input_parser
        when insufficient input is provided.
        """
        with self.assertRaises(ValueError):
            mock_input.return_value = PredictOutComeConstants.ERROR_INPUT1
            PredictOutcome()

        with self.assertRaises(ValueError):
            mock_input.return_value = PredictOutComeConstants.ERROR_INPUT2
            PredictOutcome()

    @mock.patch("builtins.input")
    def test_super_over_input_parser(self, mock_input):
        """
        Check valid input for super over input parser.
        """
        mock_input.return_value = SuperOverConstants.MOCK_INPUT
        played_shot, played_timing = self.parser.parse_input_with_printable_name()
        self.assertEqual(
            played_shot,
            SuperOverConstants.INPUT_SIDE_EFFECTS[0][0],
        )
        self.assertEqual(
            played_timing,
            SuperOverConstants.INPUT_SIDE_EFFECTS[0][1],
        )

    @mock.patch("builtins.input")
    def test_errors_of_super_over_input_parser(self, mock_input):
        """
        Check ValueError in super_over_input_parser
        when insufficient input is provided.
        """
        with self.assertRaises(ValueError):
            mock_input.return_value = SuperOverConstants.ERROR_INPUT1
            PredictSuperOver().set_shot_and_timing_values_from_input()

        with self.assertRaises(ValueError):
            mock_input.return_value = SuperOverConstants.ERROR_INPUT2
            PredictSuperOver().set_shot_and_timing_values_from_input()


if __name__ == "__main__":
    unittest.main()
