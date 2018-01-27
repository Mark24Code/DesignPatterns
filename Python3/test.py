class A:
    pass

class B:
    def __new__(cls, *args, **kwargs):
        print('---B new----')
        print(args)
        print(kwargs)
        print('----B new end----')

        return super().__new__(cls)
    def __init__(self,name):
        print('----B init----')
        print(self)
        print(name)
        print('----B init end----')

b = B('atom')