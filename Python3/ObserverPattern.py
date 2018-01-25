'''
观察者模式

也叫做发布订阅模式


实现方式有很多种
可以基于注册（下面例子）
也可以基于事件

一个状态变化，通知所有订阅者
'''

class Inventory:
    def __init__(self):
        self.observers = []
        self._product = None

    def attach(self,observer):
        self.observers.append(observer)

    @property
    def product(self):
        return self._product
    @product.setter
    def product(self,value):
        self._product = value
        self._broadcast_all_observers()

    def _broadcast_all_observers(self):
        for observer in self.observers:
            observer()

class Observer:
    def __init__(self,name,inventory):
        self.name = name
        self.inventory = inventory

    def __call__(self):
        print("{}收到{}".format(self.name,self.inventory.product))

#发布者
i = Inventory()
#订阅者
o1 = Observer('o1',i)
o2 = Observer('o2',i)
o3 = Observer('o3',i)
#发布者添加订阅人
i.attach(o1)
i.attach(o2)
i.attach(o3)
#发布者添加product，订阅人会收到消息
i.product='Apple'