"""Manager用于管理共享内存，但是共享内存会出现进程安全问题，需要使用锁"""
import multiprocessing
import time
""""""

def add_num(share_list,lock,num):
    """往共享内存中添加数

    Args:
        share_list (list): 共享列表，处于共享内存中
        lock (lock): 锁，防止进程安全问题
        num (int): 添加的数
    """
    lock.acquire()
    try:
        share_list.append(num)
        print(f'成功向共享内存中写入{num}')
    finally:
        lock.release()



if __name__=="__main__":
    manager=multiprocessing.Manager()
    share_list=manager.list()
    lock=multiprocessing.Lock()

    p_list=[]
    for i in range(5):
        p=multiprocessing.Process(target=add_num,args=(share_list,lock,i))
        p.start()
        p_list.append(p)
    
    for p in p_list:
        p.join()
    
    print(f'最终结果{share_list}')
