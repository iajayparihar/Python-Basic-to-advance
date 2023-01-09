import threading 
import time

class myThread (threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter
    def run(self):
        print("starting :- ",self.name)  #---------------------> +
        threadLock.acquire()
        print_Time(self.name,self.counter,3)
        threadLock.release()

def print_Time(threadName,delay,counter):
    while counter:
        time.sleep(delay)
        print("%s : %s"%(threadName,time.ctime(time.time())))
        counter-=1

#__main__
threadLock=threading.Lock()
threads_list=[]
thread1=myThread(1, "thread-1", 1)
thread2=myThread(2, "thread-2", 2)
thread1.start()
thread2.start()
threads_list.append(thread1)
threads_list.append(thread2)
for t in threads_list:
    t.join()
print("Exiting Main Thread.")