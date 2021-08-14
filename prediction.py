import random
import input_parser as InputParser
from output_parser import OutputParser


class Prediction:
    def __init__(self):
        self.parser = InputParser
        (
            self.batting_cards,
            self.shot_timings,
            self.runs,
        ) = self.parser.read_outcome_chart()

    def predict_comment_using_bowl_outcome(self, result):
        try:
            return random.choice(self.runs[str(result)]["probable_comments"])
        except KeyError as err:
            raise err

    def predict_outcome_using_shot_timing(self):
        try:
            # TODO Check THe name of the Vars Here Timing and shot_timings
            return random.choice(self.shot_timings[self.played_timing]["probable_runs"])
        except KeyError as err:
            raise err

    def predict_bowl_type_using_shot_type(self, played_shot):
        try:
            return random.choice(self.batting_cards[played_shot]["probable_bowl"])
        except KeyError as err:
            raise err
