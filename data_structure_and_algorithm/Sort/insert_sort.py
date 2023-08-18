"""
插入排序算法：保证在前n个数字位置上是有序的，有序顺序为从前往后（冒泡是从后往前）
"""
class InsertSort:
    def __init__(self):
        pass

    @classmethod
    def insert_sort(cls, array):
        for i in range(1, len(array)):
            for j in range(i-1, -1, -1):  # 从i-1位置倒序，终点为0，步长为-1
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                else:  # 只要j位置的数字小于等于j+1位置的数字，直接退出当前循环，进入下一循环
                    break
        return array

print(InsertSort.insert_sort([4, 2, 5, 7, 3, 6, 1]))