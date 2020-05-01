from math import factorial

def sum_factorial(number: int) -> int:
    count = 0

    """
    math.factorial returns an integer which isn't iterable so convert to a string which is.
    """

    for _ in str(factorial(number)):
        count += int(_)

    return count

factor_to_sum = 100
# print(sum_factorial(factor_to_sum))
print(f'Solution for {factor_to_sum} is {sum_factorial(factor_to_sum)}.')
