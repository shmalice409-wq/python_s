"""线程之间通讯的方式，event.set()发送信息唤醒等待线程 event.wait(timeout)阻塞线程 event.clear()重置"""
import threading
import time

event=threading.Event()

def wait_task():
    print('waiting...')
    event.wait()
    print('gain signal, working...')

def send_task():
    time.sleep(2)
    print('sending...')
    event.set()

if __name__=="__main__":
    t1=threading.Thread(target=wait_task)
    t2=threading.Thread(target=send_task)
    t1.start()
    t2.start()
    t1.join()
    t2.join()