#!/usr/bin/python3
"""writing a class"""


class MyInt(int):
    def __eq__(self, other):
        # Override the == operator
        return super().__ne__(other)

    def __ne__(self, other):
        # Override the != operator
        return super().__eq__(other)
