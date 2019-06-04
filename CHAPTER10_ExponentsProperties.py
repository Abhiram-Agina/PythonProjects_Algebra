# Type in an Expression that includes exponents and I will give you an Answer
# Negative Exponents: Work in progress

SEEquations = input(" Type in a simple expression using exponents, 1 operator, and the same constant (i.e. 3^2 * 3^6) \n ")
terms2 = SEEquations.split(" ")
ExponentTerms = []

for item in terms2:
    if '^' in item:
        ExponentTerms.append(item)
        
print(ExponentTerms)
lhs1, rhs1 = ExponentTerms[0].split('^')
lhs2, rhs2 = ExponentTerms[1].split('^')
ExpoNum = int(int(rhs1) + int(rhs2))
counter = 1
sumNum = (int(lhs1) * int(lhs1))
print(" your answer is: ... \n")
if('*' in str(SEEquations)):
    print(str(lhs1) + "^" + str(ExpoNum))
    while(counter < ExpoNum-1):
        sumNum = sumNum * int(lhs1)
        counter = counter + 1
    print("= " + str(sumNum))
        
if('/' in str(SEEquations)):
    print(str(lhs1) + "^" + str(int(int(rhs1) - int(rhs2))))
    while((counter < int(int(rhs1) - int(rhs2)))-1):
        sumNum = sumNum * int(lhs1)
        counter = counter + 1
    print("= " + str(sumNum))
Ans1 = 0
Ans2 = 0
if('+' in str(SEEquations)):
    while(counter < int(rhs1)-1):
        sumNum = sumNum * int(lhs1)
        counter = counter + 1
    Ans1 = sumNum
    sumNum = (int(lhs1) * int(lhs1))
    counter = 1
    while(counter < int(rhs2)-1):
        sumNum = sumNum * int(lhs1)
        counter = counter + 1
    Ans2 = sumNum
    print("= " + str(int(Ans1 + Ans2)))
if('-' in str(SEEquations)):
    while(counter < int(rhs1)-1):
        sumNum = sumNum * int(lhs1)
        counter = counter + 1
    Ans1 = sumNum
    sumNum = (int(lhs1) * int(lhs1))
    counter = 1
    while(counter < int(rhs2)-1):
        sumNum = sumNum * int(lhs1)
        counter = counter + 1
    Ans2 = sumNum
    print("= " + str(int(Ans1 - Ans2)))