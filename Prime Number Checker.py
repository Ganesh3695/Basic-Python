# Prime Number Checker in Python

# Get user input for a positive integer
n = int(input("Enter a positive integer: "))

# Check if the input is valid
if n <= 1:
    print("Error: Invalid input. Please enter a positive integer greater than 1.")
else:
    is_prime = True  # Assume the number is prime initially

    # Check for factors from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False  # Set is_prime to False if a factor is found
            break

    # Print the result
    if is_prime:
        print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")
