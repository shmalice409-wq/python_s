import threading
import time


def task():
    time.sleep(3)


t = threading.Thread(target=task)
print("before start thread is_alive ?", t.is_alive())
t.start()
print("after start thread is_alive ?", t.is_alive())
print("current thread name:", threading.current_thread().name)
print("alive thread number", threading.active_count())
print("active thread list:", threading.enumerate())
t.join()
print("after end thread is_alive ?", t.is_alive())
