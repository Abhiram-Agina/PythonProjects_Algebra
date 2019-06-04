# This program generates random quadratic functions

import random

a = random.randint(1, 10)
b = random.randint(-10, -1)

print('x^2 +',str(a+b) + 'x',(a*b))

x = input("press H for hint: \n")
if x == 'H' or 'h':
    print(a*-1)
    print(b*-1)