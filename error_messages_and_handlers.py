CHALLENGE_SELECTION_PARSE_ERROR_MESSAGE = (
    "Please enter the corresponding challenge number."
)
SUPER_OVER_PARSE_ERROR_MESSAGE = (
    "We need two values 'Shot name' and 'Shot timing' seperated by spaces."
)
PREDICT_OUTCOME_PARSE_ERROR_MESSAGE = (
    "We need three values 'Bowl name',"
    " 'Shot name' and 'Shot timing' seperated by spaces."
)
KEY_ERROR_MESSAGE = "is not found in the outcome chart"


def key_error_handler(func):
    def inner_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as err:
            raise KeyError(f"{str(err)} {KEY_ERROR_MESSAGE}")

    return inner_function


def predict_outcome_value_error_handler(func):
    def inner_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as err:
            raise ValueError(PREDICT_OUTCOME_PARSE_ERROR_MESSAGE)

    return inner_function


def super_over_value_error_handler(func):
    def inner_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as err:
            raise ValueError(SUPER_OVER_PARSE_ERROR_MESSAGE)

    return inner_function


def challenge_selection_value_error_handler(func):
    def inner_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as err:
            raise ValueError(CHALLENGE_SELECTION_PARSE_ERROR_MESSAGE)

    return inner_function
