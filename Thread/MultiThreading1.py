import threading as td
import os

def task1():
    print("Task 1 assigned to thread:{}".format(td.current_thread().name))
    print("ID of process running task 1 : {}".format(os.getpid()))

def task2():
    print("Task 2 assigned to thread : {}".format(td.current_thread().name))
    print("ID of process running task 2 : {}".format(os.getpid()))
    

if __name__ == "__main__" :
    print("Main thread name :{}".format(td.current_thread().name))
    print("ID of process running main program : {}".format(os.getpid()))

    t1=td.Thread(target=task1,name="first")
    t2=td.Thread(target=task2,name="second")

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Done!!!")