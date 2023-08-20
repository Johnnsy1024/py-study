from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        def judge(nums: List[int], res=0):
            length = len(nums)
            if not length:
                return None, res
            if length == 1:
                return nums, res
            pivot = length//2
            left, res = judge(nums[:pivot], res)
            right, res = judge(nums[pivot:], res)

            res_list = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] > right[j]:
                    res += len(left) - i
                    res_list.append(right[j])
                    j += 1
                else:
                    res_list.append(left[i])
                    i += 1
            while i < len(left):
                res_list.append(left[i])
                i += 1
            while j < len(right):
                res_list.append(right[j])
                j += 1
            return res_list, res
        if not nums: return 0
        _, res = judge(nums)
        
        return res


s = Solution()
print(s.reversePairs([7,5,6,4]))