# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

import sys


def cli_quit():
    """ Request user input before quitting command line """
    input("Press Any Key to Quit...")


def cli_arguments() -> list[str]:
    """ Return system command line arguments"""
    return sys.argv[1:]


def cli_has_argument(arg):
    """ Return true if argument exists """
    if arg in cli_arguments():
        return True
    else:
        return False


def cli_get_value_for_argument(param):
    """ Return value for an argument """
    args = cli_arguments()
    for arg in args:
        if "=" not in arg:
            return arg
        if param in arg:
            value = arg.split("=")
            if value[1].lower() == "true":
                return True
            if value[1].lower() == "false":
                return False
            return value[1]
    return None
