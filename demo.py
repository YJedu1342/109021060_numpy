import numpy as np

#a = np.array([1,2,3,4])
#print(a)
#b = np.array([(2.5,1,3,4.5),(5,6,7,8)],dtype=float)
#print(b)
#c = np.array([[(2.5,1,3,4.5),(5,6,7,8)],[(2.5,1,3,4.5),(5,6,7,8)]],dtype=float)
#print(c)
#np.zeros((2, 3))               # 建立一個2x3全為0的陣列
#np.ones((2, 3, 4))             # 建立一個2x3x4全為1的陣列
#x = np.ones((2, 3, 3)) * 128 \ print(x) ->同full
#np.arange(1, 10, 2)            # 建立一個由1開始，不超過10，間隔值為2的均勻數值陣列
x = np.linspace(0, 10, 5)          # 建立一個0到10之間，均勻的5個數值陣列
#np.full((3,2), 8)              # 建立一個3x2全為8的陣列
#np.eye(2)                      # 建立一個5x5的單位矩陣
#np.random.random((2,3))        # 建立一個2x3的隨機值矩陣
#x = np.random.randint(2,135,(2,3))# 建立一個2x3，數字數值介於2~135的隨機值矩陣
print(x)
#z = x.reshape(1,6)#將陣列重構成1x6的矩陣
#print(z)
#z.sort()
#print(z)

filename = "numpydemoout1.npy"
#with open(filename,"wb") as fp:
#    np.save(fp,x)
print("---------分隔線---------")
with open(filename,"rb") as fp:
    x2 =  np.load(fp,x)
    print(x2)
