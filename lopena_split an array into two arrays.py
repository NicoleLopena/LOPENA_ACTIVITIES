def split_even_odd(arr):
    even_numbers = [num for num in arr if num % 2 == 0]
    odd_numbers = [num for num in arr if num % 2 != 0]
    return even_numbers, odd_numbers

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even, odd = split_even_odd(arr)
print("Even numbers:", even)
print("Odd numbers:", odd)