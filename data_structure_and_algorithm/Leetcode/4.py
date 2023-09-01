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

s = Solution()
nums1 = [1,3]
nums2 = [2]
print(s.findMedianSortedArrays(nums1, nums2))