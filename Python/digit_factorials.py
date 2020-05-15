"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits. (Note: as 1! = 1 and
2! = 2 are not sums they are not included).

Insights: This would need to be limited to single digit factorials, the highest being 9!.
trial and error shows that 9!7 and 9!8 are both 7 digits long, giving up upper bound of
7!9.
"""

from math import factorial

BTM_LIMIT = 3  # 1 and 2 are not sums so ignored
TOP_LIMIT = factorial(9) * 7  # 9!7 and 9!8 are both 7 digits, so 9!7 is upper limit

curious_numbers = []  # This isn't the term for these but it fits well!


def brute_force():
    """
    Brute force perfect number finder.
    :return: list:int
    """
    for _ in range(BTM_LIMIT, TOP_LIMIT + 1):
        total_factorials = 0
        for digit in [char for char in str(_)]:
            total_factorials += factorial(int(digit))
        if total_factorials == _:
            curious_numbers.append(int(_))
    return curious_numbers


if __name__ == '__main__':
    print(sum(brute_force()))
