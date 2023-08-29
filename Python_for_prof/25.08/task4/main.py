def recursive_sum(nums):
    if not nums:
        return 0
    return nums[0] + recursive_sum(nums[1:])

numbers = [1, 9, 2, 8, 7, 3]

print(recursive_sum(numbers))
