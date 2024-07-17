def merge_sort(arr: list):
    # 归并排序，时间复杂度O(nlogn)，空间复杂度O(n)，稳定排序
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    i = j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        elif left[i] >= right[j]:
            res.append(right[j])
            j += 1
    if i == len(left):
        res.extend(right[j:])
    elif j == len(right):
        res.extend(left[i:])
    return res


def heapify(arr: list, n: int, i: int):
    # 通过输入参数n来控制最大堆化的范围
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[largest] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(
            arr, n, largest
        )  # 交换之后，与largest交换的元素作为根节点的子树不一定是最大堆


def heap_sort(arr: list):
    # 堆排序 时间复杂度O(nlogn)，空间复杂度O(1) 不稳定排序
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)  # 由于heapify函数要输入最大堆化的个数n，因此直接输入arr即可
    return arr


def select_sort(arr: list):
    # 选择排序 时间复杂度O(n^2), 空间复杂度O(1) 不稳定排序
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr


def insert_sort(arr: list):
    # 插入排序 时间复杂度O(n^2) 空间复杂度O(1) 稳定排序
    n = len(arr)
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                break
    return arr


def fast_sort(arr: list):
    # 快速排序 时间复杂度O(nlogn)
    if len(arr) <= 1:
        return arr
    mid = arr[len(arr) // 2]
    left, right, middle = [], [], []
    for i in arr:
        if i < mid:
            left.append(i)
        elif i > mid:
            right.append(i)
        else:
            middle.append(i)
    return fast_sort(left) + middle + fast_sort(right)


def bucket_sort(arr: list, bucket_num: int):
    # 桶排序 空间复杂度O(k + n) 时间复杂度最好为O(n)，最差为O(nlogn)
    max_val, min_val = arr[0], arr[0]
    for i in arr:
        if i < min_val:
            min_val = i
        elif i > max_val:
            max_val = i
    max_val = max(arr)
    min_val = min(arr)
    bucket_range = (max_val - min_val) / bucket_num
    buckets = [[] for _ in range(bucket_num)]
    for i in arr:
        index = int((i - min_val) / bucket_range)
        if index == bucket_num:
            index -= 1
        buckets[index].append(i)
    res = []
    for k in buckets:
        k.sort()
        res.extend(k)
    return res


if __name__ == "__main__":
    arr = [1, 2, 4, 3, 6, 5]
    print(merge_sort(arr))
    print(heap_sort(arr))
    print(select_sort([2, 1, -2, 6]))
    print(select_sort([2, 1, -2, 6]))
    print(fast_sort([2, 1, -2, 6]))
    print(bucket_sort([2, 1, -2, 6], 3))
