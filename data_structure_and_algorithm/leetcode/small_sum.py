# def merge(left, right):
#     i, j, res = 0, 0, []
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             res.append(left[i])
#             i += 1
#         else:
#             res.append(right[j])
#             j += 1
#     res.extend(left[i:])
#     res.extend(right[j:])
#     return res

class SmallSum:
    def __init__(self):
        self.smallsum = 0

    def small_sum(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        left = self.small_sum(left)
        right = self.small_sum(right)

        i, j, res = 0, 0, []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                self.smallsum += left[i] * (len(right) - j)
                i += 1
            else:
                res.append(right[j])
                j += 1
        res.extend(left[i:])
        res.extend(right[j:])
        return res


arr = [1, 3, 4, 2, 5]
solution = SmallSum()
print(solution.small_sum(arr), solution.smallsum)
