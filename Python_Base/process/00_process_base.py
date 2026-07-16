import multiprocessing
import time

"""进程的执行需要执行任务，首先定义一个任务"""

def task(name,delay):
    """ 子进程执行函数

    Args:
        name (_type_): 子进程名称
        delay (_type_): 睡眠时间
    """
    print(f"子进程名称{name},子进程PID{multiprocessing.current_process().pid}")

    time.sleep(delay)

    print(f"子进程{name}执行完毕")

print(f"进程PID{multiprocessing.current_process().pid}")


if __name__ == "__main__":
    """这里我使用的是linux,linux创建进程使用的是fork。
    fork会复制当前进程内存，而不是重新加载，所以在子进程中，会直接调用task,而不是重新加载一遍整个的.py文件。
    而windows使用的是spawn,这个创建子进程的时候会重新完整地倒入整个py文件"""
    #multiprocessing.set_start_method("spawn")
    print(f"主进程启动，主进程PID为{multiprocessing.current_process().pid}")

    p1=multiprocessing.Process(target=task,args=("p1",2))
    p2=multiprocessing.Process(target=task,args=("p2",1))

    """python这里还提供了terminate强制杀死子进程，is_alive判断子进程是否存活"""
    p1.start()
    p2.start()

    """python这里如果不join，那么主进程将会跑完就结束退出"""
    print("主进程执行完毕")