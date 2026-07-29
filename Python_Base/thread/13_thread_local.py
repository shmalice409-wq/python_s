import threading

local_data = threading.local()


def func(S):
    """这里主要是为了体现local的作用:
    local可以为每一个线程创建独立的变量

    :param S: 线程名
    """
    local_data.value = S
    print(f"thread name{S}:local_data={local_data.value}")


if __name__ == "__main__":
    t1 = threading.Thread(target=func, args=("q",))
    t2 = threading.Thread(target=func, args=("s",))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
