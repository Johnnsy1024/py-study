def counting_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # 找到最大值和最小值
    min_val = min(arr)
    max_val = max(arr)
    
    # 创建计数数组
    count_array = [0] * (max_val - min_val + 1)
    
    # 统计每个元素的出现次数
    for num in arr:
        count_array[num - min_val] += 1
    
    res = []
    for i in range(len(count_array)):
        res.extend([min_val+i]*count_array[i])
    # 对计数数组进行累加
    # for i in range(1, len(count_array)):
    #     count_array[i] += count_array[i - 1]
    
    # # 创建结果数组
    # sorted_array = [0] * len(arr)
    
    # # 根据计数数组的信息将元素放入结果数组
    # for num in reversed(arr):
    #     index = count_array[num - min_val] - 1
    #     sorted_array[index] = num
    #     count_array[num - min_val] -= 1
    
    return res

# 示例
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print(sorted_arr)
