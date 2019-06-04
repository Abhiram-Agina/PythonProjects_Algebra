# finds slope when line is written in slope-intercept form :)
# works with whole numbers

def FindIntercept(YI,x):
    YI = EquationInput
    print("I will now find the slope of the equation")
    while(YI[YI.find('x')-x] != " "):
        print(YI[YI.find('x')-x])
        x = x + 1
    while(YI[YI.find('x')-x] != " "):
         x = x - 1
EquationInput = input("Type in an equation in Slope intercept for with the use of x,y,y-int, and constant. : \n")
EquationInput = str(EquationInput)
x = 1
FindIntercept(EquationInput,x)