import threading
import time
 

#starting joining threads
def task():
    print("thread is running")
 
t1=threading.Thread(target=task)
 
t1.start()
 
t1.join()
 
print('proccess completed')
 

#multithreadning
class mt(threading.Thread):
    def run(self):
        print(f"thread {self.name} is running")
 
t1=mt()
t2=mt()
t3=mt()
 
t1.start()
t2.start()
t3.start()
 
t1.join()
t2.join()
t3.join()

print("process completed")

#daemon threads
class dt(threading.Thread):
    def run(self):
        while True:
            print("daemon threat is running background")
            time.sleep(1)
            break
a=dt()
a.daemon=True
a.start()
 
time.sleep(2)
print("task completed")
 
#synchronization lock
class counter:
    def __init__(self):
        self.value=0
        self.lock=threading.Lock()
    def increment(self):
        for _ in range(100000):
            with self.lock:
                self.value+=1
c=counter()
t1=threading.Thread(target=c.increment)
t2=threading.Thread(target=c.increment)
 
t1.start()
t2.start()
t1.join()
t2.join()
 
print('final value',c.value)
 
#Deadlock of threaads
class dlt:
    def __init__(self):
        self.lock1=threading.Lock()
        self.lock2=threading.Lock()
    def task1(self):
        print("lock1 acqurie")
        self.lock1.acquire()
        print("task 1 completed")
        time.sleep(1)
        print("lock 2 is acquried")
        if self.lock2.acquire(timeout=2):
            print("task 1 completed")
            self.lock2.release()
        else:
            print("task 1 not reach lock 2 ")
        self.lock1.release()
    def task2(self):
         print("lock2 acqurie")
         self.lock2.acquire()
         print("task 2 completed")
         time.sleep(1)
         print("lock 1 is acquried")
         if self.lock1.acquire(timeout=2):
            print("task 2 completed")
            self.lock1.release()
         else:
            print("task 2 not reach lock 1 ")
         self.lock2.release()
d=dlt()
h1=threading.Thread(target=d.task1)
h2=threading.Thread(target=d.task2)
 
h1.start()
h2.start()
h1.join()
h2.join()
 
#Avoid of deadlocks
class adl:
    def __init__(self):
        self.lock1=threading.Lock()
        self.lock2=threading.Lock()
    def task1(self):
       with self.lock1:
           time.sleep(1)
           with self.lock2:
               print("task 1 complted")
    def task2(self):
        with self.lock1:
            time.sleep(1)
            with self.lock2:
                print("task 2 complted")
w=adl()
t1=threading.Thread(target=w.task1())
t2=threading.Thread(target=w.task2())
t1.start()
t2.start()
t1.join()
t2.join()
 
   
 