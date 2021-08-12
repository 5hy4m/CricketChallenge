from constants import INTRO_STRING
from input_parser import InputParser
from constants import ChallengeSelectionChoices
from predict_outcome import PredictOutcome
from super_over import PredictSuperOver


def main():
    print(INTRO_STRING)
    selection = InputParser.parse_challenge_selection()
    if selection == ChallengeSelectionChoices.PREDICT_OUTCOME_CHALLENGE:
        PredictOutcome().predict()
    elif selection == ChallengeSelectionChoices.PREDICT_OUTCOME_CHALLENGE_WITH_COMMENTS:
        PredictOutcome().predict_with_comment()
    elif selection == ChallengeSelectionChoices.SUPER_OVER_CHALLENGE:
        PredictSuperOver().start_second_innings()
    else:
        raise ValueError(selection)


if __name__ == "__main__":
    main()
