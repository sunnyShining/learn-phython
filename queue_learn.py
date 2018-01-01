from threading import Thread
from time import  sleep
from random import randint
from queue import Queue

class Consumer(object):
    def __init__(self, q):
        self.q = q
    def get(self):
        print('从Q取对象。。。')
        self.q.get(1)
        print('当前Q大小： %d' % self.q.qsize())
    def consume(self):
        for i in range(10):
            self.get()
            sleep(randint(2, 5))
    
    def __call__(self):
        self.consume()

class Producer(object):
    def __init__(self, q):
        self.q = q
    def put(self):
        print('为Q添加对象。。。')
        self.q.put('xxx', 1)
        print('当前Q大小： %d' % self.q.qsize())
    def produce(self):
        for i in range(10):
            self.put()
            sleep(randint(2, 5))
    def __call__(self):
        self.produce()

def main():
    q = Queue(32) #创建一个队列
    consumer = Consumer(q)
    producer = Producer(q)

    t1 = Thread(target=consumer)
    t1.start()
    t2 = Thread(target=producer)
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()