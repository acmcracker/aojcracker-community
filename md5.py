import hashlib

def generateMD5(str):
    hl=hashlib.md5()
    hl.update(str.encode(encoding='UTF-8'))
    return hl.hexdigest()
if __name__ == '__main__':
    str=input("input string")

    print(type(generateMD5(str)))