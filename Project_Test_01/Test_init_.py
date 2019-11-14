import time
def shwtime(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print('spend is {}'.format(end_time - start_time))
    return wrapper

@shwtime
def foo():
    print('foo..')
    time.sleep(1)

foo()

def shw(func):
    def wrapper():
        func()
        print("test")

    return wrapper

@shw
def f11():
    print(1111)

f11()

def f12(func):
    def f13():
        func()
        print("装饰函数")
    return f13

@f12
def faa():
    print("他是谁")


faa()
