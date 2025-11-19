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

def tan(x):
    """Return tangent of x (in radians)."""
    return math.tan(x)

def sqrt(x):
    """Return square root of x."""
    return math.sqrt(x)

def power(a, b):
    """Return a raised to the power b."""
    return math.pow(a, b)

def degrees(x):
    """Convert radians to degrees."""
    return math.degrees(x)

def radians(x):
    """Convert degrees to radians."""
    return math.radians(x)

def factorial(n):
    """Return n! (factorial)."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(int(n))

def log10(x):
    """Return base-10 logarithm."""
    return math.log10(x)

def sinh(x):
    """Return hyperbolic sine."""
    return math.sinh(x)

def cosh(x):
    """Return hyperbolic cosine."""
    return math.cosh(x)

def tanh(x):
    """Return hyperbolic tangent."""
    return math.tanh(x)

# ------------------------
# INTERFACE FUNCTION
# ------------------------

def calculator():
    """
    Interface function:
    - Prompts user for input repeatedly
    - Calls the appropriate operation
    - Handles exceptions
    - Exits when user types 'exit'
    """

    print("Welcome to the calculator!")
    print("Available operations: add, subtract, multiply, divide, "
          "sin, cos, tan, log, log10, exp, sqrt, power, degrees, radians, "
          "factorial, sinh, cosh, tanh")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter command (e.g., add 3 5): ").strip()

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        try:
            parts = user_input.split()
            operation = parts[0].lower()

            # -------------------------
            # BINARY OPERATIONS (2 args)
            # -------------------------
            binary_ops = {
                "add": add,
                "subtract": subtract,
                "multiply": multiply,
                "divide": divide,
                "power": power
            }

            if operation in binary_ops:
                if len(parts) != 3:
                    raise ValueError("Binary operations require two numbers.")

                a = float(parts[1])
                b = float(parts[2])

                result = binary_ops[operation](a, b)
                print("Result:", result)
                continue

            # -------------------------
            # UNARY OPERATIONS (1 arg)
            # -------------------------
            unary_ops = {
                "sin": sin,
                "cos": cos,
                "tan": tan,
                "log": log,
                "log10": log10,
                "exp": exp,
                "sqrt": sqrt,
                "degrees": degrees,
                "radians": radians,
                "factorial": factorial,
                "sinh": sinh,
                "cosh": cosh,
                "tanh": tanh
            }

            if operation in unary_ops:
                if len(parts) != 2:
                    raise ValueError("This operation requires exactly one number.")

                x = float(parts[1])
                result = unary_ops[operation](x)
                print("Result:", result)
                continue

            # -------------------------
            # UNKNOWN OPERATION
            # -------------------------
            print("Unknown operation:", operation)

        except Exception as e:
            print("Error:", e)
            print("Please try again.\n")

if __name__ == "__main__":
    calculator()