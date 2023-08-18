def heapify(arr, n, i):
    largest = i  # 初始化最大元素的索引为父节点 i
    left = 2 * i + 1  # 左子节点索引
    right = 2 * i + 2  # 右子节点索引

    # 如果左子节点存在且大于根节点，则更新最大元素的索引
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 如果右子节点存在且大于根节点，则更新最大元素的索引
    if right < n and arr[right] > arr[largest]:
        largest = right

    # 如果最大元素的索引不是父节点 i，则交换父节点与最大元素
    """
    为什么这里能够保证当前子树的最大值节点保持在父节点就不用再往下了？
    因为我们在建立最大堆的时候，是从最后一个非叶子节点出发开始创建的,当前子树的后序子树们都已经保证了最大堆
    如果当前子树的左右节点都比当前的根节点小，那么根节点一定大于所有的后序子节点
    """
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # 对交换后的子树递归进行堆化操作
        heapify(arr, n, largest)

def nums_to_maxheap(nums):
    for i in range(len(nums)):
        #  将给定数组逐个和其父节点相比，如果比父节点大，则持续向上走
        while nums[i] > nums[int((i-1/2))]:
            tmp = nums[i]
            nums[i] = nums[int((i-1)/2)]
            nums[int((i-1)/2)] = tmp
            i = int((i-1)/2)

def heap_sort(arr):
    n = len(arr)
    # 构建最大堆，从最后一个非叶节点开始进行堆化操作
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # nums_to_maxheap(arr)
    # 逐个将堆顶元素（最大值）与当前未排序部分的末尾元素交换，并对剩余元素进行堆化操作
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换堆顶元素与末尾元素
        heapify(arr, i, 0)  # 对剩余元素进行堆化操作

    return arr


# 测试示例
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = heap_sort(arr)
print(sorted_arr)


