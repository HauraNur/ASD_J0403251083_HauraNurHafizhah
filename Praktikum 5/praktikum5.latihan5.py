# ==========================================================
# Nama: Haura Nur Hafizhah
# NIM: J0403251083
# Kelas: TPL A1
# Studi Kasus: Generator PIN
# ==========================================================
def buat_pin(panjang, hasil=""):
   # Base Case
   if len(hasil) == panjang:
     print("PIN:", hasil)
     return
   # Loop setiap kemungkinan angka
   for angka in ["0", "1", "2"]:
     # Recursive Case
     buat_pin(panjang, hasil + angka)
     
buat_pin(3)

# Program ini membuat semua kombinasi PIN dari angka 0, 1, dan 2 sepanjang panjang tertentu dengan rekursi.
# Agar angka yang sama tidak muncul berulang dalam satu PIN, kita perlu memastikan angka yang akan ditambahkan belum ada di hasil.
# Caranya dengan menambahkan pengecekan if angka not in hasil sebelum memanggil rekursi.