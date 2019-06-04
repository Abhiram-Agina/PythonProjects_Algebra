# solves linear equations using Equal Values method

Yequation1 = input("enter the equation in slope-intercept form, space after each term: \n ")
print(Yequation1)
terms = Yequation1.split(" ")
print(terms)

YvarTerms1 = []

for item in terms:
    if 'x' in item:
        YvarTerms1.append(item)
        
print(YvarTerms1)
lhs1, rhs1 = YvarTerms1[0].split('x')
print(lhs1)

Yequation2 = input("enter the 2nd equation in slope-intercept form, space after each term: \n ")
print(Yequation2)
terms2 = Yequation2.split(" ")
print(terms2)

YvarTerms2 = []

for item in terms2:
    if 'x' in item:
        YvarTerms2.append(item)
        
print(YvarTerms2)
lhs2, rhs2 = YvarTerms2[0].split('x')
print(lhs2)

c1 = int(lhs1)
c2 = int(lhs2)
k1 = int(terms[4])
k2 = int(terms2[4])

print(c1)
print(c2)
print(k1)
print(k2)

result = 0
resultNum = 0

if(c1 ^ c2 < 0):
    result = c1 + (c2 * -1)
    print(result)
else:
    result = c1 + c2

if(k1 ^ k2 < 0):
    resultNum = k2 + (k1 * -1)
    print(resultNum)
else:
    resultNum = k2 + k1


print("Simplified Equation : \n")

print(str(result)+ "x = " + str(resultNum))

print("Final Solution: \n")

x = float(int(resultNum)/int(result))
print("x = "  + str(x))

y1 = int(int(c1*x) +  k1)
y2 = int(int(c2*x) +  k2)

if(y1 == y2):    
    print("y = " + str(y1))
else:
    print("Sorry error during calculation..... Recalculating \n")
    result = result * -1
    resultNum = k2 + k1
    print("")
    print("")
    print("")
    print("")
    print("Simplified Equation : \n")
    
    print(str(result)+ "x = " + str(resultNum))
    
    print("Final Solution: \n")

    x = float(int(resultNum)/int(result))
    print("x = "  + str(x))
    print("y = "  + str(y1))