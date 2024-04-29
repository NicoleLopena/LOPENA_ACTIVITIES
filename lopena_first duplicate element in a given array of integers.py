def first_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1

# Test cases
print(first_duplicate([1, 2, 3, 4, 5, 4]))  # 4
print(first_duplicate([1, 2, 3, 4, 5]))  # -1
print(first_duplicate([1, 2, 3, 1, 4, 2, 5]))  # 1