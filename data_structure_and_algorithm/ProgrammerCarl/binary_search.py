def binary_search(nums : list, left : int, right : int, target : int) -> int:
    while right >= left: # 如果当前找的只剩下一个数了，还没有实现target = nums[mid]，那么下一步就会导致right和left的指针错位
        mid = left + (right - left) // 2
        if target > nums[mid]:
            left = mid + 1
            return binary_search(nums, left, right, target) # 切记，如果要用两个指针来实现二分查找的话，递归时传入的数组一定不要再用指针进行切片了
        if target == nums[mid]:
            return mid
        right = mid - 1
        return binary_search(nums, left, right, target)
    
    return -1

def binary_search2(nums : list, target : int) -> int:
    if not nums:
        return - 1
    mid = len(nums) // 2
    if target > nums[mid]:
        return binary_search2(nums[mid + 1 :], target)
    if target < nums[mid]:
        return binary_search2(nums[:mid], target)
    return mid

arr = [2, 5, 6, 9, 12, 13]
# print(binary_search2(arr, 0, len(arr) - 1, 12))
print(binary_search2(arr, 2))