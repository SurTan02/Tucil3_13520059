import random
import time






def CopyMtrx(mtrx):
    temp = [[0 for i in range (4)] for j in range (4)]
    for i in range(4):
        for j in range(4):
            temp[i][j] = mtrx[i][j]
    return temp

def RandomizeMatrix():
    temp = random.sample(range(1, 17), 16)
    mtrx = [[0 for i in range (4)] for j in range (4)]

    k = 0
    for i in range (4):
        for j in range(4):
            
            mtrx[i][j] = temp[k]
            k +=1 

    return mtrx

def Output(mtrx):
    
    for i in range (4):
        for j in range(4):
            if (mtrx[i][j] != 16):
                print(str(mtrx[i][j]).rjust(4),end="")
            else:
                print(str("-").rjust(4),end="")                
        print() 

def Position(mtrx, value):
    for i in range(4):
        for j in range(4):
            if value == mtrx[i][j]:
                return [i,j]

def Up(mtrx):
    nol = Position(mtrx, 16)
    tempMtrx = CopyMtrx(mtrx)
    
    if(nol[0] != 0 ):
        tempMtrx[nol[0]][nol[1]] = mtrx[nol[0]-1][nol[1]]
        tempMtrx[nol[0]-1][nol[1]] = 16
    
    return tempMtrx
    
def Down(mtrx):
    nol = Position(mtrx, 16)
    tempMtrx = CopyMtrx(mtrx)

    if(nol[0] != 3 ):
        
        tempMtrx[nol[0]][nol[1]] = mtrx[nol[0]+1][nol[1]]
        tempMtrx[nol[0]+1][nol[1]] = 16

    return tempMtrx

def Left(mtrx):
    nol = Position(mtrx, 16)
    
    tempMtrx = CopyMtrx(mtrx)

    if(nol[1] != 0 ):
        tempMtrx[nol[0]][nol[1]] = mtrx[nol[0]][nol[1]-1]
        tempMtrx[nol[0]][nol[1]-1] = 16
    
    return tempMtrx

def Right(mtrx):
    nol = Position(mtrx, 16)
    tempMtrx = CopyMtrx(mtrx)

    if(nol[1] != 3 ):
        tempMtrx[nol[0]][nol[1]] = mtrx[nol[0]][nol[1]+1]
        tempMtrx[nol[0]][nol[1]+1] = 16
    
    return tempMtrx


def Kurang(mtrx, num):
    count = 0
    posisi = Position(mtrx, num)    
   
    for j in range (posisi[1], 4):
        if (num > mtrx[posisi[0]][j]):
            count+=1

    for i in range (posisi[0]+1, 4):
        for j in range(4):
            
            if (num > mtrx[i][j]):
                count+=1
    return count

def IsSolveable(mtrx) :

    sum = 0
    print("[]======================[]")
    print("||",    "i".rjust(5), "||".rjust(5), " kurang".rjust(5), "||".rjust(3))
    print("[]======================[]")
    for i in range (1,17):
        kurang = Kurang(mtrx, i)
        
        print("||" , str(i).rjust(5), "||".rjust(5) , str(kurang).rjust(5), "||".rjust(5))
        sum+=kurang
    posisi = (Position(mtrx, 16)[0]* 4) + Position(mtrx, 16)[1] + 1

    
    # 2,4,5,7,10,12,13,15
    print("[]======================[]")
    print("Nilai Sigma(Kurang(i)) + X : " , sum + (posisi in [2,4,5,7,10,12,13,15]))
    if ((sum + (posisi in [2,4,5,7,10,12,13,15])) %2 == 0 ):
        return True
    else:
        return False

def Cost(mtrx, depth):
    count = 0
    num = 1
    for i in range (4):
        for j in range (4):
            if (mtrx[i][j]!= 16 and mtrx[i][j] != num):
                count+=1
            num+=1

    return count+depth

