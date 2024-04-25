def max_sublist_sum(nums):
    overall = partial = nums[0]
    for idx in range(1, len(nums)):
        # partial means the maximum value for item_sum before item(include)
        # choose itself or previous optimum value plus itself
        partial = max(partial + nums[idx], nums[idx])
        overall = max(partial, overall)
    return overall


print(max_sublist_sum([1, -2, 3, 5, -3, 2]))
