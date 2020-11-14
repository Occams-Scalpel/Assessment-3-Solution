
from current_cmd_b import CurrentCMD_B
from cmd_creator import CommandLineCreator


class CommandLineBCreator(CommandLineCreator):
    def __init__(self):
        self.runner_message = "Running Ethan's cmd"

    def create_cmd(self):
        return CurrentCMD_B(self.runner_message)
