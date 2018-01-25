'''
装饰器模式
'''

def dosth(func):
    def wrapper(*args,**kwargs):
        print('do sth.')
        return func(*args,**kwargs)
    return wrapper

def test1():
    print('test1 called')

test1 = dosth(test1)

test1()