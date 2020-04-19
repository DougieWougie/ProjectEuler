amicables = set()
# LIMIT is the value tested up to
LIMIT = 10000

def factorize(number):
    factors = []
    for i in range(1, number):
        if number % i == 0:
            factors.append(i)
    return(factors)

def amicable(a):
    # Let d(n) is the sum of proper divisors of n (less than n that
    # divide into n) d(a) = b and d(b)=a if a!=b then a and b are
    # amicable numbers.
    Da = sum(factorize(a))
    Db = sum(factorize(Da))
    if Db == Da:
        return None
    if Db == a:
        if Db > Da:
            return (Da, Db)
        return (Db, Da)

for value in range(1, LIMIT):
    test = amicable(value)
    if test != None:
        amicables.add(test)
print(amicables)
total=0
for amicable in amicables:
    total = total + sum(amicable)
print(total)
