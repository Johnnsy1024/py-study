def find_min_m(nums, m):
    left = 0
    right = m - 1
    min_value_sum = sum(nums[left:right + 1])
    while right <= len(nums) - 1:
        left += 1
        right += 1
        new_sum_value = sum(nums[left:right + 1])
        if new_sum_value < min_value_sum:
            min_value_sum = new_sum_value
    return min_value_sum


print(find_min_m([4, 3, 2, 4, 5], 3))
