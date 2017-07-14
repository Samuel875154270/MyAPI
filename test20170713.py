import queue
import threading
import time


class ThreadPool(object):

    def __init__(self, max_num=20):
        self.queue = queue.Queue(max_num)
        for i in range(max_num):
            self.queue.put(threading.Thread)

    def get_thread(self):
        return self.queue.get()

    def add_thread(self):
        self.queue.put(threading.Thread)


def func(arg, p):
    print(arg)
    time.sleep(2)
    p.add_thread()


if __name__ == '__main__':
    pool = ThreadPool(5)

    for i in range(30):
        thread = pool.get_thread()
        t = thread(target=func, args=(i, pool))
        t.start()