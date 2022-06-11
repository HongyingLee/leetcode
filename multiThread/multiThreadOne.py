import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, ThreadID, name, counter):
        threading.Thread.__init__(self)
        self.ThreadID = ThreadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Start thread : {0}".format(self.name))
        threadLock.acquire()
        printTime(self.name, self.counter, 5)
        threadLock.release()
        print("ExitThread : {0}".format(self.name))


def printTime(threadName, delay, counter):
    while counter:
        if exitFlag:
            (threading.Thread).exit()
        time.sleep(delay)
        print("{0} : {1}".format(threadName, time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()
threads = []

thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()
    print("Exit thread")
