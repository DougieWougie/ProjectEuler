from sympy import divisors
SMALLEST = 28
LARGEST  = 28123

def properDivisors(number):
    factors = (divisors(number))
    factors.remove(number)
    return factors

def isPerfect(number):
    sumDivisors = sum(properDivisors(number))
    print("Sum %i" %(sumDivisors))
    if number == sumDivisors:
        return 'perfect'
    else:
        if number < sumDivisors:
            return 'deficient'
        else:
            return 'abundant'
