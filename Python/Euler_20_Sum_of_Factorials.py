from sys import argv
from math import factorial


def sum_factorial(number: int) -> int:
    count = 0

    """
    math.factorial returns an integer which isn't iterable so convert to a string which is.
    """

    for _ in str(factorial(number)):
        count += int(_)

    return count


def main():
    """
    Throw a ValueError if the argument count isn't 2.
    """
    try:
        if len(argv) != 2:
            raise ValueError
        else:
            print(f'Solution for {int(argv[1])} is {sum_factorial(int(argv[1]))}.')
    except ValueError:
        print('Need one argument - a factorial to calculate!')


if __name__ == '__main__':
    main()
