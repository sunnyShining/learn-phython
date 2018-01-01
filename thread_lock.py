# import threading
# from time import sleep

# tickets = 100

# class Window(threading.Thread):
# 	def __init__(self, n, lock):
# 		self.lock = lock
# 		threading.Thread.__init__(self, name = n)

# 	def take(self):
# 		global tickets
# 		while tickets >= 1:
# 			# self.lock.acquire()
# 			# print('%s : %d' % (threading.currentThread().name, tickets))
# 			# tickets = tickets - 1
# 			# self.lock.release()
# 			with self.lock:
# 				print('%s: %d' % (threading.currentThread().name, tickets))
# 				tickets = tickets - 1
# 			sleep(1)
# 	def run(self):
# 		self.take()

# def main():
# 	lock = threading.Lock()
# 	for i in range(1, 5):
# 		name = 'w' + str(i)
# 		w = Window(name, lock)
# 		w.start()

# if __name__ == '__main__':
# 	main()

from threading import Thread, BoundedSemaphore, Lock
from time import ctime, sleep
from random import randrange
from atexit import register

lock =Lock()
MAX = 10

bs = BoundedSemaphore(MAX)

class Consumer(object):
    def get(self):
        lock.acquire()
        print('取出')
        if bs.acquire(False):
            print('OK')
        else:
            print('空的，等等。。。')
        lock.release()
    def consume(self):
        for i in range(10):
            self.get()
            sleep(randrange(3))
    
    def __call__(self):
        self.consume()

class Producer(object):
    def put(self):
        lock.acquire()
        print('放入')
        try:
            bs.release()
        except ValueError:
            print('满的，等等')
        else:
            print('OK')
        lock.release()
    def produce(self):
        for i in range(15):
            self.put()
            sleep(randrange(3))
    def __call__(self):
        self.produce()

@register
def _asdict():
    print('end at: ', ctime())

def main():
    print('start at:', ctime())
    consumer = Consumer()
    producer = Producer()

    Thread(target=consumer).start()
    Thread(target=producer).start()

if __name__ == '__main__':
    main()


