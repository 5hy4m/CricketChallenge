import random
from output_parser import OutputParser
from constants import BOWLER_NAME, BATSMEN_NAMES, COUNTRY_NAME
from prediction import Prediction


class SuperOver(Prediction):
    def __init__(self):
        super().__init__()
        self.wickets = 0
        self.remaining_balls = 6
        self.target = 11
        self.score = 0
        self.batsmen_names = BATSMEN_NAMES
        self.bowler_name = BOWLER_NAME
        self.country_name = COUNTRY_NAME
        self.maximum_wicket = 2

    def predict_bowl_type(self, shot):
        return random.choice(self.batting_cards[shot]["probable_bowl"])

    def is_target_achieved(self):
        return self.score > self.target

    def is_all_out(self):
        return self.wickets >= self.maximum_wicket

    def can_bowl(self):
        return (
            self.remaining_balls
            and not self.is_target_achieved()
            and not self.is_all_out()
        )

    def print_output_for_current_bowl(self, result, printable_shot, printable_timing):
        current_batsman = self.batsmen_names[self.wickets]
        bowl = self.predict_bowl_type(self.shot)
        comment = self.give_comment(result)
        OutputParser.print_bowling_details(self.bowler_name, bowl)
        OutputParser.print_batting_details(
            current_batsman, printable_shot, printable_timing
        )
        OutputParser.print_output_for_predict_outcome_with_comments(comment, result)

    def bowl_six_balls(self):
        while self.can_bowl():
            (
                (printable_shot, self.shot),
                (printable_timing, self.timing),
            ) = self.parser.parse_input_with_printable_name()
            result = self.get_result_of_current_bowl()
            self.print_output_for_current_bowl(result, printable_shot, printable_timing)
            self.remaining_balls -= 1
            if result == "wicket":
                self.wickets += 1
                continue
            self.score += result

    def start_innings(self):
        self.bowl_six_balls()
        if self.is_target_achieved():
            balance_wickets = self.maximum_wicket - self.wickets
            OutputParser.print_super_over_won_output(self.score, balance_wickets)
            return
        lost_by = self.target - self.score
        OutputParser.print_super_over_lost_output(self.score, lost_by)
