from usersql import sqltask
# from user import user


class answerCode:
    def __init__(self, pid, src, lang=0, ):
        self.pid = pid
        self.src = src
        self.lang = lang

    # def getCode(self, sid):
    #     self.kk = kk
    #     self.kv = {'id': sid}
    #     html = requests.get(d.url + d.loc[7], cookies=self.kk, params=self.kv).content

    def upCode(self, ):
        sqlupcode=sqltask()
        sqlupcode.upCode(self.pid,self.lang,self.src)
        sqlupcode.close()
    # def getCode(self):
    #     sqlgetcode=sqltask()
    #     sqlresult=sqlgetcode.getcode()
    #     sqlgetcode.close()
    #     return sqlresult
    # def postCode(self,user):
    #     self.key = requests.post(d.url + d.loc[0],
    #                              cookies=user.kk,
    #                              data=kv).text
    #     print()

if __name__ == '__main__':
    answerCodedemo=answerCode('0','demo','1')
    answerCodedemo.upCode()
