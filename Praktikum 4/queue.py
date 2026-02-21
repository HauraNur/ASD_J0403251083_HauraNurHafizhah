#===========================================================
#Nama: Haura Nur Hafizhah
#NIM: J0403251083
#Kelas: TPL A1
#===========================================================

#===========================================================
#Implementasi Dasar: Queue
#===========================================================

class Node:
    #Konstruktor yang dijalankan secara otomatis ketika class Node dipanggil/diinstantiasi
    def __init__(self,data):
        self.data = data #Menyimpan nilai atau data pada list
        self.next = None #Pointer ini menunjuk ke node berikutnya (awal = none)

class queue:
    #Buat Konstruktor untuk inisialisasi variabel front dan rear
    def __init__(self):
        self.front = None #Node paling depan
        self.rear = None #Node paling belakang

    def is_empty(self):
        return self.front is None

    #Membuat fungsi untuk menambahkan data baru
    def enqueue(self,data):
        nodeBaru = Node(data)

        #Jika queue kosong, front dan rear menunjuk kek node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
    
        #Jika queue tidak kosong, maaka letakkan data baru setelah rear dan jadikan data baru sebagai rear
        self.rear.next = nodeBaru
        self.rear = nodeBaru

    def dequeue(self):
        #Menghapus data dari depan/front
        data_terhapus = self.front.data #Lihat data paling depan
        
        #Geser front ke node berikutnya
        self.front = self.front.next

        #Jika setelah geser front menjadi none, maka queue kosong
        #Rear juga harus jadi None
        if self.front is None:
            self.rear = None

        return data_terhapus

    def tampilkan(self):
        current = self.front
        print("Front", end=" -> ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("Rear")

#Instantiasi class queue
q = queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()