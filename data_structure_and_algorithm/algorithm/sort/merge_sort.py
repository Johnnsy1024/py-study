"""
归并排序算法：时间复杂度：O(nlogn) 空间复杂度：（N）
"""


class MergeSort:
    def merge_sort(self, nums: list):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left_nums = nums[:mid]
        right_nums = nums[mid:]
        # 递归的核心：1.假定重复调用函数可以直接求出当前所需return的结果 2.在重复调用之前确定递归结束的条件
        left_nums = self.merge_sort(left_nums)
        right_nums = self.merge_sort(right_nums)

        res = []
        i = j = 0
        while i < len(left_nums) and j < len(right_nums):  # 实际上while中这两个条件只会有一个成立
            if left_nums[i] < right_nums[j]:
                res.append(left_nums[i])
                i += 1
            else:
                res.append(right_nums[j])
                j += 1
        res.extend(left_nums[i:])
        res.extend(right_nums[j:])
        return res


s = MergeSort()
print(s.merge_sort([5, 1, 3, 7, 2, 4]))
