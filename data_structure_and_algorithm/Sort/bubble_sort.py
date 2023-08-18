class BubbleSort:
    def __init__(self):
        pass

    @staticmethod
    def bubble_sort(array):
        for i in range(len(array) - 1):  # i代表循环的轮数
            for j in range(0, len(array) - i - 1):  # j代表从位置0开始到已确定的第i大的值之前的位置
                if array[j] > array[j + 1]:
                    array[j], array[j+1] = array[j+1], array[j]  # 复杂度为1
        return "The result of bubble sort is {}".format(array)


print(BubbleSort.bubble_sort([7, 3, 5, 1, 2, 6]))