def GenerateNodes(currentNode, antrian, currentId, dict):

    # ParentId, currentId,  Matrix, Cost, Level, char
    posisi = Position(currentNode[2], 16)
    depth = currentNode[4] + 1
    found = False
    
    
    if (posisi[1] != 0) and currentNode[-1] != 'd':     # MOVEUP
        temp = Up(currentNode[2])
        found = finished(temp) 

        if (temp not in dict):
            if (found):
                antrian.append([currentNode[1], currentId, temp ,0, depth, 'u'])
                
            else:
                antrian.append([currentNode[1], currentId, temp ,Cost(temp, depth), depth, 'u'])

            dict[temp] = 'CHECK'
            currentId+=1
        

    if (posisi[1] != 0) and currentNode[-1] != 'r' and not found: # MOVELEFT
        temp = Left(currentNode[2])
        found = finished(temp) 

        if (temp not in dict):
            if (found):
                antrian.append([currentNode[1], currentId, temp ,0, depth, 'l'])
            else:
                antrian.append([currentNode[1], currentId, temp ,Cost(temp, depth), depth, 'l'])
        
            dict[temp] = 'CHECK'
            currentId+=1
       

    if (posisi[0] != 3) and currentNode[-1] != 'u' and not found: # MOVEDOWN
        temp = Down(currentNode[2])
        found = finished(temp) 

        if (temp not in dict):
            if (found):
                antrian.append([currentNode[1], currentId, temp ,0, depth, 'd'])
            else:    
                antrian.append([currentNode[1], currentId, temp ,Cost(temp, depth), depth, 'd'])
        
            dict[temp] = 'CHECK'
            currentId+=1
       

    if (posisi[1] != 3) and currentNode[-1] != "l" and not found: # MOVERIGHT
        temp = Right(currentNode[2])
        found = finished(temp) 

        if (temp not in dict):
            if (found):
                antrian.append([currentNode[1], currentId, temp ,0 , depth, 'r'])
            else:
                antrian.append([currentNode[1], currentId, temp ,Cost(temp, depth), depth, 'r'])
        
            dict[temp] = 'CHECK'
            currentId+=1
    return currentId
    
def finished(mtrx):
    idx = 1
    for x in mtrx:
        for y  in x:
            if (y != idx):
                return False
            idx+=1
    return True

def getCost(antrian):
    return antrian[3];   

def solution(currentNode, array):

    result = []
    while (currentNode[0] != 0):
        result.append(currentNode[-1])
        i = 0
        found = False
        while  (i < len(array) and not found):
            if currentNode[0] == array[i][1]:
                currentNode = array.pop(i)
                found = True
            else:
                i+=1 
    
    result.append(currentNode[-1])
    

    
    return result[::-1] 

def printSolution(mtrx, solution):
    
    print("Initial")
    Output(mtrx)
    i = 1
    for x in solution:
        if x == 'u':
            mtrx = Up(mtrx)
            move = 'UP'
        elif x == 'l':
            mtrx = Left(mtrx)
            move = 'LEFT'
        elif x == 'd':
            mtrx = Down(mtrx)
            move = 'DOWN'
        elif x == 'r':
            mtrx = Right(mtrx)
            move = 'RIGHT'

        print("\nMove", i,":", move)
        Output(mtrx)
        i+=1

def solve(mtrx):
    startTime = time.time()
    nodes = [[0,0,mtrx, 0, 0, '-']]
    visited = []
    simpul= 1
    idx = 0
    
    dict = { mtrx : 'CHECK'}
    while (not finished(nodes[0][2])):
        currentNode = nodes.pop(0)
        visited.append(currentNode)

        
        simpul =  GenerateNodes(currentNode, nodes,simpul, dict)
        idx+=1
        
        if (simpul % 1000 ==0 ):
            print(simpul)
        nodes.sort(key = getCost)
        
    
    print(simpul)
    solusi = solution(nodes[0], visited)
    printSolution(mtrx, solusi)
    print(solusi)
    print("--- %s seconds ---" % (time.time() - startTime))


def readFile():
     
    
    file = str(input("Nama File : "))
        
    try:
        mtrx = open(file,"r")
    except:
        print("File not found, using default file...")
        mtrx = open("t1.txt","r")
    
    puzzle=[] # Menyimpan matrix
    for line in mtrx.readlines():
        puzzle.append( [ int (x) for x in line.split(' ') ] )
    return puzzle

if __name__ == "__main__":
    # # mtrx = (RandomizeMtrx())
    # mtrx = [[1,3,4,15], 
    #                 [2,16,5,12],
    #                 [7,6,11,14],
    #                 [8,9,10,13]]

    mtrx =         [[1,2,3,4], 
                    [5,6,16,8],
                    [9,10,7,11],
                    [13,14,15,12]]

    mtrx =          [[1,2,4,7], 
                    [5,6,16,3],
                    [9,11,12,8],
                    [13,10,14,15]]
    
    
    # mtrx =         [[1,2,3,4], 
    #                 [5,6,7,8],
    #                 [9,10,11,12],
    #                 [13,14,16,15]]

    # mtrx = [[2,3,4,11], [1,5,10,8], [9,6,12,15],  [13,14,16,7]]
    # mtrx = [[1,3,4,15], [2,16,12,5], [7,6,11,14],  [8,9,10,13]]
    mtrx = [[1,2,3,4],[5,6,7,8],[11,12,15,14],[10,9,13,16]]
    # mtrx = [[1,6,10,3],[5,12,7,4],[9,16,2,8],[13,14,11,15]]
    mtrx = [[1,2,3,4],[5,6,7,11],[9,10,12,8],[13,14,15,16]]
    
    mtrx = readFile()
    Output(mtrx)
    if (not IsSolveable(mtrx)) :
        print("Matriks tidak dapat dikerjakan")
    
    else:
    # check(mtrx)
        solve(mtrx)


        

