# def shell_sort(arr: list):
#     if not arr: return None
#     n = len(arr)
#     gap = n // 2
    
#     while gap > 0:
#         for i in range(n - gap):
#             j = i + gap
#             # 因为希尔排序是对插入排序的改进，所以每轮是从gap下标开始
#             while j >= gap and arr[j] < arr[j - gap]:
#                 arr[j], arr[j - gap] = arr[j - gap], arr[j]
#                 j -= gap
#         gap //= 2

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         for j in range(n - i - 1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr       
# def merge_sort(arr):
#     if not arr:return []
#     if len(arr) == 1:return arr
#     pivot = [arr[len(arr)//2]]
#     left = [i for i in arr if i < pivot[0]]
#     right = [i for i in arr if i > pivot[0]]
    
#     return merge_sort(left) + pivot + merge_sort(right)
# import heapq
# import random
# def heapify(arr, n, i):
#     # i：从下标i开始堆化
#     largest = i
#     left = 2* i + 1
#     right = 2* i + 2
    
#     if left < n and arr[left] > arr[largest]:
#         largest = left
#     if right < n and arr[right] > arr[largest]:
#         largest = right
        
#     if largest != i:
#         arr[largest], arr[i] = arr[i], arr[largest]
#         heapify(arr, n, largest)
        
# def heap_sort(arr):
#     for i in range(len(arr)//2 - 1, -1, -1):
#         heapify(arr, len(arr), i)
#     for i in range(len(arr) - 1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]
#         heapify(arr, i, 0)
# import random
# def insert_sort(arr):
#     for i in range(1, len(arr)):
#         for j in range(i, 0, -1):
#             if arr[j] < arr[j - 1]:
#                 arr[j], arr[j - 1] = arr[j-1], arr[j]
#             else:
#                 break
# nums = [random.randint(0, 7) for _ in range(6)]
from collections import Counter
def count_sort(arr):
    if not arr: return 
    min_val, max_val = min(arr), max(arr)
    c = Counter(arr)
    cnt = [0] * max_val
    res = []
    for i in range(len(cnt)):
        cnt[i] = c[i+min_val+1]
        res.extend()
        
print(nums)
print(insert_sort(nums))
print(nums)
