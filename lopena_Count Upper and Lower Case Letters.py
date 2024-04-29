def count_case_letters(s):
    """Counts the number of upper and lower case letters in a string."""
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count

# Example usage:
text = "Hello, World!"
upper, lower = count_case_letters(text)
print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")
# Output: Uppercase letters: 2, Lowercase letters: 8