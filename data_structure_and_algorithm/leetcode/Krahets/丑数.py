# class Solution:
#     def nthUglyNumber(self, n: int) -> int:
#         if n == 1:
#             return 1
#         two = [1]
#         three = [1]
#         five = [1]

#         m = 1
#         i, j, k = 1, 1, 1
#         while m < n:
#             a, b, c = i*2, i*3, i*5
#             two.append(a)
#             three.append(b)
#             five.append(c)
#             select = min(two[i], three[j], five[k])
#             if select == two[i]:
#                 i += 1
#             elif select == three[j]:
#                 j += 1
#             else:
#                 k += 1
#             m += 1
#         return select

# s = Solution()
# print(s.nthUglyNumber(10))

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        two = [1]
        three = [1]
        five = [1]

        m = 1
        i, j, k = 1, 1, 1
        while m < n:
            a, b, c = i*2, j*3, k*5
            select = min(a, b, c)
            if select == a:
                i += 1
            if select == b:
                j += 1
            if select == c:
                k += 1
            m += 1
        return select

s = Solution()
print(s.nthUglyNumber(11))
