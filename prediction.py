from input_parser import InputParser

from output_parser import OutputParser
import random
from constants import BOWLER_NAME, BATSMEN_NAMES, COUNTRY_NAME


class Prediction:
    def __init__(self):
        self.parser = InputParser()
        (
            self.bowling_cards,
            self.batting_cards,
            self.timings,
            self.runs,
        ) = self.parser.read_outcome_chart()

    def comment(self, result):
        return random.choice(self.runs[str(result)]["probable_comments"])

    def result(self):
        return random.choice(self.timings[self.timing]["probable_runs"])


class PredictOutcome(Prediction):
    def __init__(self):
        super().__init__()
        self.bowl, self.shot, self.timing = self.parser.parse_input()


class SuperOver(Prediction):
    def __init__(self):
        super().__init__()
        self.wickets = 0
        self.remaining_balls = 6
        self.chase = 11
        self.score = 0
        self.batsmen_names = BATSMEN_NAMES
        self.bowler_name = BOWLER_NAME
        self.country_name = COUNTRY_NAME
        self.maximum_wicket = 2

    def predict_bowl_type(self, shot):
        return random.choice(self.batting_cards[shot]["probable_bowl"])

    def start_innings(self):
        while self.remaining_balls:
            if self.score > self.chase:
                OutputParser.print_super_over_won_output(self.score, self.wickets)
                break
            current_batsman = self.batsmen_names[self.wickets]
            (
                (
                    printable_shot,
                    self.shot,
                ),
                (
                    printable_timing,
                    self.timing,
                ),
            ) = self.parser.parse_input_with_printable_name()
            bowl = self.predict_bowl_type(self.shot)
            result = self.result()
            comment = self.comment(result)
            OutputParser.print_bowling_details(self.bowler_name, bowl)
            OutputParser.print_batting_details(
                current_batsman, printable_shot, printable_timing
            )
            OutputParser.print_output_for_predict_outcome_with_comments(comment, result)
            self.remaining_balls -= 1
            if result == "wicket":
                self.wickets += 1
                if self.wickets >= self.maximum_wicket:
                    break
            else:
                self.score += result
        if self.score > self.chase:
            OutputParser.print_super_over_won_output(self.score, self.wickets)
        else:
            lost_by = self.chase - self.score
            OutputParser.print_super_over_lost_output(self.score, lost_by)
