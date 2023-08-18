def factorial(n : int)  -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
n = 4
r = 2
# Permutation
print(factorial(n)//factorial(n-r))
# Combination
print(factorial(n)//(factorial(r)*factorial(n-r)))