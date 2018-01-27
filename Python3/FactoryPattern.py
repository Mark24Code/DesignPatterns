'''
工厂模式

工厂模式一般用在我们的一个系统根据配置
和平台的问题拥有多个实现的情况。
（个人经验Flask生成多个网站测试实例的时候，并且方便灵活配置）


'''


class App:
    def __init__(self):
        pass

    def config(self, config_dict):
        pass

    def install(self, ext):
        pass


def factory(config_dict):
    app = App()
    app.config(config_dict)
    app.install('some_extends')
    return app


test_app = factory({"model": "test"})
dev_app = factory({"model": "dev"})
