# ==========================================================
# Nama: Haura Nur Hafizhah
# NIM: J0403251083
# Kelas: TPL A1
# ==========================================================

def quickSort(skor):
    quickSortHelper(skor,0,len(skor)-1)

def quickSortHelper(skor,first,last):
    if first < last:
        splitpoint = partition(skor,first,last)
        quickSortHelper(skor,first,splitpoint-1)
        quickSortHelper(skor,splitpoint+1,last)

def partition(skor,first,last):
    pivotvalue = skor[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and skor[leftmark] >= pivotvalue:
            leftmark = leftmark + 1

        while skor[rightmark] <= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = skor[leftmark]
            skor[leftmark] = skor[rightmark]
            skor[rightmark] = temp

    temp = skor[first]
    skor[first] = skor[rightmark]
    skor[rightmark] = temp

    return rightmark


skor_tes = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
quickSort(skor_tes)
print("Skor setelah diurutkan:", skor_tes)
print("5 skor tertinggi:", skor_tes[:5])