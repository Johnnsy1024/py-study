def sum_from_num1_to_num2(n):
    if n == 0:
        return 0
    return n + sum_from_num1_to_num2(n-1)
print(sum_from_num1_to_num2(100))