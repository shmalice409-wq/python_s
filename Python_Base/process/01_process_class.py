import multiprocessing
import time

class MyProcess(multiprocessing.Process):
    def __init__(self,name,delayed):
        super().__init__()
        self.name=name
        self.delay=delayed
    
    def run(self):
        """进程核心逻辑，start()会调用该函数
        """
        print(f"自定义进程{self.name},启动PID：{self.pid}")
        time.sleep(self.delay)
        print(f"自定义进程{self.name}执行完毕")

    
if __name__=="__main__":
    p=MyProcess('zyyC',4)

    p.start()
    p.join()

    print("主进程结束")
