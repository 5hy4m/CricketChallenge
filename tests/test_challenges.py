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
from tests.mocks import InputMock, ChallengeSelectionMock, SuperOverMock
from tests.test_constants import MockChallenges
from prediction import PredictOutcome
from super_over import PredictSuperOver


class TestChallenges(unittest.TestCase):
    def setUp(self):
        (
            self.bowling_cards,
            self.batting_cards,
            self.timings,
            self.runs,
        ) = InputParser().read_outcome_chart()

    @mock.patch("input_parser.InputParser.parse_input")
    def test_predict_outcome(self, mock_input):
        InputMock().execute(
            mock_input, data=MockChallenges.PREDICT_OUTCOME_MOCK_INPUT_PARSED_VALUES
        )
        self.assertTrue(
            PredictOutcome().get_result_of_current_bowl()
            in self.timings[MockChallenges.PREDICT_OUTCOME_MOCK_INPUT_PARSED_VALUES[2]][
                "probable_runs"
            ]
        )

    @mock.patch("input_parser.InputParser.parse_input")
    def test_predict_outcome_with_comments(self, mock_input):
        InputMock().execute(
            mock_input, data=MockChallenges.PREDICT_OUTCOME_MOCK_INPUT_PARSED_VALUES_2
        )
        result = PredictOutcome().get_result_of_current_bowl()
        comment = PredictOutcome().give_comment(result)
        self.assertTrue(comment in self.runs[str(result)]["probable_comments"])

    def test_super_over_challenge_predict_bowl_type(self):
        shot = "STRAIGHT"
        bowl = PredictSuperOver().predict_bowl_type(shot)
        self.assertTrue(bowl in self.batting_cards[shot]["probable_bowl"])
