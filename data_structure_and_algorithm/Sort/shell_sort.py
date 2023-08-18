def shell_sort(arr : list):
    if not arr: return
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(n - gap):
            j = i + gap
            while j >= gap and arr[j] < arr[j - gap]:
                arr[j], arr[j - gap] = arr[j - gap], arr[j]
                j -= gap
        gap //= 2


if __name__ == '__main__':
    import random
    arr = [random.randint(0, 100) for _ in range(10)]
    print(f'arr before sorting{arr}')
    shell_sort(arr)
    print(f'arr after sorting{arr}')