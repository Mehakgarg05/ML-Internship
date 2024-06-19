# Write a python program that generates the first n numbers in the 
# Fibonacci sequence.

n = int(input("Enter n:"))
def generate_fibonacci(n):
    if n <= 0:
        return []

    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence[:n]

fibonacci_sequence = generate_fibonacci(n)

# Print the Fibonacci sequence
print(fibonacci_sequence)
