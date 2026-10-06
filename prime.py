# Python program to check if a number is prime
#Take the input from the user
num = int(input("Enter a number:"))
#Check if the number is greater than 1(Since prime numbers are greater than 1)
if num > 1:
    #Loop only up to the square root of num for efficiency
    for i in range(2 , int (num**0.5) + 1):
        #If num is is divisible by any number, it is not prime
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
        else:
            #If no divisors are found, then the number is prime
            print(f"{num} is a prime number")
    else:
        #Numbers less than 2 are not prime
        print(f"{num} is not a prime number")