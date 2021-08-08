class MockChallenges:
    PREDICT_OUTCOME_MOCK_INPUT = "Bouncer Pull Perfect"

    PREDICT_OUTCOME_MOCK_INPUT_PARSED_VALUES = ["BOUNCER", "PULL", "PERFECT"]

    PREDICT_OUTCOME_MOCK_INPUT_PARSED_VALUES_2 = ["BOUNCER", "PULL", "LATE"]

    SUPER_OVER_CHALLENGE_MOCK_INPUT = [
        ["Straight", "Perfect"],
        ["Flick", "Early"],
        ["Hook", "Good"],
        ["LegGGlance", "Good"],
        ["LongOff", "Late"],
        ["LongOn", "Perfect"],
    ]

    MOCK_INPUT_SUPER_OVER_PARSED_VALUES = [
        [("Straight", "STRAIGHT"), ("Perfect", "PERFECT")],
        [("Flick", "FLICK"), ("Early", "EARLY")],
        [("Hook", "HOOK"), ("Good", "GOOD")],
        [("LegGlance", "LEGGLANCE"), ("Good", "GOOD")],
        [("LongOff", "LONGOFF"), ("Late", "LATE")],
        [("LongOn", "LONGON"), ("Perfect", "PERFECT")],
    ]
    SUPER_OVER_BOWL_SIDE_EFFECTS = [
        "Inswinger",
        "Doosra",
        "Pace",
        "Inswinger",
        "Pace",
        "Leg Cutter",
    ]

    SUPER_OVER_RESULTS_SIDE_EFFECTS = [4, "wicket", 1, 2, 0, 6]

    SUPER_OVER_COMMENTS_SIDE_EFFECTS = [
        "Excellent drive",
        "Howzat!",
        "Excellent running between the wickets.",
        "Thats sloppy work by the fielder",
        "Terrific fielding",
        "It’s a huge hit.",
    ]

    SUPER_OVER_SIX_BALLS_OUTPUT = """Sudhakar bowled Inswinger ball,Craig played Perfect Straight shotExcellent drive - 4 runsSudhakar bowled Doosra ball,Craig played Early Flick shotHowzat! - 1 wicketSudhakar bowled Pace ball,Paul played Good Hook shotExcellent running between the wickets. - 1 runSudhakar bowled Inswinger ball,Paul played Good LegGlance shotThats sloppy work by the fielder - 2 runsSudhakar bowled Pace ball,Paul played Late LongOff shotTerrific fielding - 0 runSudhakar bowled Leg Cutter ball,Paul played Perfect LongOn shotIt’s a huge hit. - 6 runsAUSTRALIA scored: 13 runsAUSTRALIA won by 1 wicket"""

    MOCK_INPUT_SUPER_OVER_AFTER_TWO_WICKETS_SIDE_EFFECTS = [
        [("Straight", "STRAIGHT"), ("Perfect", "PERFECT")],
        [("Flick", "FLICK"), ("Early", "EARLY")],
    ]

    SUPER_OVER_AFTER_TWO_WICKETS_BOWL_SIDE_EFFECTS = ["Inswinger", "Doosra"]

    SUPER_OVER_AFTER_TWO_WICKETS_RESULTS_SIDE_EFFECTS = ["wicket", "wicket"]

    SUPER_OVER_AFTER_TWO_WICKETS_COMMENTS_SIDE_EFFECTS = [
        "It’s a wicket.",
        "Edged and taken.",
    ]

    SUPER_OVER_TWO_WICKETS_OUTPUT = """Sudhakar bowled Inswinger ball,Craig played Perfect Straight shotIt’s a wicket. - 1 wicketSudhakar bowled Doosra ball,Paul played Early Flick shotEdged and taken. - 1 wicketAUSTRALIA scored: 0 runAUSTRALIA lost by 11 runs"""

    SUPER_OVER_AFTER_THREE_BALLS_VICTORY_INPUT_SIDE_EFFECTS = [
        [("Straight", "STRAIGHT"), ("Perfect", "PERFECT")],
        [("Flick", "FLICK"), ("Perfect", "PERFECT")],
        [("Hook", "HOOK"), ("Perfect", "PERFECT")],
    ]

    SUPER_OVER_AFTER_THREE_BALLS_VICTORY_BOWL_SIDE_EFFECTS = [
        "Inswinger",
        "Doosra",
        "Pace",
    ]

    SUPER_OVER_AFTER_THREE_BALLS_VICTORY_RESULTS_SIDE_EFFECTS = [4, 4, 4]

    SUPER_OVER_AFTER_THREE_BALLS_VICTORY_COMMENTS_SIDE_EFFECTS = [
        "Excellent drive",
        "It’s a huge hit.",
        "Excellent effort on the boundary.",
    ]

    SUPER_OVER_AFTER_THREE_BALLS_VICTORY_OUTPUT_SIDE_EFFECTS = """Sudhakar bowled Inswinger ball,Craig played Perfect Straight shotExcellent drive - 4 runsSudhakar bowled Doosra ball,Craig played Perfect Flick shotIt’s a huge hit. - 4 runsSudhakar bowled Pace ball,Craig played Perfect Hook shotExcellent effort on the boundary. - 4 runsAUSTRALIA scored: 12 runsAUSTRALIA won by 2 wickets"""

    # SUPER_OVER_CHALLENGE_RESULT = """Sudhakar bowled Bouncer ball,
    # Craig played Perfect Straight shot
    # Excellent line and length - 1 run"""
