import requests
from md5 import generateMD5
import json
from bs4 import BeautifulSoup as bsp
# class login
import data as d
import re


# from answerCode import answerCode

#
# url = "https://www.webturing.com/"
# # hd={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
# kkname = 'PHPSESSID'
# loc = ['submit.php', 'login.php', 'problem.php', 'status.php', 'wallet.php', 'admin/', 'postFunction.php']
# loc2 = ['modifyInfo.php']
# list = ['请先登录!', '今天已经签到过啦，赶紧去A题吧~', ]
# seg = [b'\xe8\xb4\xa6\xe5\x8f\xb7\xef\xbc\x9a', b'</legend>', b'(\'example\',', b')']

# u.status 登陆状态
# u.n 昵称
# u.s 学校
# u.c 班级
# # gender 0:♂ 1:♀
# u.g 性别
# u.e 邮箱
# u.b 生日
# u.cookie cookie值
# u.kk cookie内容
# u.id 登录名（学号
# u.pw 密码（md5密文
# u.u = u.id

class user:
    def __init__(self, id, pw):
        self.pw = pw
        # print(pw)
        if (self.pw == d.nonmd5):
            self.cookie = id
            self.kk = {d.kkname: self.cookie}
            self.idget = requests.get(d.url + d.loc[5] + d.loc2[0], cookies=self.kk).text
            # print(self.idget)
            soup = bsp(self.idget, "html5lib")
            # try:
            self.id = soup.legend.contents[0].split(d.seg[0])[1].strip()
            # print(self.id)
            # except:
            #     pass
        else:
            self.id = id
            self.getcookie()
        if self.status():
            self.info()
        # print(self.pw)
    def getcookie(self, ):
        # self.pw = pw
        # status状态码0:网络问题1:登陆失败2:未知错误3:登陆成功
        # 返回cookie
        loginfo = {'user_id': self.id, 'password': self.pw, 'submit': ''}
        cookie = requests.post(d.url + d.loc[1], data=loginfo).headers
        # print(cookie)
        cookie = cookie['Set-Cookie']
        self.cookie = cookie.split('=')[1].split(';')[0]
        self.kk = {d.kkname: self.cookie}
        # if (self.status()):
        #     self.__init__(self.id, self.cookie)

    def status(self):
        s = requests.get(d.url + d.loc[5], cookies=self.kk).text
        status = len(s.split(self.id))
        # print(status)
        if (status == 3):
            status = True
        else:
            status = False
        # if ((not status) and hasattr(self, 'pw')):
        #     self.getcookie(self.id, self.pw)
        return status

    def info(self):
        self.idget = requests.get(d.url + d.loc[5] + d.loc2[0], cookies=self.kk).text
        # 注释部分用bs4脱裤子放屁
        # soup = bsp(idget, "html5lib")
        # self.id = soup.legend.contents[0].split(d.seg[0])[1].strip()
        # print(legend)
        # info = soup('script')
        # info = info[len(info) - 1].string
        # self.id = idget.split(d.seg[0])[1].split(d.seg[1])[0].strip()
        info = json.loads(self.idget.split(d.seg[2])[1].split(d.seg[3])[0])
        # print(info)
        self.n = info['nick']
        self.s = info['school']
        self.c = info['class']
        # gender 0:♂ 1:♀
        self.g = info['gender']
        self.e = info['email']
        self.b = info['birthday']
        userinfoPage = requests.get(d.url + d.loc[8], params={'user': self.id}).text
        userinfoPage = bsp(userinfoPage, "html5lib")
        tag = userinfoPage.find('div', id="yijiejue")
        # it=tag.text
        # print(it)
        # print(type(it))
        # print(re.findall(re.compile(r'\d\d\d\d'), it))
        self.headled = re.findall(re.compile(r'\d\d\d\d'), tag.text)

    def postAnswer(self, answerCode):
        kv = {'id': answerCode.pid, 'language': answerCode.lang, 'source': answerCode.src}
        return requests.post(d.url + d.loc[0], cookies=self.kk, data=kv).text

    # def crash(self):
    #     self

if __name__ == '__main__':
    while True:
        uid = input("username or cookie:\n")
        pw = input("password:\n")
        # id = input("username")
        # pw = getpass("password")
        # cookie=input("cookie,可选填")
        # 添加正则判断
        # pass
        # if (pw==''):
        #     u=user(uid)
        # else:
        u = user(uid, generateMD5(pw))
        # u=user(id,"u1td2ikcu4lr4v8p8kk1lr2n22")
        if (u.status()):
            print('登陆成功')
            break
        else:
            print(u.status())
            print(u.pw, u.cookie)
            print('登陆失败')
    print(u.id)
    print(u.n)
    print(u.status())
    while 1:
        print("请输入指令用于调试")
        queue = input("")
        if (queue != 'end'):
            try:
                exec(queue)
            except:
                print("\"" + queue + "\"" + " 执行失败")
        else:
            break
