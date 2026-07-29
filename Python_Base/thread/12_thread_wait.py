import time
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait


def work(x):
    time.sleep(x)
    return x


if __name__ == "__main__":
    with ThreadPoolExecutor(3) as pool:
        # 这里使用线程池的submit提交线程任务,最后返回的是一个任务列表,但是可能还没有运行完
        fs = [pool.submit(work, t) for t in [2, 1, 3]]
        # wait 是等待线程运行结束,可以选择等待第一个运行完成的,还是全部完成
        done, pending = wait(fs, return_when=FIRST_COMPLETED)
        # pending是未完成的任务的集合
        print(pending)
        print("first end is ", [done.result() for done in done])
