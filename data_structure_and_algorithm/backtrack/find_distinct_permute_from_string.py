"""
给定一个只含有大写字母的字符串，返回其不重复的排列组合
"""


def permute(string: str):
    result = []
    backtrack(string, [], result)
    return set(result)


def map_dig_str(string: str, dig: list):
    res = ''
    for i in dig:
        res += string[i]
    return res


def backtrack(string: str, current: list, result: list):
    if len(current) == len(string):
        result.append(map_dig_str(string, current.copy()))
        return
    for i in range(len(string)):
        if i not in current:
            current.append(i)
            backtrack(string, current, result)  # 每次满足了回溯条件才会走到下一步
            current.pop()


print(permute('ABAC'))
