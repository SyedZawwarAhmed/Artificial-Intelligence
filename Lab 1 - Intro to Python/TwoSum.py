# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# This problem is taken from leetcode.com

def two_sum(nums, target):
    result = []
    for i in range(len(nums)):
        first_num = nums[i]
        second_num = target - first_num
        for j in range(len(nums)):
            if j != i and second_num == nums[j]:
                result.append(i)
                result.append(j)
                return result
    return result

nums_str = input("Enter the numbers separated by space: ")
nums_list = nums_str.split()
nums = []
i = 0
while i < len(nums_list):
    nums.append(int(nums_list[i]))
    i += 1
target = int(input("Enter the target number: "))
result = two_sum(nums, target)
print(result)
