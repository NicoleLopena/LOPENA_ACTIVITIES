def find_difference(arr):
    if not arr:
        return []

    avg = sum(arr) / len(arr)
    differences = [num - avg for num in arr]
    return differences

# Example usage:
arr = [1, 2, 3, 4, 5]
differences = find_difference(arr)
print("Differences:", differences)