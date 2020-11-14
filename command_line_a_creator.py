
from current_cmd_a import CurrentCMD_A
from cmd_creator import CommandLineCreator


class CommandLineACreator(CommandLineCreator):
    def __init__(self):
        self.runner_message = "Running Azez's cmd"

    def create_cmd(self):
        return CurrentCMD_A(self.runner_message)
