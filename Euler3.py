def largest_prime_factor(number):
    # Start with the smallest prime factor (2)
    prime_factor = 2
    
    # Iterate while the number is greater than 1
    while number > 1:
        # Check if the current prime factor divides the number
        if number % prime_factor == 0:
            # Divide the number by the prime factor
            number //= prime_factor
        else:
            # If the current prime factor does not divide the number, increment to the next prime
            prime_factor += 1
    
    return prime_factor

# Example usage
number_to_factorize = 600851475143
result = largest_prime_factor(number_to_factorize)

print("Largest prime factor of", number_to_factorize, "is:", result)
