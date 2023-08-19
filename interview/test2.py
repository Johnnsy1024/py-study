import sys

for idx, line in enumerate(sys.stdin):
    if idx != 0:
        a = line.split()
        nums = [int(a[i]) for i in range(len(a))]

        from copy import deepcopy


        def exec_1(arr, res):
            if len(arr) == 1:
                res.append(arr[0])
                return arr[0]
            a, b = arr[-1], arr[-2]
            tmp = (a + b) % 10
            arr.pop()
            arr[-1] = tmp
            arr_1 = deepcopy(arr)
            arr_2 = deepcopy(arr)
            tmp1 = exec_1(arr_1, res)
            tmp2 = exec_2(arr_2, res)

        def exec_2(arr, res):
            if len(arr) == 1:
                res.append(arr[0])
                return arr[0]
            a, b = arr[-1], arr[-2]
            tmp = (a * b) % 10
            arr.pop()
            arr[-1] = tmp
            arr_1 = deepcopy(arr)
            arr_2 = deepcopy(arr)
            tmp1 = exec_1(arr_1, res)
            tmp2 = exec_2(arr_2, res)
        res = []
        arr_1 = deepcopy(nums)
        arr_2 = deepcopy(nums)
        exec_1(arr_1, res)
        result = []
        for i in range(10):
            result.append(str(res.count(i)//2))
        print(' '.join(result))
