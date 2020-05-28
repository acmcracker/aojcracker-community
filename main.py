# import execjs
from user import user
from post import post as p
import time
from md5 import generateMD5
# from getpass import getpass
from get import get
def threadhb(user):
    while user.status():
        time.sleep(3)
    
if __name__ == '__main__':
    # new file log (include cookie)
    # log=file()
    # # file
    # login
    print("登录方式：\n"
          "使用cookie方式密码请留空"
          "输错后会提示重新输入"
          "")
    while True:
        id = input("username or cookie :\n")
        pw = input("password:\n")
        # cookie=input("cookie,可选填")
        u = user(id, generateMD5(pw))
        if (u.status()):
            print('登陆成功')
            break
        else:
            print('登陆失败,请重新登录')

    # hearbeat start  /sign start
    # hearbeat thread / sign thread process
    # try:
    print("请确认登录信息")
    print("用户名："+u.n)
    print("用户须知：\n"
          "1.该程序不会保留您的密码\n"
          "2.该程序将尝试获取您的所有正确题解并上传至数据库\n"
          "3.上传过程根据您的提交量约需要10分钟左右不等"
          "4.社区版本（communtiy）可自动为您提交数据库中题号<=1500的所有可能题解\n"
          "5.所有过程均不会消耗或提供图灵币（大概）\n"
          "6.由于aoj问题答题间隔为4秒，整个过程不会超过半个小时")
    while eval(input("请输入1确认信息，或直接关闭窗口\n"))==1:
        break

    post = p(u)
    # print(post.sign())
    geth=get(u)
    print("")
    geth.getAnswer()
    post.postAnswer()
    # # threading
    # get info
    # get user's answer
    # download and upload user's codeAnswer thread start
    # # mysql
    # user opearte:
    # 1. check info
    # 2. auto finish ac
    # 3. exit
    # # finish
    # while 1:
    #     print("请输入指令用于调试")
    #     queue = input("")
    #     if(queue!=end):
    #         try:
    #             exec(queue)
    #         except:
    #             print("\"" + queue + "\"" + " 执行失败")
    #     else:
    #         break