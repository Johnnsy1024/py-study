"""
输入一个递增排序的数组和一个数字s
在数组中查找两个数
使得它们的和正好是s
如果有多对数字的和等于s
则输出任意一对即可。
"""


# 双指针
def twoSum(nums: list, target: int) -> list:
    left, right = 0, len(nums) - 1
    while left < right:
        tmp = nums[left] + nums[right]
        if tmp == target:
            return [nums[left], nums[right]]
        elif tmp > target:
            right -= 1
        else:
            left += 1
    return []
# 哈希表
def two_sum_hash(nums: list, target: int) -> list:
    tmp_map = {}
    for i in nums:
        tmp = target - i
        if tmp in tmp_map.keys():
            return [tmp, i]
        else:
            tmp_map[i] = True
    return []


arr = [2, 3, 4, 5, 6]
print(two_sum_hash(arr, 8))
