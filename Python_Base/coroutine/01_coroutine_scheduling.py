import asyncio


async def sleep_demo():
    # 注意这里的异步函数中只能使用异步的休眠,不能使用
    print("start IO block 2s")
    await asyncio.sleep(2)
    print("2s wait end,recover coroutine")


"""这里的asyncio.run实际上是启动Eventloop,使得他去任务队列中不断地循环去遍历
如果发现有协程因IO阻塞,那么他就会进行调度,让另外的协程占用cpu,同时当IO结束的时候,会立刻唤醒被阻塞的协程"""
asyncio.run(sleep_demo())
