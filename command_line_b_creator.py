
from current_cmd_b import CurrentCMD_B
from cmd_creator import CommandLineCreator


class CommandLineBCreator(CommandLineCreator):
    def create_cmd(self):
        return CurrentCMD_B()
