# Objective: print number of levels of stages for Pascal's Triangle
#  Pascal's triangle is a triangular array of the binomial coefficients: (a+b)^n
# an algebraic expression of the sum or the difference of two terms: a+b

n = int(input("How many levels would you like me to print: \n"))

Ax = [1]
Ay = [1,1]

if(n == 0): # Hardcoded
    print(Ax)
if(n == 1): # Hardcoded
    print(Ax)
    print(Ay)
if(n > 1):
    print(Ax)
    print(Ay)
    PyraLevel = 2
    while PyraLevel <= n:
        Ax = list(Ay)
        Ay[0] = 1
        i = 1
        while i < PyraLevel:
            Ay[i] = Ax[i-1] + Ax[i] # Compares to Ax when adding values
            i = i + 1
        Ay.append(1)
        print(Ay)
        PyraLevel = PyraLevel + 1