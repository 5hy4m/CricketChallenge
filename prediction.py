import random
from input_parser import InputParser


class Prediction:
    def __init__(self):
        self.parser = InputParser()
        (
            self.batting_cards,
            self.timings,
            self.runs,
        ) = self.parser.read_outcome_chart()

    def get_comment(self, result):
        try:
            return random.choice(self.runs[str(result)]["probable_comments"])
        except KeyError as err:
            raise err

    def get_result_of_current_bowl(self):
        try:
            return random.choice(self.timings[self.timing]["probable_runs"])
        except KeyError as err:
            raise err
