def func(string: str):
    max_step = len(string) // 2
    dp1 = [string] * max_step
    dp2 = [string] * max_step
    for i in range(max_step):
        dp1[i] = string[i + 1:] + string[i]
        
    
    