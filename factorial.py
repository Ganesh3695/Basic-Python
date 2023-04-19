# Factorial Calculator in Python

# Get user input for a positive integer
n = int(input("Enter a positive integer: "))

# Initialize the factorial value to 1
factorial = 1

# Check if the input is valid
if n < 0:
    print("Error: Invalid input. Please enter a positive integer.")
elif n == 0:
    print("Factorial of 0 is 1.")
else:
    # Calculate the factorial using a loop
    for i in range(1, n + 1):
        factorial *= i

    # Print the factorial
    print("Factorial of", n, "is", factorial)
