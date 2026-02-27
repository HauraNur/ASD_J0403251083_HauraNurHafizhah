# ==========================================================
# Nama: Haura Nur Hafizhah
# NIM: J0403251083
# Kelas: TPL A1
# Latihan 2: Tracing Rekursi
# ==========================================================
def countdown(n):
   # Base Case
   if n == 0:
     print("Selesai")
     return
   print("Masuk:", n)
   # Recursive Case
   countdown(n - 1)
   print("Keluar:", n)

countdown(3)

# Program ini menunjukkan cara kerja rekursi pada fungsi countdown(n), yang mencetak teks sebelum dan sesudah memanggil dirinya sendiri.
# Base case ada pada n == 0, yang mencetak "Selesai" lalu menghentikan rekursi dengan return.
# Recursive call terdapat pada countdown(n - 1), sehingga nilai n terus berkurang sampai 0.
# Output "Keluar" muncul terbalik karena perintah tersebut dijalankan setelah pemanggilan rekursi selesai. Program turun dulu sampai base case, lalu saat kembali naik, barulah "Keluar" dicetak dari angka kecil ke besar.
