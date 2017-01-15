import sys

class UserInputValidator(object):
    def __init__(self):
        self.input = []
        self.termination_str = "q"

    # Force validation criteria to happen in sub-classes
    def get_validated_input(self, user_input):
        raise NotImplementedError

    def get_data(self, input_message="", error_message="{}"):
        try:
            user_input = raw_input(input_message)
            output = self.get_validated_input(user_input.strip())
        except GameTerminated:
            sys.exit()
        except (ValueError, TypeError), e:
            print error_message.format(e)
            return []
        return output

    def validate_num_arguments(self, expected_num_arguments):
        if len(self.input) != expected_num_arguments:
            raise WrongNumberOfArguments(
                "Number of args must equal {}"
                .format(expected_num_arguments))

    def convert_arguments_to_ints(self):
        try:
            for i in range(len(self.input)):
                self.input[i] = int(self.input[i])
        except ValueError:
            raise ValueError("Arguments must be ints")

    def reset_input(self, new_input):
        self.input = new_input

    def is_game_terminated(self):
        if self.input == self.termination_str:
            raise GameTerminated("Game Terminated")

    @staticmethod
    def validate_argument_inclusive_range(argument, min_value, max_value):
        if argument < min_value or argument > max_value:
            raise ValueError(
                "{} is not within the inclusive range: {} to {}"\
                .format(argument, min_value, max_value))


class WrongNumberOfArguments(TypeError):
    """Custom Exception for UserInputValidator"""
    pass


class GameTerminated(IOError):
    """Custom Exception for UserInputValidator"""
    pass
