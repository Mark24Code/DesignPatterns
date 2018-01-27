'''
享元模式
英文是 Flyweight 轻量级选手
其实是专门针对节省内存用的一种设计模式

我个人猜测：享元，翻译的名字就想表达，（共）享（内存单）元 的意思吧

享元模式和单例模式很像，但是单例永远只返回一个实例。享元模式是要去返回已存在的多种类的实例。


适用于当有成百上千个相似对象的时候，将他们相同的特性，整合进一个享元中，可以极大减少对内存的消耗。
'''

class CarModel:
    '''
    记录汽车生产型号

    构建一个新的享元式，建立一个索引，如果存在就返回，如果没有就新建。
    这样共享内存。类似于JS的prototype。
    '''
    _models = dict()

    def __new__(cls,model_name, *args, **kwargs):
        model = cls._models.get(model_name)
        if not model:
            model = super().__new__(cls)
            cls._models[model_name] = model
        return model

    def __init__(self, model_name):
        self.model_name = model_name

t1 = CarModel('tesla')
bz = CarModel('benzi')
t2 = CarModel('tesla')

print(t1 is t2) #True 他们在内存中一样，其实他们是一样的对象。节省了内存。
print(t1 is bz) #False

t1.test = 'testName'
print(t1.test) # testName
print(t2.test) # testName
