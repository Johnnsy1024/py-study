from find_distinct_subseq import find_subsequences
import time

def find(nums, target):
    total = find_subsequences(nums)
    tmp = [sum(i) for i in total]
    i = 0
    while i < len(tmp):
        if tmp[i] == target:
            return total[i]
        i += 1

nums = [1, 2, 3, 4, 6]
target = 13
start_time = time.time()
print(find(nums, target))
end_time = time.time()
print(end_time-start_time)