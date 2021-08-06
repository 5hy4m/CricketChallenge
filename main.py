from constants import INTRO_STRING
from input_parser import InputParser
from constants import ChallengeSelectionChoices
from prediction import PredictOutcome


def main():
    print(INTRO_STRING)
    selection = InputParser.parse_challenge_selection()
    if selection == ChallengeSelectionChoices.PREDICT_OUTCOME_CHALLENGE:
        result = PredictOutcome().result()


if __name__ == "__main__":
    main()
