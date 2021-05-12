import sys
import random as rand

if __name__ == '__main__':
    if len(sys.argv) >2:
        seedvalu = sys.argv[1]
        data = list(sys.argv[2])
        rand.seed(seedvalu)
        print(data)
        rand.shuffle(data)
        print("".join(data))
        datareshuffle = [0] * len(data)
        for i in range(len(datareshuffle)):
            datareshuffle[i]=i
        print(datareshuffle)
        rand.shuffle(datareshuffle)
        print(datareshuffle)
        data2 = [0] * len(datareshuffle)
        for i in range(len(data2)):
            data2[i] = data[int(datareshuffle[i])]
        print("".join(data2))
    else:
        print("資料不足")