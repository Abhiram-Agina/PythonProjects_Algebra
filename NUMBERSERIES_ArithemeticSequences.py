# This program prints the nth term and the sum of n terms in an Arithmetic Series using loops

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
print("The difference of the series = " + str(difference))
      
Wnum = input("enter the terms in the numerical series that you would like to display: \n")
UserNum = int(startNum) + (int(difference) * int(int(Wnum) - 1))
print("Display:  " + str(UserNum))


counter = 1
result = int(UserNum)
sum = 0
print("")
print("The sum of the numbers in the numerical series up until the number of your choosing:")
while(counter < (int(Wnum))):
    sum = sum + (result - (difference * counter))
    counter = counter + 1
sum = sum + result + difference   
print(str(int(sum - difference)))
    