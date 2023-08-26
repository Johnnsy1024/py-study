def three_sum(arr: list) -> list:
    if len(arr) < 3:
        return []
    arr.sort()
    res = []
    for i in range(len(arr)):
        # if the i_st value of sorted array is bigger than 0
        # the sum of these three number will not equal to 0
        if arr[i] > 0:
            return res
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        L = i + 1
        R = len(arr) - 1
        while L < R:
            tmp = arr[i] + arr[L] + arr[R]
            if tmp == 0:
                res.append([arr[i], arr[L], arr[R]])
                while L < R and arr[L] == arr[L + 1]:
                    L += 1
                while L < R and arr[R] == arr[R - 1]:
                    R -= 1
                L += 1
                R -= 1
            elif tmp > 0:
                R -= 1
            else:
                L += 1
    return res
