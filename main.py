from constants import INTRO_STRING
from input_parser import InputParser
from constants import ChallengeSelectionChoices
from prediction import PredictOutcome
from super_over import SuperOver
from output_parser import OutputParser


def main():
    print(INTRO_STRING)
    selection = InputParser.parse_challenge_selection()
    if selection == ChallengeSelectionChoices.PREDICT_OUTCOME_CHALLENGE:
        result = PredictOutcome().get_result_of_current_bowl()
        OutputParser.print_output_for_predict_outcome(result)
    elif selection == ChallengeSelectionChoices.PREDICT_OUTCOME_CHALLENGE_WITH_COMMENTS:
        prediction = PredictOutcome()
        result = prediction.get_result_of_current_bowl()
        comment = prediction.give_comment(result)
        OutputParser.print_output_for_predict_outcome_with_comments(comment, result)
    elif selection == ChallengeSelectionChoices.SUPER_OVER_CHALLENGE:
        SuperOver().start_innings()


if __name__ == "__main__":
    main()
