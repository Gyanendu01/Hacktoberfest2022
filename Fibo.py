def fibonacci(n):
    # Initialize the first two terms of the series
    a, b = 0, 1
    # Create an empty list to store the Fibonacci sequence
    fibonacci_sequence = []

    # Check if the input value is valid
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return [a]
    elif n == 2:
        return [a, b]
    else:
        # Add the first two terms to the sequence
        fibonacci_sequence.extend([a, b])
        
        # Generate the Fibonacci sequence
        for _ in range(2, n):
            # Calculate the next term
            next_term = a + b
            # Append it to the sequence
            fibonacci_sequence.append(next_term)
            # Update a and b for the next iteration
            a, b = b, next_term

        return fibonacci_sequence

# Input the number of terms you want in the Fibonacci sequence
n = int(input("Enter the number of Fibonacci terms to generate: "))

# Call the fibonacci function and print the result
result = fibonacci(n)
print(result)
