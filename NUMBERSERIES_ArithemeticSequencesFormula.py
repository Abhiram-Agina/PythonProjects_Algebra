# This program prints the nth term and the sum of n terms in an Arithmetic Series using formula

print("This program prints the nth term and the sum of n terms in an Arithmetic Series")
series = input("enter the numerical series, with each term seperated by a space: \n")
series = series.split(" ")
print(series)

startNum = int(series[0])

if((int(series[1]) - int(series[0])) == (int(series[2]) - int(series[1]))):    
    difference = (int(series[1]) - int(series[0]))
else:
    print(" this is not a valid numerical series ")

print("The first # in this seies = " + str(startNum))
print("The common difference of the series = " + str(difference))
      
n = int(input("enter the terms in the numerical series that you would like to display: \n"))
nthTerm = int(startNum) + (int(difference) * int(int(n) - 1)) #formula for nth term
print("Nth Term:  " + str(nthTerm))


counter = 1
result = int(nthTerm)
sum = int((n/2)*((2*startNum) + ((difference)*(n-1)))) #formula for sum of n terms
print("")
print("The sum of the numbers in the numerical series up until the number of your choosing: \n")
print(sum)
