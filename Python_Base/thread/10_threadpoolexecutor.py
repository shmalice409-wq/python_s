import time
from concurrent.futures import ThreadPoolExecutor


def task(num):
    print(f"task-{num} execute")
    time.sleep(1)
    print(f"task-{num} end")


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = [pool.submit(task, i) for i in range(10)]
        for f in futures:
            f.result()
