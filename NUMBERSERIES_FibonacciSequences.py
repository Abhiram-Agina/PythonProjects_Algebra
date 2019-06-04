# -*- coding: utf-8 -*-
# Working

amountNum = input("Enter the amount of numbers in the fibonacci series you would like me to print( Starts at 2nd - 1) : \n")
IAmountNum = int(amountNum)

print("Your fibonacci series : \n")

counter = 1
x = 0
y = 1
z = x + y
print(x)
print(y)
print(z)

while((counter+3) <= IAmountNum):
    x = z
    z = z + y
    y = x
    print(z)
    counter = counter + 1