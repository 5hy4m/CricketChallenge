import json
from error_constants import (
    CHALLENGE_SELECTION_PARSE_ERROR,
    PREDICT_OUTCOME_PARSE_ERROR,
    SUPER_OVER_PARSE_ERROR,
)


class InputParser:
    @staticmethod
    def split_input_as_array():
        return input().split(" ")

    def parse_input(self):
        input_array = self.split_input_as_array()
        if len(input_array) == 3:
            return [string.upper() for string in input_array]
        raise ValueError(PREDICT_OUTCOME_PARSE_ERROR)

    def parse_input_with_printable_name(self):
        input_array = self.split_input_as_array()
        if len(input_array) == 2:
            return [(string, string.upper()) for string in input_array]
        raise ValueError(SUPER_OVER_PARSE_ERROR)

    @staticmethod
    def parse_challenge_selection():
        try:
            return int(input())
        except ValueError:
            raise ValueError(CHALLENGE_SELECTION_PARSE_ERROR)

    @staticmethod
    def read_outcome_chart():
        try:
            with open("outcome_chart.json") as f:
                outcome_chart = json.load(f)
            return (
                outcome_chart["batting_cards"],
                outcome_chart["shot_time"],
                outcome_chart["runs"],
            )
        except FileNotFoundError as error:
            raise error
