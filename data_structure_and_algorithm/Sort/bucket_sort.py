from random import randint

def bucket_sort(nums : list, bucket_num: int):
    max_val, min_val = -10000, 10000 
    for i in nums:
        max_val = i if max_val < i else max_val
        min_val = i if min_val > i else min_val
    bucket_range = (max_val - min_val) / bucket_num
    bucket = [[] for _ in range(bucket_num)]
    for i in nums:
        index = int((i - min_val) / bucket_range)
        if index == bucket_num:
            index -= 1
        bucket[index].append(i)  
    res = []
    for b in bucket:
        b.sort()
        res.extend(b)
    return res

arr = [randint(0, 10) for _ in range(10)]
print('before sort {}'.format(arr))
print('after sort {}'.format(bucket_sort(arr, 10)))