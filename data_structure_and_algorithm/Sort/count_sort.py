from collections import Counter
from random import randint

def count_sort(nums):
    max_val, min_val = 0, 0
    for i in nums:
        if i > max_val:
            max_val = i
        if i < min_val:
            min_val = i
    cnt = [0] * max_val
    res = []
    c = Counter(nums)
    for i in range(len(cnt)):
        cnt[i] = c[i+min_val+1]
        res.extend([i+1]*cnt[i])
    return res

print(count_sort([randint(0, 7) for _ in range(10)]))