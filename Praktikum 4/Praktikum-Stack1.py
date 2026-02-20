#===========================================================
#Nama: Haura Nur Hafizhah
#NIM: J0403251083
#Kelas: TPL A1
#===========================================================

#===========================================================
#Implementasi Dasar: Stack
#===========================================================

class Node:
    #Konstruktor yang dijalankan secara otomatis ketika class Node dipanggil/diinstantiasi
    def __init__(self,data):
        self.data = data #Menyimpan nilai atau data pada list
        self.next = None #Pointer ini menunjuk ke node berikutnya (awal = none)

#Stack ada operasi push (memasukkan head baru) dan pop (menghapus head)

class stack:
    def __init__(self):
        self.top = None #Top menunjuk ke node paling atas

    def is_empty(self):
        return self.top is None #Stack kosong jika top = None

    def push(self,data):
        #1 membuat node baru
        nodeBaru = Node(data)

        #2 node baru menunjuk ke top yang lama (head lama)
        nodeBaru.next = self.top

        #3 geser top pindah ke node baru
        self.top = nodeBaru
    
    def pop(self): #Mengambil/Menghapus node paling atas (top/head)

        if self.is_empty():
            print("Stack kosong, tidak bisa pop")
            return None
        data_terhapus = self.top.data #Soroti bagian top dan simpan di variabel
        self.top = self.top.next #Geser top ke node berikutnya
        return data_terhapus
    
    def peek(self):
        #Melihat data yang paling atas tanpa menghapus
        if self.is_empty():
            return None
        return self.top.data

    def tampilkan(self):
        current = self.top
        print("Top", end=" -> ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

#Instantiasi Class Stack
s = stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print("Peek (Lihat Top): ", s.peek())
s.pop()
s.tampilkan()
print("Peek (Lihat Top): ", s.peek())