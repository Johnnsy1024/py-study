"""
插入排序算法：保证在前n个数字位置上是有序的，有序顺序为从前往后（冒泡是从后往前）
"""
import random


# class InsertSort:
#     def __init__(self):
#         pass

#     @classmethod
#     def insert_sort(cls, array):
#         for i in range(1, len(array)):
#             for j in range(i-1, -1, -1):  # 从i-1位置倒序，终点为0，步长为-1
#                 if array[j] > array[j+1]:
#                     array[j], array[j+1] = array[j+1], array[j]
#                 else:  # 只要j位置的数字小于等于j+1位置的数字，直接退出当前循环，进入下一循环
#                     break
#         return array

# class InsertSort:
#     def __init__(self):
#         pass

#     @classmethod
#     def insert_sort(cls, dic):
#         for i in range(1, len(dic)):
#             for j in range(i-1, -1, -1):  # 从i-1位置倒序，终点为0，步长为-1
#                 if dic[j] > dic[j+1]:
#                     dic[j], dic[j+1] = dic[j+1], dic[j]
#                 else:  # 只要j位置的数字小于等于j+1位置的数字，直接退出当前循环，进入下一循环
#                     break
#         return dic

# random.seed(1)
# nums = {i : random.randint(0, 8) for i in range(6)}
# print(InsertSort.insert_sort(nums))

def unstable_selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def is_stable(arr, original_order):
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i][0] == arr[j][0] and original_order.index(arr[i]) > original_order.index(arr[j]):
                return False
    return True

# 测试选择排序的不稳定性验证
input_array = [(3, 1), (8, 2), (1, 3), (6, 4), (4, 5), (2, 6), (9, 7), (5, 8), (7, 9)]
original_order = list(input_array)  # 保存原始顺序的副本
print("未排序数组：", input_array)
unstable_selection_sort(input_array)
print("选择排序后的数组：", input_array)
print("是否稳定：", is_stable(input_array, original_order))


