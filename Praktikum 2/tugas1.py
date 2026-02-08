# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama : Haura Nur Hafizhah
# NIM : J0403251083
# Kelas : TPL A1
# ==========================================================

# -------------------------------
# Konstanta nama file
# -------------------------------
nama_file = "stok_barang.txt"

# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------
def baca_stok(nama_file):
    stok_dict = {} #Inisialisasi data dictionary
    with open(nama_file,"r",encoding="utf-8") as file: #Membuka file dalam mode baca
        for baris in file: #Membaca  file baris per baris
            baris = baris.strip() #Menghapus spasi dan \n
            kode_barang, nama_barang, stok = baris.split(",") #Memisah kode,nama, dan stok
            stok_dict[kode_barang] = {"nama barang": nama_barang, "stok": int(stok)} #Menyimpan data ke dict
        return stok_dict
    
# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------
def simpan_stok(nama_file, stok_dict):
    with open(nama_file,"w",encoding="utf-8") as file: #Membuka file dalam mode tulis
        for kode_barang in sorted(stok_dict.keys()): #Menyimpan data berdasarkan kode barang yang diurutkan
            nama_barang = stok_dict[kode_barang]["nama barang"]
            stok = stok_dict[kode_barang]["stok"]
            file.write(f"{kode_barang},{nama_barang},{stok}\n") #Menulis data ke file

# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------
def tampilkan_semua(stok_dict):
    #Membuat header tabel
    print("\n=== DAFTAR STOK KANTIN ===")
    print(f"{"Kode Barang" : <10} | {"Nama Barang" : <12} | {"Stok" : >5}") 
    print("-"*35) #Membuat garis

    #Menampilkan isi data stoknya
    for kode_barang in sorted(stok_dict.keys()):
        nama_barang = stok_dict[kode_barang]["nama barang"]
        stok = stok_dict[kode_barang]["stok"]
        print(f"{kode_barang:<10} | {nama_barang:<12} | {int(stok):>5}")

# -------------------------------
# Fungsi: Cari barang berdasarkan kode
# -------------------------------
def cari_barang(stok_dict):
    kode_cari = input("Masukkan kode barang yang ingin dicari: ").strip()

    #Mengecek apakah kode ada di data
    if kode_cari in stok_dict:
        nama_barang = stok_dict[kode_cari]["nama barang"]
        stok = stok_dict[kode_cari]["stok"]

        #Menampilkan data barang
        print("===== Barang Ditemukan =====")
        print(f"Kode Barang : {kode_cari}")
        print(f"Nama Barang : {nama_barang}")
        print(f"Stok : {stok}")

    else:
        print("Barang tidak ditemukan. Pastikan kode barang yang dimasukkan benar.")

# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------
def tambah_barang(stok_dict):
    #Input data barang baru
    kode = input("Masukkan kode barang baru: ").strip()
    nama = input("Masukkan nama barang: ").strip()

    #Validasi input stok
    try:
        stok_awal = int(input("Masukkan jumlah stok barang: "))
    except ValueError:
        print("Stok harus berupa angka!")

    #Mengecek apakah kode sudah ada
    if kode in stok_dict:
        print("Kode sudah digunakan.")
        return
    
    #Menambahkan barang ke dictionary
    stok_dict[kode] = {
        "nama barang" : nama,
        "stok" : stok_awal
    }

    print(nama, "berhasil ditambahkan dengan stok sebanyak", stok_awal)

# -------------------------------
# Fungsi: Update stok barang
# -------------------------------
def update_stok (stok_dict):
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip() #Input kode barang yang diupdate
    
    #Validasi kode barang
    if kode not in stok_dict:
        print("Kode tidak ditemukan. Update dibatalkan.")
        return
    
    #Menu update stok
    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")
    
    #Validasi pilihan menu
    try:
        pilihan = int(input("Masukkan pilihan (1/2): ").strip())
    except ValueError:
        print("Pilihan harus berupa angka.")
        return
    
    #Validasi jumlah stok
    try:
        jumlah = int(input("Masukkan jumlah: "))
    except ValueError:
        print("Jumlah harus berupa angka.")
        return
    
    stok_baru = stok_dict[kode]["stok"]

    #Menambah stok
    if pilihan == 1:
        stok_dict[kode]["stok"] = stok_baru + jumlah
        print("Stok berhasil ditambah.")

    #Mengurangi stok
    elif pilihan == 2:
        if stok_baru - jumlah < 0:
            print("Stok tidak boleh kurang dari 0. Update dibatalkan.")
            return
        stok_dict[kode]["stok"] = stok_baru - jumlah
        print("Stok berhasil dikurangi.")

    else:
        print("Pilihan tidak valid.")

# -------------------------------
# Program Utama
# -------------------------------
def main():
    stok_barang = baca_stok(nama_file) #Membaca data stok dari file

    #Perulangan menu utama
    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")
        
        pilihan = input("Pilih menu: ").strip()
        
        #Menjalankan menu sesuai pilihan
        if pilihan == "1":
            tampilkan_semua(stok_barang)
        
        elif pilihan == "2":
            cari_barang(stok_barang)
            
        elif pilihan == "3":
            tambah_barang(stok_barang)
            
        elif pilihan == "4":
            update_stok(stok_barang)
            
        elif pilihan == "5":
            simpan_stok(nama_file5, stok_barang)
            print("Data berhasil disimpan.")
            
        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

#Menjalankan program utama
if __name__ == "__main__":
    main()