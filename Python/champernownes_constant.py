"""
---Incomplete---
Champernowne's constant C_10 is a transcendental real constant, constructed
by concatenating succsessive integer representations:

C_10 = 0.1234567891011121314151617181920

The 12th digit of the fractional part is 1 - if d_n is the nth fractional part
find d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000.

{123456789}{111213141516171819...}{101,102,103,...999}
 |          |                      |
 |          |                      900 triple digit strings
 |          90 double digit strings
 9 single digit strings

d1 = 1 d10 = 11
"""

total = 0
a = 35
b = '1178 1222 124 71 346 1034 396 1128 123 750 754 1119 697 734 959 544 767 448 319 63 110 279 795 106 156 1101 666 61 439 824 371 317 745 486 379'
b = b.split()
for i in range(0, len(b)):
    b[i] = int(b[i])

for _ in b:
    total += _ * a
print(total)
