from match_settings import Setting


class OutputParser:
    @classmethod
    def print_output_for_predict_outcome(cls, result):
        print(cls.result_string(result))

    @classmethod
    def result_string(cls, result):
        if cls.is_integer(result):
            return cls.run_string(result)
        return cls.wicket_string(1)

    @staticmethod
    def is_integer(result):
        return type(result) == int

    @staticmethod
    def run_string(run_count):
        if run_count == 0 or run_count == 1:
            return f"{run_count} run"
        return f"{run_count} runs"

    @staticmethod
    def wicket_string(wickets_count):
        if wickets_count == 0 or wickets_count == 1:
            return f"{wickets_count} wicket"
        return f"{wickets_count} wickets"

    @classmethod
    def print_super_over_won_output(cls, score, wicket):
        print(cls.score_string(score))
        print(cls.won_string(wicket))

    @classmethod
    def score_string(cls, result):
        return f"{Setting.COUNTRY_NAME} scored: {cls.result_string(result)}"

    @classmethod
    def won_string(cls, wickets_count):
        return f"{Setting.COUNTRY_NAME} won by {cls.wicket_string(wickets_count)}"

    @classmethod
    def print_super_over_lost_output(cls, score, lost_by):
        print(cls.score_string(score))
        print(cls.lost_string(lost_by))

    @classmethod
    def lost_string(cls, score):
        return f"{Setting.COUNTRY_NAME} lost by {cls.result_string(score)}"

    @classmethod
    def print_output_for_predict_outcome_with_comment(cls, comment, result):
        print(f"{comment} - {cls.result_string(result)}")

    @classmethod
    def print_batting_details(cls, current_batsman, shot, timing):
        print(f"{current_batsman} played {timing} {shot} shot")

    @staticmethod
    def print_bowling_details(bowler, bowl):
        print(f"{bowler} bowled {bowl} ball,")
