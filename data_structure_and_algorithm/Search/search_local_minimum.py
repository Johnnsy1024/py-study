def find_local_minimum(arr: list):
    if len(arr) < 3:
        raise ValueError("数组的长度不能小于3")
    left = 0
    right = len(arr) - 1
    #  先检查数组左右两端
    if arr[left] < arr[left+1]:
        return arr[left]
    elif arr[right] < arr[right-1]:
        return arr[right]
    #  数组左右两端检查都找不到，选择中间值
    while left <= right:  # 一直二分到只有一个元素为止
        mid = left + (right - left) // 2  # 保证不溢出
        # Check if the mid element is a local minimum
        #  这步已经把mid<mid-1同时mid<mid+1的情况筛选出来了，如果这步没有return，那么必然这两种情况不是同时出现的
        if arr[mid] < arr[mid - 1] and arr[mid] < arr[mid + 1]:
            return arr[mid]

        # Choose the side with the smaller neighbor
        #  这里承接上一步筛选，如果不存在mid<mid-1同时mid<mid+1，那么二者肯定有一个不满足的

        if mid > 0 and arr[mid - 1] < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return None


# Test the function
arr = [9, 6, 3, 7, 5, 2, 8]
result = find_local_minimum(arr)
print("Local minimum:", result)
