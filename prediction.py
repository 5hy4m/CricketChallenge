from input_parser import InputParser
import random


class Prediction:
    def __init__(self):
        self.parser = InputParser()
        (
            self.bowling_cards,
            self.batting_cards,
            self.timings,
            self.runs,
        ) = self.parser.read_outcome_chart()


class PredictOutcome(Prediction):
    def __init__(self):
        super().__init__()
        self.bowl, self.shot, self.timing = self.parser.parse_input()

    def result(self):
        return random.choice(self.timings[self.timing]["probable_runs"])

    def comment(self, result):
        return random.choice(self.runs[str(result)]["probable_comments"])


class SuperOver(Prediction):
    def __init__(self):
        super().__init__()
        self.wickets = 0
        self.remaining_balls = 6
        self.chase_runs = 11
        self.batsman_names = ["Craig", "Paul"]
        self.bowler_name = "Sudhakar"

    def predict_bowl_type(self, shot):
        return random.choice(self.batting_cards[self.shot]["probable_bowl"])

    def start_innings(self):
        while self.remaining_balls:
            self.shot, self.timing = self.parser.parse_input()
            self.bowl = self.predict_bowl_type(self.shot)
            OutputParser.print_bowler_details(self.bowler_name, self.bowl)
            import pdb

            pdb.set_trace()
            self.remaining_balls -= 1
            print(self.shot)
            print(self.bowl)
            print(self.remaining_balls)
