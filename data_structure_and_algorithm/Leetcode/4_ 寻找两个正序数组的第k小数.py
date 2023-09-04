import heapq
from typing import List

# 方法一：最小堆进行n-k次堆化
class Solution:    
    def findkthminSortedArrays(self, nums1: List[int], nums2: List[int], k) -> float:
        res = []
        nums = nums1 + nums2
        for i in nums:
            heapq.heappush(res, i)
        n = len(nums)
        j = n - 1
        while j > n - k - 1:
            nums[0], nums[j] = nums[j], nums[0]
            tmp = nums[-1]
            nums = nums[:j]
            heapq.heapify(nums)
            j -= 1
        return tmp
# 方案二：双指针
class Solution:
    def findkthminSortedArrays(self, nums1: List[int], nums2: List[int], k) -> float:
        i, j = 0, 0
        del_cnt = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                del_cnt += 1
                if del_cnt == k:
                    return nums1[i]
                i += 1
            else:
                del_cnt += 1
                if del_cnt == k:
                    return nums2[j]
                j += 1
            
        while i < len(nums1):
            del_cnt += 1
            if del_cnt == k:
                return nums1[i]
            i += 1
        while j < len(nums2):
            del_cnt += 1
            if del_cnt == k:
                return nums2[j]
            j += 1
s = Solution()
l1 = [1, 3, 7, 8, 9, 10, 11, 12, 13, 14, 15]
l2 = [4, 5, 6]
print(s.findkthminSortedArrays(l1, l2, 9))     