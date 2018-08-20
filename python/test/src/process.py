
import time
from multiprocessing import Process, Queue


def f(q):
    x = q.get()
    print("Process number %s,sleeps for %s seconds." % (x, x))
    time.sleep(x)
    print("Process number %s finished!" % x)


q = Queue()
for i in range(10):
    q.put(i)
    i = Process(target=f, args=[q])
    i.start()

if __name__ == '__main__':
    print("main process joins on queue")
    i.join()
    print("main finished!")
