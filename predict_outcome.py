from output_parser import OutputParser
from prediction import Prediction
from error_constants import PREDICT_OUTCOME_PARSE_ERROR


class PredictOutcome(Prediction):
    def __init__(self):
        super().__init__()
        try:
            self.bowl, self.shot, self.timing = self.parser.parse_input()
        except ValueError:
            raise ValueError(PREDICT_OUTCOME_PARSE_ERROR)

    def predict(self):
        result = self.get_result_of_current_bowl()
        OutputParser.print_output_for_predict_outcome(result)

    def predict_with_comment(self):
        result = self.get_result_of_current_bowl()
        comment = self.get_comment(result)
        OutputParser.print_output_for_predict_outcome_with_comment(comment, result)
