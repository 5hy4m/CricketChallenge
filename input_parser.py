import json
from error_constants import CHALLENGE_SELECTION_PARSE_ERROR


def read_outcome_chart():
    with open("outcome_chart.json") as f:
        outcome_chart = json.load(f)
    return (
        outcome_chart["batting_cards"],
        outcome_chart["shot_time"],
        outcome_chart["runs"],
    )


def parse_input_with_printable_name():
    input_array = split_input_as_array()
    return [{"name": string, "key": string.upper()} for string in input_array]


def split_input_as_array():
    return input().split(" ")


def parse_challenge_selection():
    try:
        return int(input())
    except ValueError:
        raise ValueError(CHALLENGE_SELECTION_PARSE_ERROR)
