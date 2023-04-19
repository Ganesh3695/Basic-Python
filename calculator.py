# Basic Calculator in Python

# Get user input for two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform addition
sum = num1 + num2
print("Sum: ", sum)

# Perform subtraction
difference = num1 - num2
print("Difference: ", difference)

# Perform multiplication
product = num1 * num2
print("Product: ", product)

# Perform division
if num2 == 0:
    print("Error: Cannot divide by zero!")
else:
    quotient = num1 / num2
    print("Quotient: ", quotient)
