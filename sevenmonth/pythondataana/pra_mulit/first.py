# coding=utf8
from multiprocessing import Process, Queue
import threading
import time

def addtoqueue(q):
    for i in range(0,100,1):
        print 'put.....', i
        q.put(i)
        time.sleep(0.2)


def read(q):
    while True:
        v = q.get(True)

        print 'get.....................', v


lock = threading.Lock()
def testlock(info_list, n):
    lock.acquire()
    info_list.append(n)
    lock.release()
    print ('%s\n' % info_list)


if __name__ == '__main__':
    info = list()

    for i in range(0, 10, 1):
        p = Process(target=testlock, args=[info, i])
        p.start()
        p.join()


    time.sleep((5))
    print '-'*10, 'threading', '_'*10
    for i in range(10):
        p = threading.Thread(target=testlock, args=[info, i])
        p.start()
        p.join()


'''

if __name__ == '__main__':

    q = Queue()
    pw = Process(target=addtoqueue, args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    pr.start()

    pr.join()

    pr.terminate()
'''