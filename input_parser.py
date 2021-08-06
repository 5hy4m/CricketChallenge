import json


class InputParser:
    def parse_input_for_predict_outcome(self):
        input_array = input().split(" ")
        return [string.upper() for string in input_array]

    @staticmethod
    def parse_challenge_selection():
        return int(input())

    @staticmethod
    def read_outcome_chart():
        try:
            with open("outcome_chart.json") as f:
                outcome_chart = json.load(f)
            return (
                outcome_chart["bowling_cards"],
                outcome_chart["batting_cards"],
                outcome_chart["shot_time"],
                outcome_chart["runs"],
            )
        except FileNotFoundError as error:
            raise error
