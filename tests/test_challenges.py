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
from tests.test_constants import MockChallenges, Result
from prediction import PredictOutcome


class TestChallenges(unittest.TestCase):
    @mock.patch("input_parser.InputParser.parse_input_for_predict_outcome")
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
