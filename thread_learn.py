# from time import ctime, sleep

# def func1():
# 	for i in range(5):
# 		print('func1: %d \n' %i)
# 		sleep(1)

# def func2():
# 	for j in range(5):
# 		print('func2: %d \n' %j)
# 		sleep(1)

# def main():
# 	print('start:', ctime())
# 	func1()
# 	func2()
# 	print('end:', ctime())

# if __name__ == '__main__':
# 	main()

# import thread
# from time import ctime, sleep

# def func1():
# 	for i in range(5):
# 		print('func1: %d \n' %i)
# 		sleep(1)

# def func2():
# 	for j in range(5):
# 		print('func2: %d \n' %j)
# 		sleep(1)

# def main():
# 	print('start:', ctime())
# 	thread.start_new_thread(func1, ())
# 	thread.start_new_thread(func2, ())
# 	sleep(5)
# 	print('end:', ctime())

# if __name__ == '__main__':
# 	main()

# import threading
# from time import ctime, sleep

# def func1():
# 	for i in range(10):
# 		print('func1: %d \n' %i)
# 		sleep(1)

# def func2():
# 	for j in range(10):
# 		print('func2: %d \n' %j)
# 		sleep(1)

# def main():
# 	print('start: ', ctime())
# 	t1 = threading.Thread(target=func1)
# 	t2 = threading.Thread(target=func2)
# 	t1.start()
# 	t2.start()
# 	t1.join()
# 	t2.join()
# 	print('end: ', ctime())

# if __name__ == '__main__':
# 	main()

# import threading
# from time import ctime, sleep

# def func1():
# 	for i in range(10):
# 		print('func1: %d \n' %i)
# 		sleep(1)

# def func2():
# 	for j in range(10):
# 		print('func2: %d \n' %j)
# 		sleep(1)
# class MyThread():
# 	def __init__(self, func):
# 		self.func = func
# 	def __call__(self):
# 		self.func()

# def main():
# 	print('start: ', ctime())
# 	t1 = threading.Thread(target=MyThread(func1))
# 	t2 = threading.Thread(target=MyThread(func2))
# 	t1.start()
# 	t2.start()
# 	t1.join()
# 	t2.join()
# 	print('end: ', ctime())

# if __name__ == '__main__':
# 	main()
import threading
from time import ctime, sleep

def func1():
	for i in range(10):
		print('func1: %d \n' %i)
		sleep(1)

def func2():
	for j in range(10):
		print('func2: %d \n' %j)
		sleep(1)
class MyThread(threading.Thread):
	def __init__(self, func):
		threading.Thread.__init__(self)
		self.func = func
	def run(self):
		self.func()

def main():
	print('start: ', ctime())
	t1 = MyThread(func1)
	t2 = MyThread(func2)
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print('end: ', ctime())

if __name__ == '__main__':
	main()