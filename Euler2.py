# Initialize variables
fibonacci_sequence = [1, 2]
limit = 4000000
sum_even_terms = 0

# Generate Fibonacci sequence
while fibonacci_sequence[-1] + fibonacci_sequence[-2] <= limit:
    next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_term)

# Sum the even-valued terms
for term in fibonacci_sequence:
    if term % 2 == 0:
        sum_even_terms += term

# Print the result
print("Sum of even-valued terms in the Fibonacci sequence below 4 million:", sum_even_terms)