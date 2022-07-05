#!/usr/bin/python3


def read_file(filename=""):
    """The read file function"""

    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
