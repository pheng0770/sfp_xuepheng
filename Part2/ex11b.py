# Create a function called calculate that takes three arguments
def calculate(number1, operator, number2):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
        return number1 / number2
    else:
        return "Invalid operator"

# Test the function with different operations
print(calculate(10, "+", 10))  # Output: 20
print(calculate(10, "-", 10))  # Output: 0
print(calculate(10, "*", 10))  # Output: 100
print(calculate(10, "/", 10))  # Output: 1.0
