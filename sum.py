def sum_of_even_numbers(n):
    total_sum = 0
    for num in range(1, n + 1):
        if num % 2 == 0:
            total_sum += num
    return total_sum

# Test the function with n = 10
n = 10
result = sum_of_even_numbers(n)
print(f"The sum of even numbers from 1 to {n} is: {result}")
