from input_parser import InputParser

import random
from output_parser import OutputParser


class Prediction:
    def __init__(self):
        self.parser = InputParser()
        (
            self.batting_cards,
            self.timings,
            self.runs,
        ) = self.parser.read_outcome_chart()

    def give_comment(self, result):
        return random.choice(self.runs[str(result)]["probable_comments"])

    def get_result_of_current_bowl(self):
        return random.choice(self.timings[self.timing]["probable_runs"])
