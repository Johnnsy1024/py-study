import time
from functools import wraps

#  类装饰器（函数替换）
class timer:
    def __init__(self, print_args: bool):
        self.print_args = print_args

    def __call__(self, func):
        @wraps(func)
        def decorated(*args, **kwargs):
            st = time.perf_counter()
            ret = func(*args, **kwargs)
            if self.print_args:
                print(f'{func.__name__}, args: {args}, kwargs: {kwargs}')
            print(f'time cost: {time.perf_counter() - st} seconds')

            return ret

        return decorated


@timer(True)
def print_hhh():
    print('hhh')

# print_hhh()

def fuck(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        print('this is a function warpper')
        func(*args, **kwargs)
        
    return decorator
        
    
@fuck
def print_hhh():
    print('i am so happy')
    
print_hhh()