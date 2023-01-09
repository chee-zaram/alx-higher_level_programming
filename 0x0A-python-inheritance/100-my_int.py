#!/usr/bin/python3
"""Module ``100-my_int``"""


class MyInt(int):
    """Inverts '==' and '!='"""

    def __eq__(self, x):
        """Makes equal not equal"""
        return super().__ne__(x)

    def __ne__(self, x):
        """Makes not equal equal"""
        return super().__eq__(x)
