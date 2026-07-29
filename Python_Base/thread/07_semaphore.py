"""这一篇是使用信号量Semaphore来控制并发数"""

import threading
import time

# 这里决定并发数为3
sem = threading.Semaphore(3)


def crawl(url):
    """假装爬虫来进行模拟
    这里我们可以看到一次只有3个线程可以运行，其他的需要等待资源释放
    :param url: 链接
    """
    with sem:
        print(f"{url} is crawled,thread:{threading.current_thread().name}")
        time.sleep(2)
        print(f"{url} is over")


if __name__ == "__main__":
    urls = [f"url-{i}" for i in range(10)]

    t_list = []

    for url in urls:
        t = threading.Thread(target=crawl, args=(url,))
        t_list.append(t)
        t.start()

    for t in t_list:
        t.join()
