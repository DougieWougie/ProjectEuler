from sympy import divisors
# --- Incomplete ---

SMALLEST = 12  # 12 is the lowest abundant number
LIMIT = 28123  # All numbers above this can be the sum of two abundant numbers


def proper_divisors(number):
    """
    Takes a number and returns a list of it's proper factors.

    :param      number:int
    :return:    factors:list
    """
    factors = (divisors(number))
    factors.remove(number)
    return factors


def perfect_number(number):
    """
    Checks if a number is perfect by summing it's proper divisors and compares with the number, less is deficient
    greater is abundant.

    :param     number:int
    :return    perfect|deficient|abundant:str
    """
    sum_divisors = sum(proper_divisors(number))
    if number == sum_divisors:
        return 'perfect'
    else:
        if number < sum_divisors:
            return 'abundant'
        else:
            return 'deficient'


def is_abundant(check_number):
    """
    Checks if a number is perfect by summing it's proper divisors and compares with the number, less is deficient
    greater is abundant.

    :param     check_number:int
    :return    perfect|deficient|abundant:str
    """
    if number < sum(proper_divisors(check_number)):
        return True
    else:
        return False


# Get a list of abundant numbers
abundant_numbers = list()

for number in range(SMALLEST, LIMIT):
    if abundant := perfect_number(number) == 'abundant':
        # print(f'{number} is an abundant number with proper divisors {proper_divisors(number)}.')
        abundant_numbers.append(number)

print(abundant_numbers)

"""
What do we want?

Sum of positive integers that cannot be expressed as the sum of two abundant numbers
12 is the smallest abundant number, therefore 11! must be part of the total sum
all integers > 28123 can be written as the sum of two abundant, giving a limit.

What have we got?
A list of all abundant numbers.
"""
answer = list()

for abundant in abundant_numbers:
    for next_index in range(12, 28133):
        if abundant + next_index < LIMIT:
            answer.append(abundant)
        else:
            break
    print(sum(answer))

print(f'Sum is {sum(answer)}')
