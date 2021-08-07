from constants import INTRO_STRING
from input_parser import InputParser
from constants import ChallengeSelectionChoices
from prediction import PredictOutcome


class OutputParser:
    @staticmethod
    def wicket_string():
        return "1 wicket"

    @classmethod
    def result_string(cls, result):
        if cls.is_integer(result):
            if result == 0:
                return f"{result} run"
            else:
                return f"{result} runs"
        else:
            return cls.wicket_string()

    @staticmethod
    def is_integer(result):
        return type(result) == int

    @classmethod
    def print_output_for_predict_outcome(cls, result):
        print(cls.result_string(result))

    @classmethod
    def print_output_for_predict_outcome_with_comments(cls, comment, result):
        print(f"{comment} - {cls.result_string(result)}")


def main():
    print(INTRO_STRING)
    selection = InputParser.parse_challenge_selection()
    if selection == ChallengeSelectionChoices.PREDICT_OUTCOME_CHALLENGE:
        result = PredictOutcome().result()
        OutputParser.print_output_for_predict_outcome(result)
    elif selection == ChallengeSelectionChoices.PREDICT_OUTCOME_CHALLENGE_WITH_COMMENTS:
        prediction = PredictOutcome()
        result = prediction.result()
        comment = prediction.comment(result)
        OutputParser.print_output_for_predict_outcome_with_comments(comment, result)


if __name__ == "__main__":
    main()
