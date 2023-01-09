import threading as td
import time 

class mythread(td.Thread):
    def __init__(self,threadID,name,counter):
        td.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter

    def run(self):
        print("Starting"+self.name)
        print_Time(self.name, 5 ,self.counter)
        print("Exiting:- "+ self.name)

exitFlag = 0
def print_Time(threadName,counter,delay):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s : %s"%(threadName,time.ctime(time.time())))
        counter -=1

# main 
thread1 = mythread(1, "Thread-1", 1)
thread2 = mythread(2, "Thread-2", 2)
thread1.start()
thread2.start()
print("main thread exited.")