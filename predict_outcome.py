import output_parser as OutputParser
from prediction import Prediction
from error_messages_and_handlers import predict_outcome_value_error_handler


class PredictOutcome(Prediction):
    @predict_outcome_value_error_handler
    def __init__(self):
        super().__init__()
        (
            self.bowl,
            self.played_shot,
            self.played_timing,
        ) = self.parser.parse_input_with_printable_name()

    def predict(self):
        bowl_outcome = self.predict_outcome_using_shot_timing()
        OutputParser.print_output_for_predict_outcome(bowl_outcome)

    def predict_with_comment(self):
        bowl_outcome = self.predict_outcome_using_shot_timing()
        comment = self.predict_comment_using_bowl_outcome(bowl_outcome)
        OutputParser.print_output_for_outcome_with_comment(comment, bowl_outcome)
