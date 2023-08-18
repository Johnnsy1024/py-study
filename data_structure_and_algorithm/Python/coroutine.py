def my_coroutine():
    while True:
        received = yield
        print('Received:', received)


coroutine = my_coroutine()
next(coroutine)
for i in range(100):
    coroutine.send(f'fuck{i}')
