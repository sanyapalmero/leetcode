def remove_element(nums: list, val: int) -> int:
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k], nums[i] = nums[i], nums[k]
            k += 1

    print(nums)
    return k


print(remove_element([3, 2, 2, 3], 3))
# [2, 2] -> 2

print(remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))
# [0, 1, 4, 0, 3] -> 5

