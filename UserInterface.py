import time
import tkinter as tk
import login
import re
from tkinter import messagebox
import DataClean
import DataDisplay


class Login(object):
    def __init__(self):
        # 创建主窗口,用于容纳其它组件  
        self.root = tk.Tk()
        # 给主窗口设置标题内容  
        self.root.title("微博爬虫小程序")
        self.root.geometry('450x300')
        self.canvas = tk.Canvas(self.root, height=200, width=500)#创建画布  
        self.image_file = tk.PhotoImage(file='tim.gif')#加载图片文件  
        self.image = self.canvas.create_image(0,0, anchor='nw', image=self.image_file)#将图片置于画布上  
        self.canvas.pack(side='top')#放置画布（为上端）  

        # 创建一个'label'名为'微博账号' 
        self.label_account = tk.Label(self.root, text='微博账号: ')
        # 创建一个'label'名为'微博密码'  
        self.label_password = tk.Label(self.root, text='微博密码: ')
        # 创建一个'label'名为'目标微博'
        self.label_dest = tk.Label(self.root, text='目标微博: ')



        # 创建一个账号输入框,并设置尺寸
        self.input_account = tk.Entry(self.root, width=30)
        # 创建一个密码输入框,并设置尺寸  
        self.input_password = tk.Entry(self.root, show='*', width=30)
        # 创建一个目标微博输入框,并设置尺寸 
        self.input_dest = tk.Entry(self.root, width=30)

        # 创建一个登录系统的按钮  
        self.login_button = tk.Button(self.root,command =self.loginweibo , text = "爬取", width=10)
        # 创建一个退出系统的按钮  
        self.siginUp_button = tk.Button(self.root,command = self.quit, text = "退出", width=10)


    # 完成布局  
    def gui_arrang(self):
        self.label_account.place(x=60, y=170)
        self.label_password.place(x=60, y=195)
        self.label_dest.place(x=60, y=220)
        self.input_account.place(x=135, y=170)
        self.input_password.place(x=135, y=195)
        self.input_dest.place(x=135, y=220)
        self.login_button.place(x=140, y=260)
        self.siginUp_button.place(x=240, y=260)


    # 主程序退出函数
    def quit(self):
        self.root.destroy()

    # 登陆函数
    def loginweibo(self):
        username = self.input_account.get()
        password = self.input_password.get()
        uid = self.input_dest.get()
        #当密码和用户名正确时进行爬取
        if username and password is not None:
            if self.judge(username, password):
               self.crawler(username, password, uid)
            else:
                tk.messagebox.showerror(message='用户名或密码不符合规范')
        else:
            tk.messagebox.showerror(message='用户名或密码为空')


    # 用户名密码正则判断
    def judge(self, username, password):
        # 判断用户名密码是否合法！
        result_name = re.compile(r"(13|14|15|17|18)[0-9]{9}")
        result_nameMail = re.compile(r"/[\w-]+(\.[\w-]+)*@([\w-]+\.)+\w{2,14}/")
        result_password = re.compile(r"^[a-zA-Z]\w{6,18}")
        return result_name.match(username) or result_nameMail.match(username) and result_password.match(password)


    # 爬取函数
    def crawler(self,username,password,uid):
        login.loginWeibo(username, password)
        time.sleep(3)
        login.visitUserInfo(uid)
        result = login.visitWeiboContent(uid)
        if result:
            tk.messagebox.showinfo("爬取完毕！")
        chuli_result = DataClean.clean()
        if chuli_result:
            DataDisplay.word()



def main():
    # 初始化对象  
    L = Login()
    # 进行布局  
    L.gui_arrang()
    # 主程序执行  
    tk.mainloop()


