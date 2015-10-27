#!/usr/bin/env python3
"""Prints diagnostic info to your screen.

This program prints info about your computer version and Python installation

This is called a docstring comment. It uses `\"\"\"` (without the backslashes)
to denote that the information in between the triple " characters is a comment
for other programmers.

"""

from __future__ import print_function
import getpass
import platform
import sys


def os_name():
    """This function returns a prettier name for your operating system."""
    if sys.platform == 'darwin':
        return 'OS X'
    elif sys.platform == 'win32' or sys.platform == 'cygwin':
        return 'Windows'
    elif sys.platform == 'linux':
        return 'Linux'
    else:
        return 'Other'


def main():
    print('Hello ' + getpass.getuser())
    print('You are using Python ' + platform.python_version())
    print('And you are using a computer running ' + os_name())


# If this Python program is run directly, e.g. python print_test.py, then this
#   block of code will get executed.
if __name__ == '__main__':
    main()
