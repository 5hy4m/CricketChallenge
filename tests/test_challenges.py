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
from tests.test_constants import PredictOutComeConstants
from predict_outcome import PredictOutcome
from super_over import PredictSuperOver


class TestChallenges(unittest.TestCase):
    def setUp(self):
        (
            self.batting_cards,
            self.shot_timings,
            self.runs,
        ) = InputParser().read_outcome_chart()

    @mock.patch("input_parser.InputParser.parse_input")
    def test_predict_outcome(self, mock_input):
        mock_input.return_value = PredictOutComeConstants.PARSED_VALUES
        self.assertTrue(
            PredictOutcome().predict_outcome_using_shot_timing()
            in self.shot_timings[PredictOutComeConstants.PARSED_VALUES[2]][
                "probable_runs"
            ]
        )

    @mock.patch("input_parser.InputParser.parse_input")
    def test_errors_of_predict_outcome(self, mock_input):
        mock_input.return_value = PredictOutComeConstants.ERROR_INPUT3
        with self.assertRaises(KeyError):
            PredictOutcome().predict_outcome_using_shot_timing()

    @mock.patch("input_parser.InputParser.parse_input")
    def test_predict_outcome_with_comments(self, mock_input):
        mock_input.return_value = PredictOutComeConstants.PARSED_VALUES_2
        result = PredictOutcome().predict_outcome_using_shot_timing()
        comment = PredictOutcome().predict_comment_using_bowl_outcome(result)
        self.assertTrue(comment in self.runs[str(result)]["probable_comments"])

    @mock.patch("input_parser.InputParser.parse_input")
    def test_errors_of_predict_outcome(self, mock_input):
        mock_input.return_value = PredictOutComeConstants.ERROR_INPUT3
        with self.assertRaises(KeyError):
            PredictOutcome().predict_outcome_using_shot_timing()

    def test_super_over_challenge_predict_bowl_type(self):
        played_shot = "STRAIGHT"
        bowl = PredictSuperOver().predict_bowl_type_using_shot_type(played_shot)
        self.assertTrue(bowl in self.batting_cards[played_shot]["probable_bowl"])
