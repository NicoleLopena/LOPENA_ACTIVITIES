def remove_duplicates(input_list):
    """Returns a new list with distinct elements from the input list."""
    return list(set(input_list))

# Example usage:
my_list = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(my_list))  # Output: [1, 2, 3, 4, 5]