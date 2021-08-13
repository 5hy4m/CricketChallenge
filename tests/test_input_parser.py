import unittest
import os
import sys
from unittest.mock import patch
from unittest import mock

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from constants import ChallengeSelectionChoices
from input_parser import InputParser
from tests.test_constants import PredictOutComeConstants, SuperOverConstants
from super_over import PredictSuperOver
from predict_outcome import PredictOutcome


class TestInputParser(unittest.TestCase):
    def setUp(self):
        self.parser = InputParser()

    @mock.patch("builtins.input")
    def test_challenge_selection_parser(self, mock_input):
        mock_input.return_value = ChallengeSelectionChoices.PREDICT_OUTCOME_CHALLENGE
        selection = self.parser.parse_challenge_selection()
        self.assertEqual(
            selection,
            ChallengeSelectionChoices.PREDICT_OUTCOME_CHALLENGE,
        )

    @mock.patch("builtins.input")
    def test_predict_outcome_input_parser(self, mock_input):
        mock_input.return_value = PredictOutComeConstants.MOCK_INPUT
        bowl, shot, timing = self.parser.parse_input()
        self.assertEqual(
            bowl,
            PredictOutComeConstants.MOCK_INPUT.split(" ")[0].upper(),
        )
        self.assertEqual(
            shot,
            PredictOutComeConstants.MOCK_INPUT.split(" ")[1].upper(),
        )
        self.assertEqual(
            timing,
            PredictOutComeConstants.MOCK_INPUT.split(" ")[2].upper(),
        )

    @mock.patch("builtins.input")
    def test_errors_of_predict_outcome_input_parser(self, mock_input):
        with self.assertRaises(ValueError):
            mock_input.return_value = PredictOutComeConstants.ERROR_INPUT1
            PredictOutcome()

        with self.assertRaises(ValueError):
            mock_input.return_value = PredictOutComeConstants.ERROR_INPUT2
            PredictOutcome()

    @mock.patch("builtins.input")
    def test_super_over_input_parser(self, mock_input):
        mock_input.return_value = SuperOverConstants.MOCK_INPUT
        shot, timing = self.parser.parse_input_with_printable_name()
        self.assertEqual(
            shot,
            SuperOverConstants.INPUT_SIDE_EFFECTS[0][0],
        )
        self.assertEqual(
            timing,
            SuperOverConstants.INPUT_SIDE_EFFECTS[0][1],
        )

    @mock.patch("builtins.input")
    def test_errors_of_super_over_input_parser(self, mock_input):
        with self.assertRaises(ValueError):
            mock_input.return_value = SuperOverConstants.ERROR_INPUT1
            PredictSuperOver().set_shot_and_timing_values_from_input()

        with self.assertRaises(ValueError):
            mock_input.return_value = SuperOverConstants.ERROR_INPUT2
            PredictSuperOver().set_shot_and_timing_values_from_input()


if __name__ == "__main__":
    unittest.main()
