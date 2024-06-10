import threading
import time

a = {"a": []}


def block():
    time.sleep(1)
    pass


def abc():
    if len(a["a"]) == 0:
        block()
        a["a"].append(2)


def abc2():
    if len(a["a"]) == 0:
        block()
        a["a"].append(3)


t1 = threading.Thread(target=abc)
t2 = threading.Thread(target=abc2)

t2.run()
t1.run()
print(a)
