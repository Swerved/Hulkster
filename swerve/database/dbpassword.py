"""
Database Passwords

Requires PWPPY.dll for PWP Databases

"""

from swerve.core import commandline


def pwp():
    return commandline.cli_get_value_for_argument("pwp")
