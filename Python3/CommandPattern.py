'''
命令模式

常见于GUI操作中，一个操作，可以被 菜单栏，快捷键，工具栏图标所调用。
实际发生的动作，Exit，Save,Copy都有CommandInterface 实现。

GUI窗口接收到退出指明，文档收到保存指令。

命令模式的构成：
client 客户：一个实例化的对象
    |
invoker 调用者：决定哪个方法被调用
    |
receiver 接受者：实际命令的执行者
'''


class KeyboardShortcut:
    '''
    client 客户
    '''

    def keypress(self):
        self.command()


class Document:
    '''
    receiver 接受者，实际执行
    '''

    def __init__(self, filename):
        self.filename = filename
        self.contents = 'this is test file'

    def save(self):
        with open(self.filename, 'w') as file:
            file.write(self.contents)


class SaveCommand:
    '''
    invoker 调用者
    '''

    def __init__(self, document):
        self.document = document

    def __call__(self):
        self.document.save()


# 这里能够把对象的命令给取出，然后交给客户者在某一时刻调用
document = Document('test.txt')
shortcut = KeyboardShortcut()
save_command = SaveCommand(document)
shortcut.command = save_command
