class PredictOutComeConstants:
    MOCK_INPUT = "Bouncer Pull Perfect"
    PARSED_VALUES = [
        {"name": "Bouncer", "key": "BOUNCER"},
        {"name": "Pull", "key": "PULL"},
        {"name": "Perfect", "key": "PERFECT"},
    ]
    PARSED_VALUES_2 = [
        {"name": "Bouncer", "key": "BOUNCER"},
        {"name": "Pull", "key": "PULL"},
        {"name": "Late", "key": "LATE"},
    ]
    ERROR_INPUT1 = "AWD AWD AWD AWD"
    ERROR_INPUT2 = "AWD AWD"
    ERROR_INPUT3 = [
        {"name": "awd", "key": "AWD"},
        {"name": "awd", "key": "AWD"},
        {"name": "awd", "key": "AWD"},
    ]


class SuperOverConstants:
    MOCK_INPUT = "Straight Perfect"
    INPUT_SIDE_EFFECTS = [
        [
            {"name": "Straight", "key": "STRAIGHT"},
            {"name": "Perfect", "key": "PERFECT"},
        ],
        [{"name": "Flick", "key": "FLICK"}, {"name": "Early", "key": "EARLY"}],
        [{"name": "Hook", "key": "HOOK"}, {"name": "Good", "key": "GOOD"}],
        [{"name": "LegGlance", "key": "LEGGLANCE"}, {"name": "Good", "key": "GOOD"}],
        [{"name": "LongOff", "key": "LONGOFF"}, {"name": "Late", "key": "LATE"}],
        [{"name": "LongOn", "key": "LONGON"}, {"name": "Perfect", "key": "PERFECT"}],
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
    OUTPUT = (
        "Sudhakar bowled Inswinger ball,"
        "Craig played Perfect Straight shot"
        "Excellent drive - 4 runs"
        "Sudhakar bowled Doosra ball,"
        "Craig played Early Flick shot"
        "Howzat! - 1 wicket"
        "Sudhakar bowled Pace ball,"
        "Paul played Good Hook shot"
        "Excellent running between the wickets. - 1 run"
        "Sudhakar bowled Inswinger ball,"
        "Paul played Good LegGlance shot"
        "Thats sloppy work by the fielder - 2 runs"
        "Sudhakar bowled Pace ball,"
        "Paul played Late LongOff shot"
        "Terrific fielding - 0 run"
        "Sudhakar bowled Leg Cutter ball,"
        "Paul played Perfect LongOn shot"
        "It’s a huge hit. - 6 runs"
        "AUSTRALIA scored: 13 runs"
        "AUSTRALIA won by 1 wicket"
    )
    ERROR_INPUT1 = "I'm an error text"
    ERROR_INPUT2 = "   "


class SuperOverTwoWicketsConstants:
    INPUT_SIDE_EFFECTS = [
        [
            {"name": "Straight", "key": "STRAIGHT"},
            {"name": "Perfect", "key": "PERFECT"},
        ],
        [{"name": "Flick", "key": "FLICK"}, {"name": "Early", "key": "EARLY"}],
    ]

    BOWL_SIDE_EFFECTS = ["Inswinger", "Doosra"]

    RESULTS_SIDE_EFFECTS = ["wicket", "wicket"]

    COMMENTS_SIDE_EFFECTS = [
        "It’s a wicket.",
        "Edged and taken.",
    ]

    OUTPUT = (
        "Sudhakar bowled Inswinger ball,"
        "Craig played Perfect Straight shot"
        "It’s a wicket. - 1 wicket"
        "Sudhakar bowled Doosra ball,"
        "Paul played Early Flick shot"
        "Edged and taken. - 1 wicket"
        "AUSTRALIA scored: 0 run"
        "AUSTRALIA lost by 11 runs"
    )


class SuperOverThreeBallsVictoryConstants:
    INPUT_SIDE_EFFECTS = [
        [
            {"name": "Straight", "key": "STRAIGHT"},
            {"name": "Perfect", "key": "PERFECT"},
        ],
        [{"name": "Flick", "key": "FLICK"}, {"name": "Perfect", "key": "PERFECT"}],
        [{"name": "Hook", "key": "HOOK"}, {"name": "Perfect", "key": "PERFECT"}],
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

    OUTPUT_SIDE_EFFECTS = (
        "Sudhakar bowled Inswinger ball,"
        "Craig played Perfect Straight shot"
        "Excellent drive - 4 runs"
        "Sudhakar bowled Doosra ball,"
        "Craig played Perfect Flick shot"
        "It’s a huge hit. - 4 runs"
        "Sudhakar bowled Pace ball,"
        "Craig played Perfect Hook shot"
        "Excellent effort on the boundary. - 4 runs"
        "AUSTRALIA scored: 12 runs"
        "AUSTRALIA won by 2 wickets"
    )
