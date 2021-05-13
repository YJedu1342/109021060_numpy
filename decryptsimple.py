import sys
import random as rand

if __name__ == '__main__':
    if len(sys.argv) > 1:
        rand.seed(sys.argv[1])#設定亂數種子
        encryptword = list(sys.argv[2])#設定欲解密之文字
        lenword = len(encryptword)
        encrynum = [0]*lenword
        for i in range(lenword):
            encrynum[i] = i
        decryptword = [0]*lenword
        rand.shuffle(encrynum)
        tmp = 0
        for i in encrynum:
            decryptword[i] = encryptword[tmp]
            tmp += 1
        print("".join(decryptword))
    else:
        print("缺少資料")