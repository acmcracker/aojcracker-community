import requests
# from login import user
import data as d
from user import user
from answerCode import answerCode
from usersql import sqltask
import time
# 提交请求
class post:
    def __init__(self, user):
        self.u = user

    ## 提交题目
    #
    def postAnswer(self, ):
        # self.id=
        # if ( == None):
        #     self.cid = cid
        #     self.pid = pid
        #     kv = {'cid': self.cid, 'pid': self.pid, 'language': self.lang, 'source': self.src}
        # else:
        #     kv = {'id': self.id, 'language': self.lang, 'source': self.src}
        sqlgetcode = sqltask()
        sqlresult = sqlgetcode.getcode()
        sqlgetcode.close()
        # print(sqlresult)
        if sqlresult is not None:
            for row in sqlresult:
                try:
                    time.sleep(4)
                    answer=answerCode(row[0], row[2], row[1])
                    print("正在为您提交题解，题交编号为"+self.u.postAnswer(answer))
                except:
                    # print(row + "Err")
                    pass
    ## 签到
    def sign(self, ):
        self.str = requests.post(d.url + d.loc[6],
                                 cookies=self.u.kk,
                                 params={'action': 'sign'}).text
        # if (self.str == re.compile(d.list[0])):
        #     self.result = 0
        # elif (self.str == re.compile(d.list[1])):
        #     self.result = 2
        # else:
        #     self.result = 1
        # print(self.str)
        return self.str


if __name__ == '__main__':
    # cookie = input("")
    # id = input("")
    # pw = input("")
    id=''
    pw=''
    u = post(user(id, pw))
    print(u.sign())
    u.postAnswer()
    while 1:
        print("请输入指令用于调试")
        queue = input("")
        if (queue != end):
            try:
                exec(queue)
            except:
                print("\"" + queue + "\"" + " 执行失败")
        else:
            break
            

