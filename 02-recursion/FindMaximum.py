def maximum(nums, i):
    if i == 0:
        return nums[0]
    else:
        return max(nums[i], maximum(nums, i - 1))


nums = [4, 3, 6, 7, 0, 9, 2]
print(maximum(nums, len(nums)-1))
