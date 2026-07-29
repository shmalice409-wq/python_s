"""condition条件变量来控制线程之间的通讯
用生产者消费者来模拟"""

import threading
import time

goods = 0
cond = threading.Condition()
max_goods = 5


def producer():
    global goods
    while True:
        with cond:
            if goods >= max_goods:
                print("goods is full. producer waiting...")
                cond.wait()
            goods += 1
            print(f"product one, goods: {goods}")
            if goods == 1:
                cond.notify_all()
        time.sleep(0.5)


def consumer():
    global goods
    while True:
        with cond:  # 使用cond条件变量，python自动上锁
            if goods <= 0:
                print("goods is empty, consumer waiting...")
                cond.wait()
            goods -= 1
            print(f"consume one. goods :{goods}")
            if goods != max_goods:
                cond.notify_all()
        time.sleep(
            0.8
        )  # 这里不能在cond里面睡，不然锁不会解开，就只有0 1,0 1 .....无限循环


if __name__ == "__main__":
    p = threading.Thread(target=producer)
    c = threading.Thread(target=consumer)
    p.start()
    c.start()
