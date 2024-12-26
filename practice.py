
def sum_of_natural_numbers(n):
    return n + sum_of_natural_numbers(n - 1) if n > 0 else 0


n = int(input("Enter a positive integer: "))
print("The sum of natural numbers up to {n} is: {sum_of_natural_numbers(n)}")
