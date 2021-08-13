import random
from output_parser import OutputParser
from prediction import Prediction
from error_constants import SUPER_OVER_PARSE_ERROR
from match_settings import Setting


class PredictSuperOver(Prediction):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.wickets_taken = 0
        self.remaining_balls = 6
        self.played_shot = None
        self.played_timing = None

    def start_second_innings(self):
        self.bowl_six_balls()
        if self.is_target_achieved():
            OutputParser.print_super_over_won_output(self.score, self.wickets_taken)
            return
        OutputParser.print_super_over_lost_output(self.score)

    def bowl_six_balls(self):
        while self.can_bowl():
            self.set_shot_and_timing_values_from_input()
            self.bowl_outcome = self.predict_outcome_using_shot_timing()
            self.process_commentry_for_current_ball()
            self.prepare_for_next_bowl()

    def can_bowl(self):
        return (
            self.remaining_balls
            and not self.is_target_achieved()
            and not self.is_all_out()
        )

    def is_target_achieved(self):
        return self.score > Setting.TARGET

    def is_all_out(self):
        return self.wickets_taken >= Setting.MAXIMUM_WICKETS

    def set_shot_and_timing_values_from_input(self):
        try:
            (
                self.played_shot,
                self.played_timing,
            ) = self.parser.parse_input_with_printable_name()
        except ValueError:
            raise ValueError(SUPER_OVER_PARSE_ERROR)

    def prepare_for_next_bowl(self):
        self.remaining_balls -= 1
        if self.is_wicket(self.bowl_outcome):
            self.wickets_taken += 1
        else:
            self.score += self.bowl_outcome

    def process_commentry_for_current_ball(self):
        bowl = self.predict_bowl_type_using_shot_type(self.played_shot["key"])
        comment = self.predict_comment_using_bowl_outcome(self.bowl_outcome)
        OutputParser.print_bowling_details(bowl)
        OutputParser.print_batting_details(
            self.wickets_taken,
            self.played_shot["name"],
            self.played_timing["name"],
        )
        OutputParser.print_output_for_outcome_with_comment(
            comment,
            self.bowl_outcome,
        )

    @staticmethod
    def is_wicket(outcome):
        return outcome == "wicket"
