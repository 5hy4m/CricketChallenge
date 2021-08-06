class InputMock:
    def execute(self, mock_input, data):
        mock_input.return_value = data


class ChallengeSelectionMock:
    def execute(mock_input, data):
        mock_input.return_value = data
