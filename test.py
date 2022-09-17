import time
import pickle
print(time.ctime())

class Scene:
    def __init__(self,str='Hello World!'):
        self.info = str

    def getInfo(self):
        print(self.info)


fp = open('file.bin','wb')
info = Scene('Hello Dad!')
pickle.dump(info,fp)
fp.close()

f = open('file.bin','rb')
result = pickle.load(f)
result.getInfo()
f.close()


fp.close()