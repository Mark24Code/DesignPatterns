'''
策略模式

函数A和 对象B
函数A接收B的参数，采取不同的工作方式
但是又想避免在A中复杂 if-else，和强耦合
因为如果你想要增加 B的类型就要去修改 A中if-else的判断链


下面以只做壁纸作为例子

可以看到，主要是约定接口实现

这样，A只要负责调起统一的接口
参数自身完善自己要做的事情

不需要 if-else

很像鸭子类型
'''


class TiledStrategy:
    def make_background(self):
        print("平铺策略")

class ScaledStrategy:
    def make_background(self):
        print("放缩策略")

class CenteredStrategy:
    def make_background(self):
        print("居中策略")


class SysBackground:
    def __init__(self):
        pass

    def set_bg(self,strategy):
        strategy.make_background()

ts = TiledStrategy()
ss = ScaledStrategy()
cs = CenteredStrategy()

sysbg = SysBackground()
sysbg.set_bg(ts)