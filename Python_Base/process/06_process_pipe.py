"""pipe管道通讯，双向通讯，点对点"""

import multiprocessing

def pipe_child(child_con):
    """管道子进程
    这里需要注意，如果双方都没有发送消息，却都在等待消息，那么直接阻塞
    :param child_con: 孩子pipe对象
    """
    print("子进程收到",child_con.recv())
    child_con.send('子进程消息1')
    #print("子进程收到",child_con.recv())
    child_con.close()




if __name__=="__main__":
    parent_con,child_con = multiprocessing.Pipe()

    p=multiprocessing.Process(target=pipe_child,args=(child_con,))
    p.start()

    print('主进程受到信息',parent_con.recv())
    parent_con.send('主进程发送的信息1')
    p.join()