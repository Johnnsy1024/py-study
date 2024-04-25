class Solution:
    def reversePairs(self, nums):
        self.count = 0
        self.merge_sort_count(nums)
        return self.count

    def merge_sort_count(self, nums):
        if len(nums) <= 1:
            return nums, 0
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        left, cnt = self.merge_sort_count(left)
        right, cnt = self.merge_sort_count(right)

        res, i, j = [], 0, 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                self.count += len(left) - i
                res.append(right[j])
                j += 1
            else:
                res.append(left[i])
                i += 1
        if i < len(left):
            res.extend(left[i:])
        else:
            res.extend(right[j:])
        return res, self.count

s = Solution()
print(s.reversePairs([7, 5, 6, 4]))