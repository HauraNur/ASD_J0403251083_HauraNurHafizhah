#=============================================================================
#Praktikum 1: Konsep ADT dan File Handling
#Latihan Dasar 1: Membaca seluruh isi file data
#=============================================================================

print("====Membuka file dalam satu string====")
with open ("data_mahasiswa.txt","r",encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)
print("Tipe Data:", type(isi_file))

print("====Membuka file per baris====")
jumlah_baris = 0
with open ("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() #menghilangkan karakter baris baru
        print("Baris ke-", jumlah_baris)
        print("Isinya:", baris)

#=============================================================================
#Praktikum 1: Konsep ADT dan File Handling
#Latihan Dasar 2: Membaca data dan menyimpannya ke struktur data list
#=============================================================================

#Parsing baris menjadi bentuk satuan dan menampilkannya dalam bentuk kolom kolom data
with open ("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilang karakter baris baru
        nim,nama,nilai = baris.split(",") #pecah menjadi data satuan dan simpan ke variabel
        print("NIM:", nim, "| Nama:", nama, "| Nilai:", nilai) #menampilkan satuan data dalam bentuk kolom

#=============================================================================
#Praktikum 1: Konsep ADT dan File Handling
#Latihan Dasar 3: Membaca data dan menyimpannya dalam list
#=============================================================================

data_list = []

with open ("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilang karakter baris baru
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan dan simpan ke variabel
        data_list.append([nim,nama,int(nilai)])
print("====Menampilkan List")
print(data_list)
print("Contoh data record ke 1", data_list[0])
print("Contoh data record ke 2", data_list[1])

print("Jumlah Record", len(data_list))

#=============================================================================
#Praktikum 1: Konsep ADT dan File Handling
#Latihan Dasar 4: Membaca data dan menyimpannya ke Struktur Data Dictionary
#=============================================================================
data_dict = {} #Inisialisasi dictionary
with open ("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilang karakter baris baru
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan dan simpan ke variabel
        #simpan data dalam dictionary
        data_dict[nim] = {
            "nama" : nama,
            "nilai" : int(nilai)
        }
print("====Menampilkan Data Dictionary====")
print(data_dict)