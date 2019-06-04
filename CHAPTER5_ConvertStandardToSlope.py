# Converts equation from standard to slope intercept form

Yequation1 = input("enter the equation in Standard Form, space after each term ( 3x + 4y + 7 = 0 ):\n ")
print(Yequation1)
terms = Yequation1.split(" ")
print(terms)

XvarTerms = []

for item in terms:
    if 'x' in item:
        XvarTerms.append(item)
        
print(XvarTerms)
lhs1, rhs1 = XvarTerms[0].split('x')
print(lhs1)
x = int(int(lhs1) * -1)

for item in terms:
    if 'x' in item:
        XvarTerms.append(item)
        
print(XvarTerms)
lhs1, rhs1 = XvarTerms[0].split('x')
print(lhs1)

YvarTerms = []

for item in terms:
    if 'y' in item:
        YvarTerms.append(item)
        
print(YvarTerms)
lhs2, rhs2 = YvarTerms[0].split('y')
print(lhs2)

k1 = int(int(terms[4]) * -1)

Yequation2 = (str(lhs2)+"y = " + str(x)+"x + " + str(k1))



print("Simplified Completely: \n ")
Yequation2 = ("y = " + str((float(x)/float(lhs2))) + "x + " + str(float(float(k1)/float(lhs2))))

print()
print()
print("Slope-Intercept Form:")
print(Yequation2)

print()
print("Slope: " + str((float(x)/float(lhs2))))
print("Y-Intercept: " + str(float(float(k1)/float(lhs2))))