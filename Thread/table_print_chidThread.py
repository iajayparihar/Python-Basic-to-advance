import threading 
class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter

    def run(self):
        print("Starting Table "+self.name)
        threadLock.acquire(timeout=10)
        table(self.counter)
        threadLock.release()


def table(counter):
    for i in range(1,11):
        print(counter * i,end=" ")
    print()


#__main__
threadLock = threading.Lock()
print("Main thread is Started. ")

for i in range(2,11):
    t1=myThread(i,"Thread :-"+str(i), i)
    t1.start()
    t1.join()


