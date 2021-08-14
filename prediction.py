import random
import input_parser as InputParser
from error_messages_and_handlers import KEY_ERROR_MESSAGE, key_error_handler


class Prediction:
    def __init__(self):
        self.parser = InputParser
        (
            self.batting_cards,
            self.shot_timings,
            self.runs,
        ) = self.parser.read_outcome_chart()

    @key_error_handler
    def predict_comment_using_bowl_outcome(self, result):
        return self.predict_from_probable_values(
            self.runs[str(result)]["probable_comments"]
        )

    @staticmethod
    @key_error_handler
    def predict_from_probable_values(probable_values):
        return random.choice(probable_values)

    @key_error_handler
    def predict_outcome_using_shot_timing(self):
        return self.predict_from_probable_values(
            self.shot_timings[self.played_timing["key"]]["probable_runs"]
        )

    @key_error_handler
    def predict_bowl_type_using_shot_type(self):
        return self.predict_from_probable_values(
            self.batting_cards[self.played_shot["key"]]["probable_bowl"]
        )
