""" 进程之间存在隔离，我们可以通过使用共享队列来进行通讯
下面将使用一个简单的生产者消费者问题来进行学习
"""

import multiprocessing
import time

def producer(q):
    """生产者生成数据

    Args:
        q (队列): 共享队列，生产者向其中放入数据
    """
    for i in range(10):
        q.put(f'数据{i}')
        print(f'生产者写入数据{i}')
    q.put('end')
    print("生产者进程结束")
    

def conusumer(q):
    """消费者从队列中获得数据

    Args:
        q (队列): 共享队列，消费者从里面把数据去除
    """
    while True:
        #当队列为空的时候进阻塞
        data=q.get()
        if data=='end':
            break
        print(f"消费者取出数据{data}")
    print("消费者进程结束")



if __name__=="__main__":
    # 创建进程安全队列
    queue=multiprocessing.Queue(maxsize=10)

    p1=multiprocessing.Process(target=producer,args=(queue,))
    c1=multiprocessing.Process(target=conusumer,args=(queue,))

    p1.start()
    c1.start()

    # 主进程要等待生产者进程结束
    p1.join()

    # 主进程要等待消费者进程结束
    c1.join()