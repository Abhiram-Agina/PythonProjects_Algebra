# -*- coding: utf-8 -*-

firstNum = input("Enter the number you would like the geometric series to start with: \n")
IFirstNum = int(firstNum)

baseNum = input("Enter the base ratio for the geometric series you would like me to print: \n")
IBaseNum = int(baseNum)

amountNum = input("Enter the amount of numbers in the geometric series you would like me to print: \n")
IAmountNum = int(amountNum)


print("Your geometric series : \n")

counter = 1
result = IFirstNum
print(result)

while(counter < IAmountNum):
    result = (result*IBaseNum)
    counter = counter + 1
    print(result)
