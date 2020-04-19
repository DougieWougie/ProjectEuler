import math

num = math.factorial(100)
string = str(num)
count = 0
for c in string:
    count = count + int(c) 
print(count)
