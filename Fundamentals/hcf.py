def find_hcf(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example usage
num1 = 48
num2 = 18
print(f"The HCF of {num1} and {num2} is {find_hcf(num1, num2)}")
