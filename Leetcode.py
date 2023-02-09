'''
724. Find Pivot Index

'''

nums = [1, 7, 3, 6, 5, 6]


left = 0
right = sum(nums)

for i in range(len(nums)):
    right = right - nums[i]
    if left == right:
        print(nums[i])
    left = left + nums[i]
print(-1)