###
## simple_package - Module operations.py
## Basic online calculator
###

## Here I have defined four functions for the four
## basic operations. 
##
## 1) You should provide an interface function
##    that will prompt the user for input and
##    call the appropriate function based on the
##    user's input. The interface function should
##    continue to prompt the user for input until
##    the user enters'exit'. 
##
## 2) The interface function should also handle
##    any exceptions that might be thrown by the
##    basic operations functions. If an exception 
##    is thrown,the interface function should print 
##    an error message and continue to prompt the 
##    user for input.
##
## 3) Add other "operations" to the calculator, that
##    involve complicated operations (e.g., 
##    trigonometric functions, logarithms, etc.).
##

import math

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract one number from another."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide one number by another."""
    return a / b


# ------------------------
# EXTRA OPERATIONS
# ------------------------

def sin(x):
    """Return sine of x (in radians)."""
    return math.sin(x)

def cos(x):
    """Return cosine of x (in radians)."""
    return math.cos(x)

def log(x):
    """Return natural logarithm of x."""
    return math.log(x)

def exp(x):
    """Return e raised to the power x."""
    return math.exp(x)

# ------------------------
# INTERFACE FUNCTION
# ------------------------

def interface():
    """
    Interface function:
    - Prompts user for input repeatedly
    - Calls the appropriate operation
    - Handles exceptions
    - Exits when user types 'exit'
    """
    
    print("Welcome to the calculator!")
    print("Available operations: add, subtract, multiply, divide, sin, cos, log, exp")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter command (e.g, add 3 5): ").strip()

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        try:
            # Split input into parts
            parts = user_input.split()
            operation = parts[0].lower()

            # -------------------------
            # BINARY OPERATIONS (2 args)
            # -------------------------
            if operation in ("add", "subtract", "multiply", "divide"):
                if len(parts) != 3:
                    raise ValueError("Binary operations require two numbers.")

                a = float(parts[1])
                b = float(parts[2])

                if operation == "add":
                    result = add(a, b)
                elif operation == "subtract":
                    result = subtract(a, b)
                elif operation == "multiply":
                    result = multiply(a, b)
                elif operation == "divide":
                    result = divide(a, b)

                print("Result:", result)

            # -------------------------
            # UNARY OPERATIONS (1 arg)
            # -------------------------
            elif operation in ("sin", "cos", "log", "exp"):
                if len(parts) != 2:
                    raise ValueError("This operation requires exactly one number.")

                x = float(parts[1])

                if operation == "sin":
                    result = sin(x)
                elif operation == "cos":
                    result = cos(x)
                elif operation == "log":
                    result = log(x)
                elif operation == "exp":
                    result = exp(x)

                print("Result:", result)

            else:
                print("Unknown operation:", operation)

        # Catch *any* error and continue loop
        except Exception as e:
            print("Error:", e)
            print("Please try again.\n")

