from constants import INTRO_STRING
import input_parser as InputParser
from constants import ChallengeSelectionChoices
from predict_outcome import PredictOutcome
from super_over import PredictSuperOver
from error_messages_and_handlers import CHALLENGE_SELECTION_PARSE_ERROR_MESSAGE


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
        raise ValueError(CHALLENGE_SELECTION_PARSE_ERROR_MESSAGE)


if __name__ == "__main__":
    main()
