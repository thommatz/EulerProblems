# Initialize the sum variable
sum_multiples = 0

# Iterate through numbers below 1000
for num in range(1000):
    # Check if the number is a multiple of 3 or 5
    if num % 3 == 0 or num % 5 == 0:
        # Add the multiple to the sum
        sum_multiples += num

print("Sum of multiples of 3 or 5 below 1000:", sum_multiples)