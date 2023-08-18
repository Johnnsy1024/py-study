# 非递归方法
def fibonacci(n : int) -> int:
    if n <= 0:
        return 0
    if n <= 2:
        return 1
    a, b = 1, 1
    for i in range(3, n+1):
        tmp = a + b
        a = b
        b = tmp
    return tmp




# 原递归：要计算两个递归
def fibonacci1(n : int)-> int:
    """_summary_

    Args:
        n (int): 第n个fibonacci数

    Returns:
        int: 
    """
    if n <= 0:
        return 0
    if n <= 2:
        return 1
    return fibonacci1(n - 1) + fibonacci1(n - 2)

# 优化递归：函数参数中维护前两个fibonacci数
def fibonacci2(n : int, first : int = 1, second : int = 1)-> int:
    """_summary_

    Args:
        n (int): 第n个fibonacci数
        first (int): 第一个fibonacci数
        second (int): 第二个fibonacci数

    Returns:
        int: 
    """
    if n <= 0:
        return 0
    if n <= 2:
        return 1
    if n == 3: # 这里实际上是常规情况下（n非0、1、2）时的递归退出位置
        return first + second
    return fibonacci2(n - 1, second, first + second)

print(fibonacci(6))