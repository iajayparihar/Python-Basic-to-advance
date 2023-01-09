import threading 
import time 
import queue
class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter

    def run(self):
        print("Starting Table "+self.name)
        threadLock.acquire()
        table(self.counter)
        threadLock.release()

def table(counter):
    for i in range(1,11):
        print(counter * i,end=" ")
    print()

#__main__
threadLock = threading.Lock()
print("Main thread is Started. ")
for i in range(1,11,2):
    t1=myThread(i,"Thread:- "+str(i), i)
    t2=myThread(i+1,"Thread:- "+str(i+1), i+1)
    t1.start()
    t2.start()
    # t1.join()
    # t2.join()
print("Main thread exited...")

