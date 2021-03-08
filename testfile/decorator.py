def base1(func):
    def warp(*args):
        print("now is 2 {}".format(func.__name__))
        func(*args)
    return warp

def base2(func):
    def warp():
        print("now is 1 {}".format(func.__name__))
        func()
    return warp

def keydec(time):
    def decor(func):
        def warp():
            print(time)
            func()
        return warp
    return decor

class animal:
    def __init__(self, func):
        self.age = 10
        self.ablity = func
    def bark(self):
        print("bark!")

import time

@base1
def tt(*args):
    print(type(args))

@animal
def people():
    print("im fee...")

if __name__ == "__main__":
    '''
    me = people
    print(me.age)
    me.ablity()
    me.bark()
    '''
    tt(1,2,3,4)

