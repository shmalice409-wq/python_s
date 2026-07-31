import asyncio
import time


async def task(name, delay):
    print(f"task-{name} start, need to wait {delay}s. ")
    await asyncio.sleep(delay)
    print(f"task-{name} was executed.")
    return f"{name}-result"


async def main():
    start_time = time.time()

    """gather 上一节中我们对于创建的每个任务都使用await执行并等待任务完成,这里可以使用gather将任务放在一起"""
    result_list = await asyncio.gather(
        task("A", 5),
        task("B", 1),
        task("C", 3),
    )

    total_time = time.time() - start_time

    print(f"total time is {total_time}. ")
    print(result_list)


asyncio.run(main())
