"""
给定一个数组，其下标对应位置为其最多能往后跳跃的步数
"""


def can_jump(nums):
    # 记录当前能够跳到的最远位置
    max_jump = 0
    # 遍历数组
    for i in range(len(nums)):
        # 如果当前位置无法到达，直接返回False
        if i > max_jump:
            return False
        # 更新能够跳到的最远位置
        max_jump = max(max_jump, i + nums[i])
        # 如果最远位置已经达到或超过最后一位，说明可以跳到最后一位
        if max_jump >= len(nums) - 1:
            return True
    # 遍历完整个数组后仍未达到最后一位，返回False
    return False


# 测试
nums = [2, 3, 1, 1, 4]
print(can_jump(nums))  # 输出: True

nums = [3, 2, 1, 0, 4]
print(can_jump(nums))  # 输出: False
