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
from tests.mock_constants import MockChallenges


class TestInputParser(unittest.TestCase):
    def setUp(self):
        pass

    @mock.patch("builtins.input")
    def test_challenge_selection_parser(self, mock_input):
        ChallengeSelectionMock.execute(
            mock_input, data=ChallengeSelectionChoices.SELECT_PREDICT_OUTCOME_CHALLENGE
        )
        selection = InputParser.parse_challenge_selection()
        self.assertEqual(
            selection, ChallengeSelectionChoices.SELECT_PREDICT_OUTCOME_CHALLENGE
        )

    @mock.patch("builtins.input")
    def test_predict_outcome_input_parser(self, mock_input):
        InputMock.execute(mock_input, data=MockChallenges.PREDICT_OUTCOME_MOCK)
        bowl_card, shot_card, shot_timing = InputParser.parse()
        print(bowl_card, shot_card, shot_timing)
