def bin_search(nums, target):
    if len(nums) < 1:
        return False
    mid = len(nums) // 2
    if target == nums[mid]:
        return True
    if target < nums[mid]:
        res = bin_search(nums[:mid], target)
    if target > nums[mid]:
        res = bin_search(nums[mid + 1:], target)
    return res


num = [1, 2, 3, 4, 5]
print(bin_search(nums=num, target=4))
