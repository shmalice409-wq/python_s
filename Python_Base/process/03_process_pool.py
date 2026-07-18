"""进程池
进程池和cpu核心数有关，创建多个进程，可以运行在多核心上面，当进程数大于核心数的时候，没有抢到cpu资源的进程会在进程队列中等待，直到有进程释放了资源
"""
import multiprocessing
import time

def claw_power(num):
    """计算平方，cpu密集型

    Args:
        num (int): 某个基数
    """
    ans=num**2
    print(f'计算结果为{ans}')
    time.sleep(0.5)
    return ans

if __name__=="__main__":
    # 获取cpu核心数，设置进程池大小
    core_count=multiprocessing.cpu_count()
    print(f'本机cpu核心数{core_count}')

    with multiprocessing.Pool(processes=core_count) as pool:
        """map 将要执行任务的函数和参数结合起来，交给进程池去调度
        """
        data_list=[1,2,3,4,5,6,7,8,9,10]
        # 这里map会自动分配任务，并阻塞主进程，等待全部任务完成，并返回结果列表
        result=pool.map(claw_power,data_list)
    
    print(result)