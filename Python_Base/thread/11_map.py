import time
from concurrent.futures import ThreadPoolExecutor


def calc(x):
    time.sleep(1)
    return x**x

if __name__=="__main__":
    data=[1,2,3,4,5,6]
    with ThreadPoolExecutor(max_workers=3) as pool:
        res=pool.map(calc,data)
        print(list(res))