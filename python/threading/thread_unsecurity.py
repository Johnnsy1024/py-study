import threading
import time

lock = threading.Lock()


def increment_n_times(n):
    global total
    for i in range(n):
        total += 1


def safe_increment_n_times(n):
    global total
    for i in range(n):
        with lock:
            total += 1


def increment_n_times_in_x_threads(x, func, n):
    threads = [threading.Thread(target=func, args=(n,)) for _ in range(x)]
    global total
    total = 0
    begin_time = time.time()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()
    print(
        f"finished in {end_time-begin_time} \n total {total} \n expected {n*x} \n difference {n*x - total}({100-total/n/x*100}%)"
    )


print("unsafe")
increment_n_times_in_x_threads(20, increment_n_times, 100000)

print("\nwith locks")
increment_n_times_in_x_threads(20, safe_increment_n_times, 100000)
