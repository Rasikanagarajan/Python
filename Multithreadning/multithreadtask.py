import threading
import time

class MyThread(threading.Thread):
    def run(self):
        print(f"thread {self.name} is running")

threads = [MyThread(), MyThread(), MyThread()]

threads[0].start()
threads[1].start()
threads[2].start()

threads[0].join()
threads[1].join()
threads[2].join()

print("process completed")



class dlt:
    def __init__(self):
        self.mark1 = threading.Lock()
        self.mark2 = threading.Lock()
        self.mark3 = threading.Lock()

    def mk1(self):
        print("mark1 acquire")
        self.mark1.acquire()
        print("mk1 completed")
        time.sleep(1)

        print("mk1 is acquire")
        if self.mark2.acquire(timeout=2):
            print("mk1 completed")
            self.mark2.release()
        else:
            print("mk1 not reach mark2")

        self.mark1.release()

    def mk2(self):
        print("mark2 acquire")
        self.mark2.acquire()
        print("mk2 completed")
        time.sleep(1)

        print("mark1 is acquire")
        if self.mark1.acquire(timeout=2):
            print("mk2 completed")
            self.mark1.release()
        else:
            print("mk2 not reach mark1")

        self.mark2.release()

    def mk3(self):
        print("mark3 acquire")
        self.mark3.acquire()
        print("mk3 completed")
        time.sleep(1)

        print("mark2 is acquire")
        if self.mark2.acquire(timeout=2):
            print("mk3 completed")
            self.mark2.release()
        else:
            print("mk3 not reach mark2")

        self.mark3.release()


d = dlt()
h1 = threading.Thread(target=d.mk1)
h2 = threading.Thread(target=d.mk2)
h3 = threading.Thread(target=d.mk3)

h1.start()
h2.start()
h3.start()

h1.join()
h2.join()
h3.join()