'''
外观模式

为拥有多个组件的复杂系统提供简单接口。

做一件事情非常复杂，涉及到多方组件。但是这件事情，相当常见，为了避免每次都是
去操作繁杂的底层。决定封装出简单的接口。

举个例子，发送邮件，涉及的底层库相当多，而且又是常见的操作。

那么我们就可以抽象和设计出一个类，来整合这种操作
'''

import smtplib
import imaplib

class EmailFacade:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

    def send_email(self, to_email, subject, message):
        '''
        外观模式就是在这里整合多组件细节
        只提供一个简洁的接口

        虽然底层调用相当多的库和交互，但是他又是固定的。
        我们丝毫不关系。

        我们只要知道，这是发送邮件的就好了
        :param to_email:
        :param subject:
        :param message:
        :return:
        '''
        # stamp 复杂细节
        pass


    def get_inbox(self):
        # imaplib 复杂的细节
        pass