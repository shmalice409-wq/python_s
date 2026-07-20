import threading
import time

def task(name,delay):
    """线程执行任务

    :param name: 线程名称
    :param delay: 休眠时间
    """
    print(f'线程{name}启动，休眠{delay}s')
    time.sleep(delay)
    print(f'thread-{name} end')

if __name__=="__main__":
    t1=threading.Thread(target=task,args=('A',4))
    t2=threading.Thread(target=task,args=('B',2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print('all thread end')

