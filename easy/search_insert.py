def search_insert(nums: list[int], target: int) -> int:
    left_idx = 0
    right_idx = len(nums) - 1

    while left_idx <= right_idx:
        middle_idx = (left_idx + right_idx) // 2
        middle_elem = nums[middle_idx]
        if middle_elem == target:
            return middle_idx
        elif middle_elem > target:
            right_idx = middle_idx - 1
        else:
            left_idx = middle_idx + 1

    return left_idx


assert search_insert([1, 3, 5, 6], 5) == 2
assert search_insert([1, 3, 5, 6], 2) == 1
assert search_insert([1, 3, 5, 6], 7) == 4
assert search_insert([1, 3, 5, 6], 0) == 0
