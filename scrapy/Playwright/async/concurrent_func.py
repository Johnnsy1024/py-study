import asyncio
import time
import logging

# 异步函数1
async def task1():
    print("Task 1: Start")
    print(f'Task 1\'s time is {time.time()}')
    await asyncio.sleep(2)  # 模拟一个耗时操作
    print("Task 1: End")

# 异步函数2
async def task2():
    print("Task 2: Start")
    print(f'Task 2\'s time is {time.time()}')
    await asyncio.sleep(1)  # 模拟一个耗时操作
    print("Task 2: End")

# 异步函数3
async def task3():
    print("Task 3: Start")
    print(f'Task 3\'s time is {time.time()}')
    await asyncio.sleep(3)  # 模拟一个耗时操作
    print("Task 3: End")

async def main():
    # 并发执行多个异步任务
    await asyncio.gather(task1(), task2(), task3())

if __name__ == "__main__":
    asyncio.run(main())
