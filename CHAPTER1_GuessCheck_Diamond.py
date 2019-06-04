# Find factors of 2 quadratic functions using Guess and Check Method
# this mimics how humans solve the quadratic function using Guess and Check Diamond

Sum = int(input("Enter the value of x + y: \n "))
Product = int(input("Enter the value of x * y: \n "))

# The goal is to find factors of the Product
# And then check if they add up to the Sum
    
counter = 1
F1 = 0
F2 = 0

while(counter < int(Product/2)):# Checking for factors until half the size of the Product
    if(Product % counter == 0):# Checking using modulus function to see if counter is a factor of Product
        F1 = int(counter) #counter is the first factor
        F2 = int(Product/counter) # quotient is the second factor
        if((F1 + F2) == Sum ): #checking if sum of factors matches the sum given
            print("x and y are : " + str(F1) + "," + str(F2))
            break
        elif(((F1*-1) + F2) == Sum):
            print("x and y are : " + str(int(F1*-1)) + "," + str(F2))
            break
        elif(((F1) + (F2 * -1)) == Sum):
            print("x and y are : " + str(int(F1*-1)) + "," + str(int(F2*-1)))
            break
        elif(((F1*-1) + ( F2* -1)) == Sum):
            print("x and y are : " + str(int(F1*-1)) + "," + str(int(F2*-1)))
            break
    counter = counter + 1
    F1 = 0
    F2 = 0