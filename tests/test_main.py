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
from tests.mocks import InputMock, ChallengeSelectionMock
from tests.test_constants import MockChallenges
from prediction import PredictOutcome


class TestMainFlow(unittest.TestCase):
    def setUp(self):
        self.mocker = InputMock()
        (
            self.bowling_cards,
            self.batting_cards,
            self.timings,
            self.runs,
        ) = InputParser().read_outcome_chart()

    @mock.patch("input_parser.InputParser.parse_input_for_predict_outcome")
    @patch("input_parser.InputParser.parse_challenge_selection")
    def test_main_for_predict_outcome_challenge(
        self, mock_selection, mock_input_for_predict_outcome
    ):
        self.mocker.execute(
            mock_selection, ChallengeSelectionChoices.PREDICT_OUTCOME_CHALLENGE
        )
        self.mocker.execute(
            mock_input_for_predict_outcome,
            MockChallenges.PREDICT_OUTCOME_MOCK_INPUT_PARSED_VALUES,
        )
        self.assertTrue(
            PredictOutcome().result()
            in self.timings[MockChallenges.PREDICT_OUTCOME_MOCK_INPUT_PARSED_VALUES[2]][
                "probable_runs"
            ]
        )
