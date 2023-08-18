class XOR:
    def __init__(self):
        pass

    @staticmethod
    def swap_xor(a, b):
        a = a ^ b
        b = a ^ b
        a = a ^ b
        return a, b


print(XOR.swap_xor(1, 2))
