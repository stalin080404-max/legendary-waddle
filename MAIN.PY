# Main.py

"""This module for blablabla"""

import double_it    # first way to import
import sys

# from double_it import double_it

X_INIT: int = 1

def prod_integers(old_inventory: int, new_inventory: int) -> int:
    """_summary_
    :param num1: _description_
    :type num1: dict[str, int]
    :param num2: _description_
    :type num2: list[int]
    :return: _description_
    :rtype: int
    """

    y = old_inventory + new_inventory + X_INIT

    result = double_it.double_int(y)

    return result


if __name__ == "__main__":
    
    print(sys.argv)
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    
    print(print(prod_integers(num1, num2)))
