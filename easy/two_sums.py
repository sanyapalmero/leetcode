"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

def two_sums(nums, target):
    for idx, num in enumerate(nums):
        for idx_2, second_num in enumerate(nums):
            if idx == idx_2:
                continue
            elif num + second_num == target:
                return [idx, idx_2]


def two_sums_v2(nums, target):
    for idx, num in enumerate(nums):
        if target - num in nums and nums.index(target - num) != idx:
            return [idx, nums.index(target - num)]


nums = [2, 7, 11, 15]
target = 9

res = two_sums(nums, target)
res_2 = two_sums_v2(nums, target)
print(res, res_2)
