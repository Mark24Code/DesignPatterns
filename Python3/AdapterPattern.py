'''
适配器模式

被设计用于已存在的代码进行交互。
适配器用于允许两个已存在的对象在一起工作，即使他们的接口不兼容

类似于包裹性质的函数，传入参数A，内部转化为B传给接口
使用方式更加灵活，类，继承，函数均可，或者给类增加方法

'''
from datetime import date

class AgeCalculator:
    '''
    已存在接口
    使用字符串作为输入
    '''
    def __init__(self, birthday):
        self.year, self.month, self.day = (int(x) for x in birthday.split('-'))

    def calculate_age(self,date):
        year, month, day = (int(x) for x in date.split('-'))
        age = year-self.year
        if (month, day) < (self.month, self.day):
            age -= 1
            return age

class DateAgeAdapter:
    ''''
    适配器
    目标是为了改进时间的输入
    '''
    def _str_date(self, date):
        return date.strftime("%Y-%m-%d")

    def __init__(self, birthday):
        '''
        这里引用了存在接口的类
        甚至可以在这里做更多的工作，
        连接多个类

        包裹了一层去工作。
        :param birthday:
        '''
        birthday = self._str_date(birthday)
        self.calculator = AgeCalculator(birthday)

    def get_age(self, date):
        date = self._str_date(date)
        return self.calculator.calculate_age(date)






a=AgeCalculator('1991-09-24')
print(a.calculate_age('2018-1-27'))

b=DateAgeAdapter(date(1991,9,24))
print(b.get_age(date.today()))