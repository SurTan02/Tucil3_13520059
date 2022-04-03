from solver import *
import time

print("Pilih Jenis Masukkan:")
print("1. File")
print("2. Randomize")

pilihan = int(input("Pilihan : "))

while (pilihan != 1 and pilihan != 2):
    print("Pilihan tidak sesuai, ketikkan angka 1 atau 2")
    pilihan = int(input("Pilihan (Int)>> "))

if (pilihan == 1):
    mtrx = readFile()
else:
    mtrx = RandomizeMatrix()

print("===== Matriks =====")
Output(mtrx)

if (not IsSolveable(mtrx)) :
    print("Puzzle tidak dapat diselesaikan")
else:
    startTime = time.time()

    nodes = []
    visited = {}
    nodes, visited, banyakSimpul  = solve(mtrx)

    endTime = time.time()

    solusi = solution(nodes, visited)
    print("\n==== Urutan Penyelesain Matriks ====")
    printSolution(mtrx, solusi)
    print("Jumlah simpul yang dibangkitkan :",banyakSimpul)
    print("Waktu Eksekusi Program :  %s seconds"  % (endTime - startTime))