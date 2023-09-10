# coding: utf-8
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED, ALL_COMPLETED, as_completed
import time
import random
import datetime

def spider(page):
    time.sleep(page)
    print(f"crawl task{page} finished")
    return page

def read_result(task_list: list) ->int:
    for i in task_list:
        print(i.result())
        
# 线程池采用类似上下文的结构
def thread_pool_exec(max_workers=5):
    with ThreadPoolExecutor(max_workers=max_workers) as t:  # 创建一个最大容纳数量为5的线程池
    # # 当提交任务数大于最大容纳数量时，池外任务会等待前面任务执行结束
    #     all_task1 = [t.submit(spider, page) for page in range(max_workers)]
    #     # wait方法按给定顺序依次执行
    #     wait(all_task1, return_when=FIRST_COMPLETED) # 第一个任务结束后就跳到下一行
    #     print('all_task1 finished!')
        
    #     all_task2 = [t.submit(spider, page) for page in range(max_workers, 2*max_workers)]
    #     wait(all_task2, timeout=50, return_when=ALL_COMPLETED)
    #     print('all_task2 all finished')
        
    #     read_result(all_task2)
        
        all_task3 = [t.submit(spider, page) for page in [5, 3, 2]]
        for future in as_completed(all_task3): # as_completed方法是一个生成器，在没有任务完成的时候，会一直阻塞
            print('终于畅通了{}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            print(future.result())
        
    # print(f"task1: {task1.done()}")  # 通过done来判断线程是否完成
    # print(f"task2: {task2.done()}")
    # print(f"task3: {task3.done()}")
    # print(f"task4: {task4.done()}")
    # print(f"task5: {task5.done()}")
    # print(f"task6: {task6.done()}")

    # time.sleep(2.5) # 这里停止了2.5s，因此只有任务1和2完成了
    # print(f"task1: {task1.done()}")
    # print(f"task2: {task2.done()}")
    # print(f"task3: {task3.done()}")
    # print(task1.result())  # 通过result来获取返回值

if __name__ == "__main__":
    thread_pool_exec()