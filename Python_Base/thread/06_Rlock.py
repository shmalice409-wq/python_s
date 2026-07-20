import threading

rlock=threading.RLock()

def task():
    rlock.acquire()
    print('first lock success')
    rlock.acquire()
    print('second lock success')
    rlock.release()
    rlock.release()

t=threading.Thread(target= task)
t.start()
t.join()