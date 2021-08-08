class PredictOutComeConstants:
    MOCK_INPUT = "Bouncer Pull Perfect"

    PARSED_VALUES = ["BOUNCER", "PULL", "PERFECT"]

    PARSED_VALUES_2 = ["BOUNCER", "PULL", "LATE"]


class SuperOverConstants:
    INPUT_SIDE_EFFECTS = [
        [("Straight", "STRAIGHT"), ("Perfect", "PERFECT")],
        [("Flick", "FLICK"), ("Early", "EARLY")],
        [("Hook", "HOOK"), ("Good", "GOOD")],
        [("LegGlance", "LEGGLANCE"), ("Good", "GOOD")],
        [("LongOff", "LONGOFF"), ("Late", "LATE")],
        [("LongOn", "LONGON"), ("Perfect", "PERFECT")],
    ]
    BOWL_SIDE_EFFECTS = [
        "Inswinger",
        "Doosra",
        "Pace",
        "Inswinger",
        "Pace",
        "Leg Cutter",
    ]

    RESULTS_SIDE_EFFECTS = [4, "wicket", 1, 2, 0, 6]

    COMMENTS_SIDE_EFFECTS = [
        "Excellent drive",
        "Howzat!",
        "Excellent running between the wickets.",
        "Thats sloppy work by the fielder",
        "Terrific fielding",
        "It’s a huge hit.",
    ]

    OUTPUT = """Sudhakar bowled Inswinger ball,Craig played Perfect Straight shotExcellent drive - 4 runsSudhakar bowled Doosra ball,Craig played Early Flick shotHowzat! - 1 wicketSudhakar bowled Pace ball,Paul played Good Hook shotExcellent running between the wickets. - 1 runSudhakar bowled Inswinger ball,Paul played Good LegGlance shotThats sloppy work by the fielder - 2 runsSudhakar bowled Pace ball,Paul played Late LongOff shotTerrific fielding - 0 runSudhakar bowled Leg Cutter ball,Paul played Perfect LongOn shotIt’s a huge hit. - 6 runsAUSTRALIA scored: 13 runsAUSTRALIA won by 1 wicket"""


class SuperOverTwoWicketsConstants:
    INPUT_SIDE_EFFECTS = [
        [("Straight", "STRAIGHT"), ("Perfect", "PERFECT")],
        [("Flick", "FLICK"), ("Early", "EARLY")],
    ]

    BOWL_SIDE_EFFECTS = ["Inswinger", "Doosra"]

    RESULTS_SIDE_EFFECTS = ["wicket", "wicket"]

    COMMENTS_SIDE_EFFECTS = [
        "It’s a wicket.",
        "Edged and taken.",
    ]

    OUTPUT = """Sudhakar bowled Inswinger ball,Craig played Perfect Straight shotIt’s a wicket. - 1 wicketSudhakar bowled Doosra ball,Paul played Early Flick shotEdged and taken. - 1 wicketAUSTRALIA scored: 0 runAUSTRALIA lost by 11 runs"""


class SuperOverThreeBallsVictoryConstants:
    INPUT_SIDE_EFFECTS = [
        [("Straight", "STRAIGHT"), ("Perfect", "PERFECT")],
        [("Flick", "FLICK"), ("Perfect", "PERFECT")],
        [("Hook", "HOOK"), ("Perfect", "PERFECT")],
    ]

    BOWL_SIDE_EFFECTS = [
        "Inswinger",
        "Doosra",
        "Pace",
    ]

    RESULTS_SIDE_EFFECTS = [4, 4, 4]

    COMMENTS_SIDE_EFFECTS = [
        "Excellent drive",
        "It’s a huge hit.",
        "Excellent effort on the boundary.",
    ]

    OUTPUT_SIDE_EFFECTS = """Sudhakar bowled Inswinger ball,Craig played Perfect Straight shotExcellent drive - 4 runsSudhakar bowled Doosra ball,Craig played Perfect Flick shotIt’s a huge hit. - 4 runsSudhakar bowled Pace ball,Craig played Perfect Hook shotExcellent effort on the boundary. - 4 runsAUSTRALIA scored: 12 runsAUSTRALIA won by 2 wickets"""
