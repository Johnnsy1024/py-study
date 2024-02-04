from functools import partial

new_int = partial(int, base=2)

print(new_int("101"))
