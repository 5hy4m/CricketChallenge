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


class TestInputParser(unittest.TestCase):
    def setUp(self):
        self.mocker = InputMock()
        self.parser = InputParser()

    @mock.patch("builtins.input")
    def test_challenge_selection_parser(self, mock_input):
        ChallengeSelectionMock.execute(
            mock_input,
            data=ChallengeSelectionChoices.PREDICT_OUTCOME_CHALLENGE,
        )
        selection = self.parser.parse_challenge_selection()
        self.assertEqual(
            selection,
            ChallengeSelectionChoices.PREDICT_OUTCOME_CHALLENGE,
        )

    @mock.patch("builtins.input")
    def test_predict_outcome_input_parser(self, mock_input):
        self.mocker.execute(
            mock_input,
            data=MockChallenges.PREDICT_OUTCOME_MOCK_INPUT,
        )
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

    # @mock.patch("builtins.input")
    # def test_super_over_input_parser(self, mock_input):
    #     self.mocker.execute(
    #         mock_input,
    #         data=MockChallenges.SUPER_OVER_CHALLENGE_MOCK_INPUT,
    #     )
    #     () = self.parser.parse_input_for_super_over()
