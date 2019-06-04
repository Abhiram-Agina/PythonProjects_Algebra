# This solves single variable equation by isolating the variable
# mimics human way of simplifying and solving equations

EquateInput = (input("Enter a single variable equation for me to solve, spaces between each term (3x + 1 = 7) : \n "))
terms = EquateInput.split(" ")
AllTerms = []

for item in terms:
    if 'x' in item:
        AllTerms.append(item)
        
print(AllTerms)
lhs1, rhs1 = AllTerms[0].split('x')
lhs1 = int(lhs1)
print(lhs1)
terms[4] = int(terms[4])
terms[2] = int(terms[2])

ERHS = int(int(terms[4]) + int(terms[2] * -1))
print("\nSimplified Equation:")
print(" " + str(lhs1) + "x = " + str(ERHS))   

print("\nFinal Solution: ")
finalTerm = float(ERHS/lhs1)
print(" x = " + str(finalTerm))