import threading
import time

def daemon_task():
    while True:
        print('daemon running....')
        time.sleep(1)

def normal_task():
    time.sleep(3)
    print('normal thread end')

if __name__=='__main__':
    t1=threading.Thread(target=daemon_task,daemon=True)
    t2=threading.Thread(target=normal_task)

    t1.start()
    t2.start()

  
    t2.join()
    print('main end,daemon thread destory')
