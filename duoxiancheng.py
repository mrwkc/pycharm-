import threading
import time

class myThread(threading.Thread):
    def __init__(self,name,delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print("Starting "+self.name+'\n')
        print_time(self.name,self.delay)
        print('Exiting'+self.name)

def print_time(threadNmae,delay):
    counter = 0
    while counter < 3:
        time.sleep(delay)
        print(threadNmae,time.ctime())
        counter +=1

threads =[]

thread1 = myThread('线程1',1)
thread2 = myThread('线程2',2)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()

print('结束主线程')