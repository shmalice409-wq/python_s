import threading
import time 

class MyThread(threading.Thread):
    def __init__(self, name, delay):
        super().__init__()
        self.name=name
        self.delay=delay
    
    def run(self):
        """线程的核心逻辑，start()自动启动
        """
        print(f"thread-{self.name} start")
        time.sleep(self.delay)
        print(f"thread-{self.name} end")
    
if __name__=="__main__":
    t1=MyThread('t1',2)
    t2=MyThread('t2',1)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print('process end')