def print_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:  # To avoid adding the square root twice
                divisors.append(n // i)
    
    # Sorting divisors to print in ascending order
    divisors.sort()
    return divisors

# Example usage
number = 36
print(f"Divisors of {number} are: {print_divisors(number)}")
