# Simple menu driven Calculator using functions
# Description ->
""" The program performs Basic Arithmatic Operation like
    Adddition, Substraction,  Multiplication and Division """
# it is a menu driven and keeps running until user exist.

# Function for Addition
def add(a,b):
    return a+b

# Function for Substraction
def substract(a,b):
    return a-b

#Function for multiplication

def multiply(a,b):
    return a*b

#Function for Division
def divide(a,b):
    if b == 0 :
        return "Error! Division by zero"   #Handling divide by zero error
    else:
        return a/b
    
#Main Calculator Function
def calculator():
    while True:        #Infite loop until user chooses Exit
        #Displaying Menu oPtion
        print("---Simple Calculator---")
        print("1.Addition")
        print("2.Substraction")
        print("3.MUltiplication")
        print("4.Division")
        print("5.Exit")

        # Taking user choice
        choice = int(input("ENter your choice (1-5): "))

        #Exit condition
        if choice == 5:
            print("Exiting calculator...bye bye!")
            break
        #taking input number from user
        num1 = float(input("enter 1st number: "))
        num2 = float(input("enter 2nd number: "))
        #performing operation based on choice
        if choice == 1:
            print("Result",add(num1,num2))
        elif choice == 2:
            print("Result",substract(num1,num2))
        elif choice == 3:
            print("Result",multiply(num1,num2))
        elif choice == 4:
            print("Result",divide(num1,num2))
        else:
            print("Invalid choice!please enter between (1-5).")

#calling the calculator function
calculator()
