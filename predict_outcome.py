import output_parser as OutputParser
from prediction import Prediction
from error_constants import PREDICT_OUTCOME_PARSE_ERROR


class PredictOutcome(Prediction):
    def __init__(self):
        super().__init__()
        try:
            self.bowl, self.played_shot, self.played_timing = self.parser.parse_input()
        except ValueError:
            raise ValueError(PREDICT_OUTCOME_PARSE_ERROR)

    def predict(self):
        bowl_outcome = self.predict_outcome_using_shot_timing()
        OutputParser.print_output_for_predict_outcome(bowl_outcome)

    def predict_with_comment(self):
        bowl_outcome = self.predict_outcome_using_shot_timing()
        comment = self.predict_comment_using_bowl_outcome(bowl_outcome)
        OutputParser.print_output_for_outcome_with_comment(comment, bowl_outcome)
