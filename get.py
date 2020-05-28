import data as d
from user import user
from bs4 import BeautifulSoup as bsp
import re
import bs4
from answerCode import answerCode


class get:
    def __init__(self, user):
        self.u = user

    def getAnswer(self, ):
        kv = {'problem_id': '',
              'user_id': self.u.id,
              'language': '-1',
              'jresult': '4',
              'page': '1'}
        r = requests.get(d.url + d.loc[3], cookies=self.u.kk, params=kv).text
        # print(type(r))
        # print(r)
        # r=r.split('table')
        # r=r[len(r)-1]
        # # get max page num
        pageNum = r.split(d.seg2[0])
        pageNum = pageNum[len(pageNum) - 1]
        pageNum = eval(pageNum.split(d.seg2[1])[0])
        # print(pageNum)
        # # get sid
        # for i in range(1,pageNum):
        # kv['page']=i
        soap = bsp(r, "html5lib")  # html.parser 解析器不好用
        # print(soap.tbody.contents)
        # text=soap.tbody.contents
        # print(soap.tr)
        # print(soap.tr.next_sibling)
        # tag=soap.tbody.children
        # print(type(soap.tbody.children))
        # cnt=0
        for page in range(1,pageNum):
            kv = {'problem_id': '',
                  'user_id': self.u.id,
                  'language': '-1',
                  'jresult': '4',
                  'page': page}
            r = requests.get(d.url + d.loc[3], cookies=self.u.kk, params=kv).text
            soap = bsp(r, "html5lib")
            for tag in soap.tbody.contents:
                # tagsoap=soap
                if (isinstance(tag, bs4.element.Tag)):
                    # tag=bsp(str(tag,encoding='UTF-8'))
                    # print(tag.tr)
                    # print(next(tag.strings))
                    # elelist=[]
                    # for tagele in tag.strings:
                    #     elelist.append(tagele)
                    # # cnt+=1
                    #     print(repr(tagele))
                    # print(tag.find_all("td"))
                    #
                    # print(tag.find(target="_blank"))
                    # print(tag.find('a',href=re.compile(d.loc[2])).string)# 题号
                    # print(tag.find('a',href=re.compile(d.loc[7])).string)# 语言
                    decodesoap = requests.get(d.url + d.loc[7],
                                              cookies=self.u.kk,
                                              params={'id': next(tag.strings)}).text
                    decodesoap = bsp(decodesoap, "html5lib")
                    pid = eval(tag.find('a', href=re.compile(d.loc[2])).text)
                    lang = tag.find('a', href=re.compile(d.loc[7])).text
                    lang = d.lang.index(lang)
                    src = decodesoap.code.text
                    # print(src)
                    # print(lang)
                    codeget=answerCode(pid,src,lang)
                    codeget.upCode()
            # else:
            #     pass
        # print(cnt)
        # output

    def getcode(self):
        pass


if __name__ == '__main__':
    uid=input("username:\n")
    pw=input("password:\n")
    u = user(uid,pw)
    getObj = get(u)
    getObj.getAnswer()
