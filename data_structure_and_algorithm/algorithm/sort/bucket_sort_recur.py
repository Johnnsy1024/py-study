def bucket_sort(arr: list, bucket_cnt: int):
    if len(arr) < 2:
        return arr
    max_val = max(arr)
    min_val = min(arr)
    bucket_num = len(arr)
    bucket_range = (max_val - min_val) / bucket_num
    bucket = [[] for _ in range(bucket_num)]
    for i in arr:
        index = int((i - min_val) / bucket_range)
        if index == bucket_num:  # 把最大值包含进来
            index -= 1
        bucket[index].append(i)
    res = []
    for b in bucket:
        res.extend(bucket_sort(b, bucket_cnt))
    return res


if __name__ == "__main__":
    print(bucket_sort([8, -1, 2, 1, 0], 2))
