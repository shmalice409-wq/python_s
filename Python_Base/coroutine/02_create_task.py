import asyncio
import time


async def task(name, delay):
    print(f"task-{name} start, need to wait {delay}s. ")
    await asyncio.sleep(delay)
    print(f"task-{name} was executed.")
    return f"{name}-result"


async def main():
    start_time = time.time()

    t1 = asyncio.create_task(task("A", 3))
    t2 = asyncio.create_task(task("B", 1))

    res1 = await t1
    res2 = await t2
    total_time = time.time() - start_time

    print(f"total time is {total_time}. ")
    print(res1, res2)


asyncio.run(main())
