"""
将字符串转化为整数
有很多离谱的用例：-abc, +-2等等
"""


class Solution:
    def judge_range(self, res: list):
        if int(''.join(res)) > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif int(''.join(res)) < -2 ** 31:
            return -2 ** 31
        else:
            return int(''.join(res))

    def loop_judge(self, res: list, str_: str, start: int):
        for i in range(start, len(str_)):
            if str_[i].isdigit():
                res.append(str_[i])
            else:
                return self.judge_range(res)
        return self.judge_range(res)
    def strToInt(self, string: str):
        str_ = string.strip()
        """
        几种不做处理的情况：
        1.去掉两侧空白后的字符串为空
        2.去掉两侧空白后的字符串只是一个正负号
        3.去掉两侧空白后的字符串第一位既不是正负号也不是数字
        4.去掉两侧空白后的字符串第一位是正负号，但是第二位不是数字
        """
        if not str_ or str_ in ('+', '-') or (not str_[0].isdigit() and str_[0] not in ('+', '-')) or (str_[0] in ('+', '-') and not str_[1].isdigit()):
            return 0
        #  此时str_不再会出现上述不做处理的情况
        if str_[0] in ('+', '-'):  # 第一位是正负号
            res = [str_[0]]  # 这里如果res设定为str的话，无法在函数中传参
            return self.loop_judge(res, str_, 1)  # 基于res，从str_的第二位开始循环
        else:
            res = []
            return  self.loop_judge(res, str_, 0)


s = Solution()
print(s.strToInt(""))
