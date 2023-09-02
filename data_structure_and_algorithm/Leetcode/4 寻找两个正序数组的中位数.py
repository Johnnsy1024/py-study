from typing import List
"""
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。
"""
class Solution:    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 + nums2:
            return
        n1 = len(nums1)
        n2 = len(nums2)
        i, j = 0, 0
        res = []
        while i < n1 and j < n2: 
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        while i < n1:
            res.append(nums1[i])
            i += 1
        while j < n2:
            res.append(nums2[j])    
            j += 1
        if (n1+n2) % 2 != 0:
            return res[len(res) // 2]
        else:
            mid = len(res) // 2
            return (res[mid - 1] + res[mid]) / 2

class Solution:
    def judge(self, left_cnt, right_cnt, nums)-> bool:
        if left_cnt + right_cnt < len(nums) // 2:
            return False
        elif left_cnt + right_cnt == len(nums) // 2:
            return True
            
        # if left_cnt + right_cnt == len(nums) // 2 and len(nums) % 2 == 0:
        #     return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2
        # else:
        #     return False
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        if not nums:
            return
        if len(nums) % 2 == 0:
            
        n1 = len(nums1)
        n2 = len(nums2)
        i, j, left_cnt, right_cnt = 0, 0, 0, 0
        while i < n1 and j < n2: 
            if nums1[i] <= nums2[j]:
                left_cnt += 1
                i += 1
            else:
                right_cnt += 1
                j += 1
            if self.judge(left_cnt, right_cnt, nums):
                return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2 if len(nums) % 2 == 0 else nums[len(nums) // 2]
        while i < n1:
            left_cnt += 1
            i += 1
            if self.judge(left_cnt, right_cnt, nums):
                return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2 if len(nums) % 2 == 0 else nums[len(nums) // 2]
        while j < n2:
            right_cnt += 1   
            j += 1
            if self.judge(left_cnt, right_cnt, nums):
                return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2 if len(nums) % 2 == 0 else nums[len(nums) // 2]            
        # if (n1+n2) % 2 != 0:
        #     return res[len(res) // 2]
        # else:
        #     mid = len(res) // 2
        #     return (res[mid - 1] + res[mid]) / 2

s = Solution()
nums1 = [1,3]
nums2 = [2]
print(s.findMedianSortedArrays(nums1, nums2))