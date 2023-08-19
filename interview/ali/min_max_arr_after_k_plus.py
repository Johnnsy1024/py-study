"""
给定一个数组 a，包含 n 个整数
再给定一个整数 k，可以给数组中任意整数加 1，总共可以加 k 次
加完 k 次后，找到数组中的最大值。最后要求得一个最小的最大值
"""
from pydantic import BaseModel, StrictInt
from typing import List
class Find(BaseModel):
    nums : list
    k : StrictInt
    
    def find_min_max(self):
        max_val = max(self.nums)
        sum_val = sum([max_val - self.nums[i] for i in range(len(self.nums))])
        if self.k <= sum_val:
            return max_val
        else:
            tmp1 = (self.k - sum_val) % len(self.nums) # 差值与数组长度的余数
            tmp2 = (self.k - sum_val) // len(self.nums) # 差值与数组长度整除倍数
            if tmp1 == 0:
                return max_val + tmp2
            else:
                return max_val + tmp2 + 1


f = Find(nums=[1, 2, 3, 4, 5], k=16)
print(f.find_min_max())