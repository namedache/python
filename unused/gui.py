import easygui as a
import login

errmsg = '[*微博账号]为必填项。\n \n [*目标微博地址]为必填项。\n \n [*微博密码]为必填项.'
Msg = "欢迎光临微博爬虫"
Title = "爬虫小程序"
input_value = []
Fileds = ['*微博账号', '*目标微博地址', '*微博密码']
input_value = a.multpasswordbox(Msg, Title, Fileds)

while True:
    if input_value == None:
        break
    errmsg = ""
    for i in range(len(input_value)):
        option = Fileds[i].strip()
        if option[0] == "*" and input_value[i].strip() =="":
            errmsg += ("【%s】为必填项\n"%Fileds[i])
    a.msgbox(errmsg, ok_button="好的")
    login.loginWeibo(input_value[0],input_value[2])
    if errmsg == "":
        break
    else:
        input_value = a.multpasswordbox("欢迎光临微博爬虫", "爬虫小程序", ['*微博账号', '*目标微博地址', '*微博密码'])




