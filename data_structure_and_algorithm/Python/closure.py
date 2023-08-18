# def wrapper(n):
#     cnt = 0
#     def inner():
#         nonlocal cnt
#         for i in range(n):
#             if i % 2 == 0:
#                 cnt += 1
#         return cnt
#     return inner

# s = wrapper(100)
# print(s())
# print(s())
# print(s())
# print(s())
def adder(x):
    def wrapper(y):
        return x + y
    return wrapper
adder5 = adder(5)
print(adder5(adder5(6)))