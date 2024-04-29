def contains_duplicate(nums):
    num_set = set()
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    return False

# Test cases
print(contains_duplicate([1, 2, 3, 4, 5]))  # False
print(contains_duplicate([1, 2, 3, 4, 2]))  # True
print(contains_duplicate([1, 1, 2, 2, 3, 3]))  # True
