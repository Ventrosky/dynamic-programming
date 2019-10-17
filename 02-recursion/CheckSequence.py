def check_sequence(nums, i):
    return i == len(nums)-1 or (nums[i] == nums[i+1]-1 and check_sequence(nums,i+1))

nums=[1,2,3,4,5,6,7,8]
print(check_sequence(nums, 0))