'''
单例模式

永远只返回一个对象

使用__new__

__init__不是Python对象的构造方法,__init__只负责初始化实例对象,在调用__init__方法之前,会首先调用__new__方法生成对象,可以认为__new__方法充当了构造方法的角色。所以可以在__new__中加以控制,使得某个类只生成唯一对象。具体实现时可以实现一个父类,重载__new__方法,单例类只需要继承这个父类就好。
'''


class Singleton:
    _singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super().__new__(cls, *args, **kwargs)
        return cls._singleton

if __name__=='__main__':
    s1 = Singleton()
    s2 = Singleton()
    print(s1 is s2)