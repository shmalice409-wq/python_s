import threading

lock=threading.Lock()

num=0
def add_num():
    global num
    for _ in range(1233):
        with lock:
            num+=1

if __name__=="__main__":
    t1=threading.Thread(target=add_num)
    t2=threading.Thread(target=add_num)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print('final answer',num)