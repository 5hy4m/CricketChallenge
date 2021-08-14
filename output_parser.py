from match_settings import Setting


def print_output_for_predict_outcome(result):
    print(result_string(result))


def result_string(result):
    if is_integer(result):
        return run_string(result)
    return wicket_string(1)


def is_integer(result):
    return type(result) == int


def run_string(run_count):
    if run_count == 0 or run_count == 1:
        return f"{run_count} run"
    return f"{run_count} runs"


def wicket_string(wickets_count):
    if wickets_count == 0 or wickets_count == 1:
        return f"{wickets_count} wicket"
    return f"{wickets_count} wickets"


def print_output_for_outcome_with_comment(comment, result):
    print(f"{comment} - {result_string(result)}")


def print_output_for_a_bowl_in_super_over(
    wickets_taken, played_shot, played_timing, bowl_outcome, bowl, comment
):
    print_bowling_details(bowl)
    print_batting_details(wickets_taken, played_shot["name"], played_timing["name"])
    print_output_for_outcome_with_comment(comment, bowl_outcome)


def print_bowling_details(bowl):
    print(f"{Setting.BOWLER_NAME} bowled {bowl} ball,")


def print_batting_details(wickets_taken, played_shot, played_timing):
    current_batsman = Setting.BATSMEN_NAMES[wickets_taken]
    print(f"{current_batsman} played {played_timing} {played_shot} shot")


def print_super_over_won_output(score, wickets_taken):
    balance_wickets = Setting.MAXIMUM_WICKETS - wickets_taken
    print(score_string(score))
    print(won_string(balance_wickets))


def score_string(result):
    return f"{Setting.COUNTRY_NAME} scored: {result_string(result)}"


def won_string(wickets_count):
    return f"{Setting.COUNTRY_NAME} won by {wicket_string(wickets_count)}"


def print_super_over_lost_output(score):
    lost_by = Setting.TARGET - score
    print(score_string(score))
    print(lost_string(lost_by))


def lost_string(score):
    return f"{Setting.COUNTRY_NAME} lost by {result_string(score)}"
