#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

def my_abs(num):
	if num >= 0:
		return num
	else:
		return -num
a = my_abs(-99)
print(a)
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[-2: -1])
d = {'a': 1, 'b': 2, 'c': 3}
for key, v in d.items():
	print(key, v)
print([x * x for x in range(1, 11)])

classmates = ['Michael', 'Bob', 'Tracy']
print(classmates[-1])
# 杨辉三角形
def triangles():
	N = [1]
	while True:
		yield N
		N.append(0) #尾部加一个零
		print(N)
		N = [N[i - 1] + N[i] for i in range(len(N))]

n = 0
for t in triangles():
	print(t)
	n = n + 1
	if n == 10:
		break
def f(x):
	return x * x
print(list(map(f, [1, 2, 3, 4, 5, 6, 7])))

def add(x, y):
	return x + y
s = reduce(add, [1, 2, 3, 4, 5, 6, 7])
print(s)

# 闭包
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
# 匿名函数
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('2015-3-25')
now()

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))
bart = Student('sunny', 99)
bart.print_score()
