class Sort:
    def __init__(self) -> None:
        pass

    # 快速排序
    """
    不稳定排序
    时间复杂度O(n**2)
    空间复杂度O(n)
    """

    def fast_sort(self, nums):
        print('fast sort')
        if len(nums) <= 1:
            return nums
        pivot = nums[len(nums) // 2]
        left, middle, right = [], [], []
        for i in nums:
            if i < pivot:
                left.append(i)
            elif i == pivot:
                middle.append(i)
            else:
                right.append(i)
        return self.fast_sort(left) + middle + self.fast_sort(right)

    # 归并排序
    """
    不稳定排序
    时间复杂度O(nlogn)
    空间复杂度O(n)
    """

    def merge_sort(self, nums):
        print('merge sort')
        if len(nums) <= 1:
            return nums
        middle = len(nums) // 2
        left = nums[:middle]
        right = nums[middle:]

        left = self.merge_sort(left)
        right = self.merge_sort(right)

        res = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        while j < len(right):
            res.append(right[j])
            j += 1
        while i < len(left):
            res.append(left[i])
            i += 1
        return res

    # 堆排序
    """
    不稳定排序
    时间复杂度O(nlogn)
    空间复杂度O(1)
    """

    def heapify(self, nums, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and nums[left] > nums[largest]:
            largest = left
        if right < n and nums[right] > nums[largest]:
            largest = right
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            self.heapify(nums, n, largest)

    def heap_sort(self, nums):
        for i in range(len(nums) // 2 - 1, -1, -1):
            self.heapify(nums, len(nums), i)
        for j in range(len(nums) - 1, 0, -1):
            # 此时已经整体最大堆化的数组的第一个位置是最大值
            nums[0], nums[j] = nums[j], nums[0]
            self.heapify(nums, j, 0)  # 这里不能传入nums的切片，因为要求传入的是nums的引用
        return nums

    # 插入排序
    """
    稳定排序
    时间复杂度O(n**2)
    空间复杂度O(1)
    """

    def inser_sort(self, nums):
        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                else:
                    break
        return nums

    # 选择排序
    """
    不稳定排序
    时间复杂度O(n**2)
    空间复杂度O(1)
    """

    def select_sort(self, nums):
        """
        每轮选择一个最小的放在最前面
        """
        for i in range(len(nums)):
            # min_value = nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums

    # 冒泡排序
    """
    稳定排序
    时间复杂度O(n**2)
    空间复杂度O(1)
    """

    def bubble_sort(self, nums):
        for i in range(len(nums) - 1):  # 每一轮确定一个当前循环的最大值，最多只需要确定n-1次即可
            for j in range(0, len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums


def dfs(graph: dict, start, target):
    if not start or not target:
        raise ValueError("Not get input start or target")
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()

        if node == target:
            return True
        if node not in visited:
            visited.add(node)
            for i in graph[node]:
                stack.append(i)

    return False


if __name__ == '__main__':
    # s = Sort()
    # nums = [5,2,4,6,3,1]
    # print(s.bubble_sort(nums))
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['C', 'F'],
        'C': ['G'],
        'D': [],
        'F': [],
        'G': []
    }
    print(dfs(graph, start='A', target='F'))
print()