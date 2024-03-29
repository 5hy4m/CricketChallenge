import unittest
import os
import sys
from unittest.mock import patch
from unittest import mock

from io import StringIO

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from constants import (
    ChallengeSelectionChoices,
    INTRO_STRING,
)
from match_settings import Setting
import input_parser as InputParser
from tests.test_constants import (
    PredictOutComeConstants,
    SuperOverConstants,
    SuperOverTwoWicketsConstants,
    SuperOverThreeBallsVictoryConstants,
)
from main import main
import output_parser as OutputParser


@patch("match_settings.Setting.BATSMEN_NAMES", ["Craig", "Paul"])
@patch("match_settings.Setting.BOWLER_NAME", "Sudhakar")
@patch("match_settings.Setting.COUNTRY_NAME", "AUSTRALIA")
@patch("match_settings.Setting.TARGET", 11)
@patch("match_settings.Setting.MAXIMUM_WICKETS", 2)
class TestMainFlow(unittest.TestCase):
    def setUp(self):
        (
            self.batting_cards,
            self.shot_timings,
            self.runs,
        ) = InputParser.read_outcome_chart()

    def remove_intro_string(self, output):
        string = output.getvalue().replace(INTRO_STRING, "")
        return string.replace("\n", "")

    @mock.patch("input_parser.parse_input_with_printable_name")
    @patch("input_parser.parse_challenge_selection")
    def test_main_for_predict_outcome_challenge(
        self, mock_selection, mock_input_for_predict_outcome
    ):
        """
        Test full flow of predict outcome challenge.
        """
        mock_selection.return_value = (
            ChallengeSelectionChoices.PREDICT_OUTCOME_CHALLENGE
        )
        mock_input_for_predict_outcome.return_value = (
            PredictOutComeConstants.PARSED_VALUES
        )
        with patch("sys.stdout", new=StringIO()) as output:
            main()
            string = self.remove_intro_string(output)
            number, outcome = string.split(" ")
            if outcome == "wicket":
                self.assertEqual(string, "1 wicket")
            else:
                self.assertEqual(string, f"{number} runs")

    @mock.patch("input_parser.parse_input_with_printable_name")
    @patch("input_parser.parse_challenge_selection")
    def test_main_for_predict_outcome_challenge_with_comments(
        self, mock_selection, mock_input_for_predict_outcome
    ):
        """
        Test full flow of predict outcome with comment challenge.
        """
        mock_selection.return_value = (
            ChallengeSelectionChoices.PREDICT_OUTCOME_CHALLENGE_WITH_COMMENTS
        )
        mock_input_for_predict_outcome.return_value = (
            PredictOutComeConstants.PARSED_VALUES_2
        )
        with patch("sys.stdout", new=StringIO()) as output:
            main()
            string = self.remove_intro_string(output)
            comment, result = string.split(" - ")
            number, outcome = result.split(" ")
            self.assertEqual(string, f"{comment} - {number} {outcome}")

    def test_super_over_challenge_output_for_each_ball(self):
        """
        Test output of a ball in super over challenge.
        """
        with patch("sys.stdout", new=StringIO()) as output:
            wickets_taken = 0
            OutputParser.print_bowling_details("Bouncer")
            OutputParser.print_batting_details(wickets_taken, "Straight", "Perfect")
            OutputParser.print_output_for_outcome_with_comment(
                "Excellent line and length", 1
            )
            string = self.remove_intro_string(output)
            self.assertEqual(
                string,
                f"""{Setting.BOWLER_NAME} bowled Bouncer ball,{Setting.BATSMEN_NAMES[0]} played Perfect Straight shotExcellent line and length - 1 run""",
            )

    @patch("prediction.Prediction.predict_comment_using_bowl_outcome")
    @patch("prediction.Prediction.predict_outcome_using_shot_timing")
    @patch("super_over.PredictSuperOver.predict_bowl_type_using_shot_type")
    @patch("input_parser.parse_input_with_printable_name")
    @patch("input_parser.parse_challenge_selection")
    def test_super_over_challenge_flow(
        self,
        mock_selection,
        mock_input_for_super_over,
        mock_bowl,
        mock_result_of_current_bowl,
        mock_comment,
    ):
        """
        Test full flow of super over challenge
        where the batsmen plays 6 balls.
        """
        mock_selection.return_value = ChallengeSelectionChoices.SUPER_OVER_CHALLENGE
        mock_input_for_super_over.side_effect = SuperOverConstants.INPUT_SIDE_EFFECTS
        mock_bowl.side_effect = SuperOverConstants.BOWL_SIDE_EFFECTS
        mock_result_of_current_bowl.side_effect = (
            SuperOverConstants.RESULTS_SIDE_EFFECTS
        )
        mock_comment.side_effect = SuperOverConstants.COMMENTS_SIDE_EFFECTS
        with patch("sys.stdout", new=StringIO()) as output:
            main()
            string = self.remove_intro_string(output)
            self.assertEqual.__self__.maxDiff = None
            self.assertEqual(
                string,
                SuperOverConstants.OUTPUT,
            )

    @patch("prediction.Prediction.predict_comment_using_bowl_outcome")
    @patch("prediction.Prediction.predict_outcome_using_shot_timing")
    @patch("super_over.PredictSuperOver.predict_bowl_type_using_shot_type")
    @patch("input_parser.parse_input_with_printable_name")
    @patch("input_parser.parse_challenge_selection")
    def test_super_over_challenge_flow_after_two_wickets(
        self,
        mock_selection,
        mock_input_for_super_over,
        mock_bowl,
        mock_result_of_current_bowl,
        mock_comment,
    ):
        """
        Test full flow of super over challenge
        where the batsmen will play 2 balls and lose the match.
        """
        mock_selection.return_value = ChallengeSelectionChoices.SUPER_OVER_CHALLENGE
        mock_input_for_super_over.side_effect = (
            SuperOverTwoWicketsConstants.INPUT_SIDE_EFFECTS
        )
        mock_bowl.side_effect = SuperOverTwoWicketsConstants.BOWL_SIDE_EFFECTS
        mock_result_of_current_bowl.side_effect = (
            SuperOverTwoWicketsConstants.RESULTS_SIDE_EFFECTS
        )
        mock_comment.side_effect = SuperOverTwoWicketsConstants.COMMENTS_SIDE_EFFECTS
        with patch("sys.stdout", new=StringIO()) as output:
            main()
            string = self.remove_intro_string(output)
            self.assertEqual.__self__.maxDiff = None
            self.assertEqual(
                string,
                SuperOverTwoWicketsConstants.OUTPUT,
            )

    @patch("prediction.Prediction.predict_comment_using_bowl_outcome")
    @patch("prediction.Prediction.predict_outcome_using_shot_timing")
    @patch("super_over.PredictSuperOver.predict_bowl_type_using_shot_type")
    @patch("input_parser.parse_input_with_printable_name")
    @patch("input_parser.parse_challenge_selection")
    def test_super_over_challenge_flow_with_three_balls_victory(
        self,
        mock_selection,
        mock_input_for_super_over,
        mock_bowl,
        mock_result_of_current_bowl,
        mock_comment,
    ):
        """
        Test full flow of super over challenge
        where the batsmen will play 3 balls and win the match.
        """
        mock_selection.return_value = ChallengeSelectionChoices.SUPER_OVER_CHALLENGE
        mock_input_for_super_over.side_effect = (
            SuperOverThreeBallsVictoryConstants.INPUT_SIDE_EFFECTS
        )
        mock_bowl.side_effect = SuperOverThreeBallsVictoryConstants.BOWL_SIDE_EFFECTS
        mock_result_of_current_bowl.side_effect = (
            SuperOverThreeBallsVictoryConstants.RESULTS_SIDE_EFFECTS
        )
        mock_comment.side_effect = (
            SuperOverThreeBallsVictoryConstants.COMMENTS_SIDE_EFFECTS
        )
        with patch("sys.stdout", new=StringIO()) as output:
            main()
            string = self.remove_intro_string(output)
            self.assertEqual.__self__.maxDiff = None
            self.assertEqual(
                string,
                SuperOverThreeBallsVictoryConstants.OUTPUT_SIDE_EFFECTS,
            )

    def test_super_over_challenge_output_for_won_output(self):
        """
        Test won output in super over challenge.
        """
        with patch("sys.stdout", new=StringIO()) as output:
            OutputParser.print_super_over_won_output(12, 1)
            string = self.remove_intro_string(output)
            self.assertEqual(
                string,
                f"""AUSTRALIA scored: 12 runsAUSTRALIA won by 1 wicket""",
            )

    def test_super_over_challenge_output_for_lost_output(self):
        """
        Test lost output in super over challenge.
        """
        with patch("sys.stdout", new=StringIO()) as output:
            OutputParser.print_super_over_lost_output(9)
            string = self.remove_intro_string(output)
            self.assertEqual(
                string,
                f"""AUSTRALIA scored: 9 runsAUSTRALIA lost by 2 runs""",
            )


if __name__ == "__main__":
    unittest.main()
