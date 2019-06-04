# Solving Quadratic Equations using the 'Never Fail' quadratic formula
# -b +- (b^2 - 4*a*c)^(1/2) /2*a
# quadratic has no real number solutions if the discriminant is negative

import math #to perform square and square root operations

equation = input("enter the equation, space after each term(except near =; e.g. 3x^2 + 7x + 3= 0: ")
print(equation)
terms = equation.split(" ")
print(terms)

x2Terms = []

for item in terms:
    if 'x^2' in item:
        x2Terms.append(item)
        
print(x2Terms)

X2_lhs, X2_rhs = x2Terms[0].split('x^2')

xTerms = []

for item in terms:
    if 'x' in item:
        xTerms.append(item)
        
print(xTerms)

X_lhs, X_rhs = xTerms[1].split('x')

CTerms = []

for item in terms:
    if '=' in item:
        CTerms.append(item)
        
print(CTerms)

C_lhs, C_rhs = CTerms[0].split('=')

print("a is", X2_lhs)
A = int(X2_lhs)
print("b is", X_lhs)
B = int(X_lhs)
print("c is", C_lhs)
C = int(C_lhs)

resultA = float((-1*(B) + math.sqrt((B*B) - 4*(A*C)))/(2*A))
resultB = float((-1*(B) - math.sqrt((B*B) - 4*(A*C)))/(2*A))

print("Your answers are " , resultA , "and " , resultB) 