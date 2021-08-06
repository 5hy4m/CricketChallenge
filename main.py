from constants import INTRO_STRING
from input_parser import InputParser
from constants import ChallengeSelectionChoices
from prediction import PredictOutcome


class OutputParser:
    @staticmethod
    def print_wicket():
        print("1 wicket")

    @staticmethod
    def print_result(result):
        if result == 0:
            print(f"{result} run")
        else:
            print(f"{result} runs")

    @staticmethod
    def is_result_integer(result):
        return type(result) == int

    @classmethod
    def print_outcome(cls, selection, result):
        if selection == ChallengeSelectionChoices.PREDICT_OUTCOME_CHALLENGE:
            if cls.is_result_integer(result):
                cls.print_result(result)
            else:
                cls.print_wicket()


def main():
    print(INTRO_STRING)
    selection = InputParser.parse_challenge_selection()
    if selection == ChallengeSelectionChoices.PREDICT_OUTCOME_CHALLENGE:
        result = PredictOutcome().result()
    OutputParser.print_outcome(selection, result)


if __name__ == "__main__":
    main()
