#Python program to print a star pattern specified on the number of rows specified by the user
#Get the number of rows from the user
n = int(input("Enter the number of rows: "))
#Outer loop for each row
for i in range(1, n+1):
    #Inner loop for each column in the row
    for j in range(i):
        #Print star, end space without moving to the next line
        print("*", end=' ')
        #After each row, print a new line
    print()
        
   