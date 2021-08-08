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
from tests.test_constants import MockChallenges, Result
from prediction import PredictOutcome, SuperOver


class TestChallenges(unittest.TestCase):
    @mock.patch("input_parser.InputParser.parse_input")
    def test_predict_outcome(self, mock_input):
        (
            self.bowling_cards,
            self.batting_cards,
            self.timings,
            self.runs,
        ) = InputParser().read_outcome_chart()
        InputMock().execute(
            mock_input, data=MockChallenges.PREDICT_OUTCOME_MOCK_INPUT_PARSED_VALUES
        )
        self.assertTrue(
            PredictOutcome().result()
            in self.timings[MockChallenges.PREDICT_OUTCOME_MOCK_INPUT_PARSED_VALUES[2]][
                "probable_runs"
            ]
        )

    @mock.patch("input_parser.InputParser.parse_input")
    def test_predict_outcome_with_comments(self, mock_input):
        (
            self.bowling_cards,
            self.batting_cards,
            self.timings,
            self.runs,
        ) = InputParser().read_outcome_chart()
        InputMock().execute(
            mock_input, data=MockChallenges.PREDICT_OUTCOME_MOCK_INPUT_PARSED_VALUES_2
        )
        result = PredictOutcome().result()
        comment = PredictOutcome().comment(result)
        self.assertTrue(comment in self.runs[str(result)]["probable_comments"])

    @mock.patch("input_parser.InputParser.parse_input")
    def test_super_over_challenge(self, mock_input):
        mock_input.side_effect = (
            MockChallenges.SUPER_OVER_CHALLENGE_MOCK_INPUT_PARSED_VALUES
        )
        result = SuperOver().start_innings()
        print(result)
