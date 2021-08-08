from constants import COUNTRY_NAME


class OutputParser:
    @staticmethod
    def wicket_string(wickets_count=None):
        if not wickets_count:
            return f"1 wicket"
        if wickets_count == 0 or wickets_count == 1:
            return f"{wickets_count} wicket"
        else:
            return f"{wickets_count} wickets"

    @classmethod
    def result_string(cls, result):
        if cls.is_integer(result):
            if result == 0 or result == 1:
                return f"{result} run"
            else:
                return f"{result} runs"
        else:
            return cls.wicket_string()

    @classmethod
    def score_string(cls, result):
        return f"{COUNTRY_NAME} scored: {cls.result_string(result)}"

    @staticmethod
    def is_integer(result):
        return type(result) == int

    @classmethod
    def won_string(cls, wickets_count):
        return f"{COUNTRY_NAME} won by {cls.wicket_string(wickets_count)}"

    @classmethod
    def lost_string(cls, score):
        return f"{COUNTRY_NAME} lost by {cls.result_string(score)}"

    @classmethod
    def print_output_for_predict_outcome(cls, result):
        print(cls.result_string(result))

    @classmethod
    def print_super_over_won_output(cls, score, wicket):
        print(cls.score_string(score))
        print(cls.won_string(wicket))

    @classmethod
    def print_super_over_lost_output(cls, score, lost_by):
        print(cls.score_string(score))
        print(cls.lost_string(lost_by))

    @classmethod
    def print_output_for_predict_outcome_with_comments(cls, comment, result):
        print(f"{comment} - {cls.result_string(result)}")

    @classmethod
    def print_bowling_details(cls, bowler, bowl):
        print(f"{bowler} bowled {bowl} ball,")

    @classmethod
    def print_batting_details(cls, current_batsman, shot, timing):
        print(f"{current_batsman} played {timing} {shot} shot")
