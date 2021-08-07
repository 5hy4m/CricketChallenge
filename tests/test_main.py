import unittest
import os
import sys
from unittest.mock import patch
from unittest import mock

from io import StringIO

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from constants import ChallengeSelectionChoices, INTRO_STRING
from input_parser import InputParser
from tests.mocks import InputMock, ChallengeSelectionMock
from tests.test_constants import MockChallenges
from main import main


class TestMainFlow(unittest.TestCase):
    def setUp(self):
        self.mocker = InputMock()
        (
            self.bowling_cards,
            self.batting_cards,
            self.timings,
            self.runs,
        ) = InputParser().read_outcome_chart()

    def remove_intro_string(self, output):
        string = output.getvalue().replace(INTRO_STRING, "")
        return string.replace("\n", "")

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
        with patch("sys.stdout", new=StringIO()) as output:
            main()
            string = self.remove_intro_string(output)
            number, outcome = string.split(" ")
            if outcome == "wicket":
                self.assertEqual(string, "1 wicket")
            else:
                self.assertEqual(string, f"{number} runs")

    @mock.patch("input_parser.InputParser.parse_input_for_predict_outcome")
    @patch("input_parser.InputParser.parse_challenge_selection")
    def test_main_for_predict_outcome_challenge_with_comments(
        self, mock_selection, mock_input_for_predict_outcome
    ):
        self.mocker.execute(
            mock_selection,
            ChallengeSelectionChoices.PREDICT_OUTCOME_CHALLENGE_WITH_COMMENTS,
        )
        self.mocker.execute(
            mock_input_for_predict_outcome,
            MockChallenges.PREDICT_OUTCOME_MOCK_INPUT_PARSED_VALUES_2,
        )
        with patch("sys.stdout", new=StringIO()) as output:
            main()
            string = self.remove_intro_string(output)
            comment, result = string.split(" - ")
            number, outcome = result.split(" ")
            self.assertEqual(string, f"{comment} - {number} {outcome}")
