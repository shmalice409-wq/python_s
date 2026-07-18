"""使用apply_async来进行异步非阻塞获取结果"""
import multiprocessing
import time

def task(x):
    """计算一个数的10倍

    Args:
        x (int): 传入的参数
    """
    time.sleep(0.5)
    return x * 10

if __name__=="__main__":
    with multiprocessing.Pool(3) as pool:
        tasks=[]#任务结果列表
        for i in range(5):
            async_ans=pool.apply_async(task,args=(i,))# 异步提交进程，但是此时进程不等待运行出结果，而是返回一个异步结果对象<multiprocessing.pool.ApplyResult object at 0x7fa0d4f1a410>，并保存到tasks中，此时我们那不到结果。
            print(async_ans)
            tasks.append(async_ans)
        #这里get取数据的时候阻塞的，等拿到结果后才结束
        result=[res.get() for res in tasks]
    print(f"所有结果{result}")