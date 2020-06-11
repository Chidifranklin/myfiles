while True:
    print("Options:")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to end the program")
    user_input = input(":")
    
    

if user_input == "quit":
    break
else:
    if user_input == "add":
            num1 = float(input("Enter first number"))
            num2 = float(input("Enter second number"))
            result = str(num1 + num2)
            print("The answer is " + result)
            
            else:
                if user_input == "subtract":
                    num1 = float(input("Enter first number"))
                    num2 = float(input("Enter second number"))
                    result = str(num1 - num2)
                    print("The answer is " + result)
                    else:
                        if user_input == "multiply":
                            num1 = float(input("Enter first number"))
                            num2 = float(input("Enter second number"))
                            result = str(num1 * num2)
                            print("The answer is " + result)
                            else:
                                if user_input == "divide":
                                    num1 = float(input("Enter first number"))
                                    num2 = float(input("Enter second number"))
                                    result = str(num1 / num2)
                                    print("The answer is " + result)
                                    else:
                                        print("Uknown input")
    
        
        
   /this program is not working yet