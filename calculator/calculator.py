while True:
    
    #Asking for input
    operation = input("Choose the operation you want to perform: \n 1. Addition (+) \n 2. Subtraction (-) \n 3. Multiplication (*) \n 4. Division (/) \n")
    
    if operation in [1,2,3,4]:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))

        #Conditions
        if(operation == 1):
            print("The sum of two numbers is ", num1 + num2)
        elif(operation == 2):
            print("The difference between two numbers is ", num1 - num2)
        elif(operation == 3):
            print("The product of two numbers is ", num1 * num2)
        elif(operation == 4):
            if(num2 != 0):
                print("The division of two numbers is ", num1 / num2)
            else:
                print("Cannot divide by Zero")
    else:
        print("Invalid Input")

    #If user wants another calculation
    choice = input("Do you want another calculation? ").lower()

    if choice !="yes":
        print("Thanks for using calculator")
        break





