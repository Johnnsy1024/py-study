class Solution:
    def isNumber(self, s: str) -> bool:
        n = len(s)
        index = 0
        has_num = has_e = has_sign = has_dot = False
        #如果有空格的话，先移动到非空格下标处
        while index < n and s[index] == ' ':
            index += 1
        while index < n:
            while index < n and '0' <= s[index] <= '9':
                index += 1
                has_num = True
            if index == n:#如果下标已经移出数组且之前都只有空格和数字，那么直接返回True
                break
            if s[index] == 'e' or s[index] == 'E':
                if has_e or not has_num:#如果已经有E或者e,此处再来一个e或E，如果碰到e但是前面没出现过数字，这两种情况都返回False
                    return False
                has_e = True
                has_num = has_sign = has_dot = False
            elif s[index] == '+' or s[index] == '-':
                if has_sign or has_num or has_dot:
                    return False
                has_sign = True
            elif s[index] == '.':
                if has_dot or has_e:
                    return False
                has_dot = True
            elif s[index] == ' ':
                break
            else:
                return False
            index += 1
        while index < n and s[index] == ' ':
            index += 1
        return has_num and index == n