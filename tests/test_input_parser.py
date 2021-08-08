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
from tests.test_constants import MockChallenges


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
        mock_input.return_value = MockChallenges.PREDICT_OUTCOME_MOCK_INPUT
        bowl, shot, timing = self.parser.parse_input()
        self.assertEqual(
            bowl, MockChallenges.PREDICT_OUTCOME_MOCK_INPUT.split(" ")[0].upper()
        )
        self.assertEqual(
            shot, MockChallenges.PREDICT_OUTCOME_MOCK_INPUT.split(" ")[1].upper()
        )
        self.assertEqual(
            timing, MockChallenges.PREDICT_OUTCOME_MOCK_INPUT.split(" ")[2].upper()
        )
