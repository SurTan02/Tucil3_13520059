import random

# Fungsi untuk mengubah matriks ke dalam string
def toString(mtrx):
    word = ''
    for x in mtrx:
        for y in x:
            word += "-" + (str(y))
    return word

# Fungsi untuk melakukan peng-copy-an matriks
def CopyMtrx(mtrx):
    temp = [[0 for i in range (4)] for j in range (4)]
    for i in range(4):
        for j in range(4):
            temp[i][j] = mtrx[i][j]
    return temp

# fungsi untuk membuat matriks secara random
def RandomizeMatrix():
    temp = random.sample(range(0,50), 50)
    mtrx = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    for i in range (len(temp)):
        if temp[i] % 4 == 0:
            mtrx = Up(mtrx)
        elif temp[i] % 4 == 1:
            mtrx = Left(mtrx)
        elif temp[i] % 4 == 2:
            mtrx = Down(mtrx)
        else:
            mtrx = Right(mtrx)   
    
    return mtrx

# Prosedur untuk mencetak matriks ke layar
def Output(mtrx):
    
    for i in range (4):
        for j in range(4):
            if (mtrx[i][j] != 16):
                print(str(mtrx[i][j]).rjust(4),end="")
            else:
                print(str("-").rjust(4),end="")                
        print() 

# Fungsi untuk mendapatkan posisi value pada matriks
def Position(mtrx, value):
    for i in range(4):
        for j in range(4):
            if value == mtrx[i][j]:
                return [i,j]

# Fungsi yang mengembalikan matriks yang tile #16 dimove ke atas
def Up(mtrx):
    nol = Position(mtrx, 16)
    tempMtrx = CopyMtrx(mtrx)
    
    if(nol[0] != 0 ):
        tempMtrx[nol[0]][nol[1]] = mtrx[nol[0]-1][nol[1]]
        tempMtrx[nol[0]-1][nol[1]] = 16
    
    return tempMtrx

# Fungsi yang mengembalikan matriks yang tile #16 dimove ke bawah
def Down(mtrx):
    nol = Position(mtrx, 16)
    tempMtrx = CopyMtrx(mtrx)

    if(nol[0] != 3 ):
        
        tempMtrx[nol[0]][nol[1]] = mtrx[nol[0]+1][nol[1]]
        tempMtrx[nol[0]+1][nol[1]] = 16

    return tempMtrx

# Fungsi yang mengembalikan matriks yang tile #16 dimove ke kiri
def Left(mtrx):
    nol = Position(mtrx, 16)
    
    tempMtrx = CopyMtrx(mtrx)

    if(nol[1] != 0 ):
        tempMtrx[nol[0]][nol[1]] = mtrx[nol[0]][nol[1]-1]
        tempMtrx[nol[0]][nol[1]-1] = 16
    
    return tempMtrx

# Fungsi yang mengembalikan matriks yang tile #16 dimove ke kanan
def Right(mtrx):
    nol = Position(mtrx, 16)
    tempMtrx = CopyMtrx(mtrx)

    if(nol[1] != 3 ):
        tempMtrx[nol[0]][nol[1]] = mtrx[nol[0]][nol[1]+1]
        tempMtrx[nol[0]][nol[1]+1] = 16
    
    return tempMtrx

# Fungsi untuk menghitung fungsi kurang pada tiap tile
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

# Fungsi untuk menentukan apakah puzzle solveable atau tidak
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

# Fungsi untuk menghitung cost
def Cost(mtrx, depth):

    if (finished(mtrx)):
        return 0
    else:
        count = 0
        num = 1
        for x in mtrx:
            for y in x:
                if (y != 16 and y != num):
                    count+=1
                num+=1

        return count+depth

# Fungsi yang mengembalikan matriks yang tile #16 dimove ke atas
def GenerateNodes(currentNode, antrian, currentId, dict):

    # ParentId, currentId,  Matrix, Cost, Level, char
    posisi = Position(currentNode[2], 16)
    depth = currentNode[4] + 1
    
    tempCost = depth
    if (posisi[0] != 0) and currentNode[-1] != 'd':         # Up
        temp = Up(currentNode[2])
        tempCost = Cost(temp,depth) 

        if (toString(temp) not in dict):
            antrian.append([currentNode[1], currentId, temp , tempCost , depth, 'u'])
            dict[toString(temp)] = 'u'
            currentId+=1
         
    if (posisi[1] != 0)  and currentNode[-1] != 'r':        # Left
        temp = Left(currentNode[2])
        tempCost = Cost(temp,depth) 

        if (toString(temp) not in dict):
            antrian.append([currentNode[1], currentId, temp ,tempCost, depth, 'l'])
            dict[toString(temp)] = 'l'
            currentId+=1
           
    if (posisi[0] != 3)  and currentNode[-1] != 'u':        # Down
        temp = Down(currentNode[2])
        tempCost = Cost(temp,depth) 

        if (toString(temp)not in dict):
            antrian.append([currentNode[1], currentId, temp , tempCost, depth, 'd'])
            dict[toString(temp)] = 'd'
            currentId+=1

    if (posisi[1] != 3) and  currentNode[-1] != 'l':        # Right
        temp = Right(currentNode[2])
        tempCost = Cost(temp,depth) 

        if (toString(temp) not in dict):
            antrian.append([currentNode[1], currentId, temp ,tempCost, depth, 'r'])
            dict[toString(temp)] = 'r'
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

def solution(currentNode, visited):
    result = []

    while (currentNode[0] != 0):
        result.append(currentNode[-1])
        currentNode = visited[str(currentNode[0])]

    result.append(currentNode[-1])
    return result[::-1] 

def printSolution(mtrx, solution):
    
    print("Initial")
    Output(mtrx)
    i = 1
    listOfMove = []
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

        listOfMove.append(move)
        print("\nMove", i,":", move)
        Output(mtrx)
        i+=1
   
    print("\nMove yang diperlukan(%d) :" %(len(solution)) , end = " ")
    print(*listOfMove,sep = ", ") 
        
    
def solve(mtrx):
    nodes = [[0,0,mtrx, 0, 0, '-']]
    visited = {}
    banyakSimpul= 1
    idx = 0
    
    simpul = { toString(mtrx) : 'CHECK'}
    
    while (not finished(nodes[0][2])):
        currentNode = nodes.pop(0)
        visited[str(currentNode[1])] = currentNode
        
        banyakSimpul =  GenerateNodes(currentNode, nodes, banyakSimpul, simpul)
        idx+=1
        nodes.sort(key = getCost)
    return nodes[0], visited, banyakSimpul

def readFile():
     
    FileFound = False
    while (not FileFound):
        file = str(input("Nama File : "))
        file = "../test/" + file
        try:
            mtrx = open(file,"r")
            FileFound = True
        except:
            print("File Tidak Ditemukan")
    
    puzzle=[] # Menyimpan matrix
    for line in mtrx.readlines():
        puzzle.append( [ int (x) for x in line.split(' ') ] )
    return puzzle