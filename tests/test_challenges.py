import unittest
import os
import sys
from unittest.mock import patch
from unittest import mock

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from constants import ChallengeSelectionChoices
from tests.test_constants import SuperOverConstants
import input_parser as InputParser
from tests.test_constants import PredictOutComeConstants
from predict_outcome import PredictOutcome
from super_over import PredictSuperOver


class TestChallenges(unittest.TestCase):
    def setUp(self):
        (
            self.batting_cards,
            self.shot_timings,
            self.runs,
        ) = InputParser.read_outcome_chart()

    @mock.patch("input_parser.parse_input_with_printable_name")
    def test_predict_outcome_using_shot_timing(self, mock_input):
        """
        Check predicted outcome using shot timing belongs to probable outcomes.
        """
        mock_input.return_value = PredictOutComeConstants.PARSED_VALUES
        self.assertTrue(
            PredictOutcome().predict_outcome_using_shot_timing()
            in self.shot_timings[PredictOutComeConstants.PARSED_VALUES[2]["key"]][
                "probable_runs"
            ]
        )

    @mock.patch("input_parser.parse_input_with_printable_name")
    def test_predict_outcome_with_comments(self, mock_input):
        """
        Check predicted comment using bowl outcome belongs to probable comments.
        """
        mock_input.return_value = PredictOutComeConstants.PARSED_VALUES_2
        result = PredictOutcome().predict_outcome_using_shot_timing()
        comment = PredictOutcome().predict_comment_using_bowl_outcome(result)
        self.assertTrue(comment in self.runs[str(result)]["probable_comments"])

    @mock.patch("input_parser.parse_input_with_printable_name")
    def test_super_over_challenge_predict_bowl_type(self, mock_input):
        """
        Check predicted bowl type using played shot belongs to probable bowl types.
        """
        mock_input.return_value = SuperOverConstants.INPUT_SIDE_EFFECTS[0]
        super_over = PredictSuperOver()
        super_over.set_shot_and_timing_values_from_input()
        played_shot = SuperOverConstants.INPUT_SIDE_EFFECTS[0][0]
        bowl = super_over.predict_bowl_type_using_shot_type()
        self.assertTrue(bowl in self.batting_cards[played_shot["key"]]["probable_bowl"])
