from app.operations import addition, subtraction, multiplication, division

def calculator():
    print("Welcome to the calculator REPL!")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = input("Enter an operation, example: add,subtract,multiply,divide followed by numbers (e.g., add 2 3): ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        try:
            operation, num1, num2 = user_input.split()
            num1, num2 = float(num1), float(num2)
        except ValueError:
            print("Invalid input format. Please try again.")
            continue
            
        if operation == 'add':
            result = addition(num1, num2)
        elif operation == 'subtract':
            result = subtraction(num1, num2)
        elif operation == 'multiply':
            result = multiplication(num1, num2)
        elif operation == 'divide':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = division(num1, num2)
        else:
            print("Unknown operation. Please try again.")
            continue
            
        print(f"Result: {result}")