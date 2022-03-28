# global matriks
from cmath import pi
import random
from sre_constants import ANY_ALL
import numpy as np



def randomizemtrx():
    temp = random.sample(range(1, 17), 16)
    mtrx = np.array([[0 for i in range (4)] for j in range (4)])

    k = 0
    for i in range (4):
        for j in range(4):
            
            mtrx[i][j] = temp[k]
            k +=1 

    return mtrx


def output(mtrx):
    for i in range (4):
        for j in range(4):
            if (mtrx[i][j] != 16):
                print(str(mtrx[i][j]).rjust(10),end="")
            else:
                print(str("-").rjust(10),end="")                
        print() 

def findPosition(mtrx, value):
    index_y,index_x = np.where(mtrx == value)
    return index_y[0],index_x[0]

def UP(mtrx):
    nol = findPosition(mtrx, 16)

    if(nol[0] != 0 ):
        temp = mtrx[nol[0]-1][nol[1]]
        mtrx[nol[0]-1][nol[1]] = 16
        mtrx[nol[0]][nol[1]] =temp
    
def DOWN(mtrx):
    nol = findPosition(mtrx, 16)

    if(nol[0] != 3 ):
        temp = mtrx[nol[0]+1][nol[1]]
        mtrx[nol[0]+1][nol[1]] = 16
        mtrx[nol[0]][nol[1]] = temp

def LEFT(mtrx):
    nol = findPosition(mtrx, 16)

    if(nol[1] != 0 ):
        temp = mtrx[nol[0]][nol[1]-1]
        mtrx[nol[0]][nol[1]-1] = 16
        mtrx[nol[0]][nol[1]] =temp

def RIGHT(mtrx):
    nol = findPosition(mtrx, 16)

    if(nol[1] != 3 ):
        temp = mtrx[nol[0]][nol[1]+1]
        mtrx[nol[0]][nol[1]+1] = 16
        mtrx[nol[0]][nol[1]] =temp

def check(mtrx):
    sum = 0
    
    # Ubah Ke list biar mudah untuk diperiksa
    tempList = []
    for i in range (4):
        for j in range(4):
            tempList.append(mtrx[i][j])
    
    for k in range (0,16):
        posisi = findPosition(mtrx, k+1)[0]* 4 + findPosition(mtrx, k+1)[1]
        
        print(posisi ,  k+1)
        
        for i in range(posisi, 16):
            if (k+1 > tempList[i]):
                # print("nilai k ", k+1)
                # print("value k ", tempList[k])
                # print("nilai i ", i)
                # print("value i ", tempList[i])
                sum+=1
        # print("nilai" ,k+1, sum)
    return sum

if __name__ == "__main__":
    # mtrx = (randomizemtrx())
    # mtrx = np.array([[1,3,4,15], 
    #                 [2,16,5,12],
    #                 [7,6,11,14],
    #                 [8,9,10,13]])

    mtrx = np.array([[1,2,3,4], 
                    [5,6,16,8],
                    [9,10,7,11],
                    [13,14,15,12]])
    output(mtrx)
    # check(mtrx)
    x = str(input())
    while (x!= "TES"):
        if (x == "LEFT") : LEFT(mtrx)
        elif (x == "RIGHT") : RIGHT(mtrx)
        elif (x == "UP") : UP(mtrx)
        elif (x == "DOWN") : DOWN(mtrx)
        
        output(mtrx)
        print("analisis " , check(mtrx))
        x = str(input())


