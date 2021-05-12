import sys
import random as rand

if __name__ == '__main__':
    if len(sys.argv) > 1:
        dict_1 = {}
        rand.seed(sys.argv[1]) #設定亂數種子
        wordlist = list(sys.argv[2])
        #根據字串長度建立數字list
        lenword = len(wordlist)
        encrynum = [0] * lenword
        for i in range(lenword):
            encrynum[i] = i

        rand.shuffle(encrynum)#打亂數字
        #根據打亂後的數字對應文字
        #wordencry為加密後
        wordencry = [0] * lenword
        tmp = 0 
        for i in encrynum:
            wordencry[tmp] = wordlist[i]
            tmp += 1
        
        worddecry = [0] * lenword
        tmp = 0
        for i in encrynum:
            worddecry[i] = wordencry[tmp]
            tmp += 1

        print(encrynum)
        print(wordencry)
        print(worddecry)
    else:
        print("缺少資料")