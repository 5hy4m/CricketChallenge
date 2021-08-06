from input_parser import InputParser
import random


class Prediction:
    def __init__(self):
        parser = InputParser()
        (
            self.bowling_cards,
            self.batting_cards,
            self.timings,
            self.runs,
        ) = parser.read_outcome_chart()
        self.bowl, self.shot, self.timing = parser.parse_input_for_predict_outcome()


class PredictOutcome(Prediction):
    def result(self):
        return random.choice(self.timings[self.timing]["probable_runs"])
