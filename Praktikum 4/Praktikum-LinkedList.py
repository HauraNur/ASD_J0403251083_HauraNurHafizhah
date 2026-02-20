#===========================================================
#Nama: Haura Nur Hafizhah
#NIM: J0403251083
#Kelas: TPL A1
#===========================================================

#===========================================================
#Implementasi Dasar: Node pada Linked List
#===========================================================

class Node:
    #Konstruktor yang dijalankan secara otomatis ketika class Node dipanggil/diinstantiasi
    def __init__(self,data):
        self.data = data #Menyimpan nilai atau data pada list
        self.next = None #Pointer ini menunjuk ke node berikutnya (awal = none)

#1) Membuat node dengan instantiasi class node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2) Mendefinisikan head dan menghubungkan Node: A -> B -> C -> None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

#4) Traversal: Menelusuri node dari head sampai ke None
current = head
while current is not None:
    print(current.data) #Menampilkan data pada node saat ini
    current = current.next #Pindah ke node berikutnya