# ==========================================================
# Nama: Haura Nur Hafizhah
# NIM: J0403251083
# Kelas: TPL A1
# Latihan 4: Kombinasi Huruf
# ==========================================================
def kombinasi(n, hasil=""):
   # Base Case
   if len(hasil) == n:
     print(hasil)
     return
   
   # Recursive Case
   kombinasi(n, hasil + "A")
   # Recursive Case
   kombinasi(n, hasil + "B")

kombinasi(2)

# Program ini menghasilkan semua kombinasi huruf A dan B sepanjang n dengan rekursi.
# Base case terjadi saat panjang hasil sudah sama dengan n, lalu kombinasi tersebut dicetak.
# Setiap langkah rekursi memiliki 2 pilihan (tambah "A" atau "B"), sehingga jumlah kombinasi yang dihasilkan adalah 2^n.
# Untuk n = 2, jumlah kombinasi = 2^2 = 4, yaitu: AA, AB, BA, BB.