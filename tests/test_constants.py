class MockChallenges:
    PREDICT_OUTCOME_MOCK_INPUT = "Bouncer Pull Perfect"
    PREDICT_OUTCOME_MOCK_INPUT_PARSED_VALUES = ["BOUNCER", "PULL", "PERFECT"]
    PREDICT_OUTCOME_MOCK_INPUT_PARSED_VALUES_2 = ["BOUNCER", "PULL", "LATE"]
    SUPER_OVER_CHALLENGE_MOCK_INPUT = [
        ["Straight", "Perfect"],
        ["Flick", "Early"],
        ["Hook", "Good"],
        ["LegGlance", "Good"],
        ["LongOff", "Late"],
        ["LongOn", "Perfect"],
    ]
    SUPER_OVER_CHALLENGE_MOCK_INPUT_PARSED_VALUES = [
        ["STRAIGHT", "PERFECT"],
        ["FLICK", "EARLY"],
        ["HOOK", "GOOD"],
        ["LEGLANCE", "GOOD"],
        ["LONGOFF", "LATE"],
        ["LONGON", "PERFECT"],
    ]
    SUPER_OVER_CHALLENGE_RESULT = """Sudhakar bowled Bouncer ball, 
    Craig played Perfect Straight shot
    Excellent line and length - 1 run"""


class Result:
    pass
