"""
选择排序算法：与冒泡排序类似，冒泡排序每轮找到一个最大值放在末尾，选择排序每轮找到一个最小值放在初始位置
"""
class SelectSort:
    def __init__(self):
        pass

    @staticmethod
    def select_sort(array):
        for i in range(len(array) - 1):
            #  和冒泡排序一样，一次确定一个值摆放的位置，一共确定n-1轮
            min_vaule = array[i]
            for j in range(i + 1, len(array)):
                if array[j] < min_vaule:
                    array[i], array[j] = array[j], array[i]
                    min_vaule = array[j]
        return array


print(SelectSort.select_sort([7, 3, 2, 1, 4, 2, 10, 0]))
