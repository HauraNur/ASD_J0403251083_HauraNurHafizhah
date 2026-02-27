# ==========================================================
# Nama: Haura Nur Hafizhah
# NIM: J0403251083
# Kelas: TPL A1
# Latihan 1: Rekursi Pangkat
# ==========================================================
def pangkat(a, n):
   # Base case
   if n == 0:
     return 1
   # Recursive case
   return a * pangkat(a, n - 1)

print(pangkat(2, 4)) # Output: 16

# Program ini digunakan untuk menghitung nilai pangkat dengan metode rekursi. Fungsi pangkat(a, n) akan mengalikan angka a sebanyak n kali dengan cara memanggil dirinya sendiri. 
# Base case terdapat pada kondisi n == 0, yang mengembalikan nilai 1. 
# Bagian ini berfungsi untuk menghentikan rekursi karena dalam matematika setiap bilangan berpangkat 0 bernilai 1. 
# Recursive call ada pada return a * pangkat(a, n - 1), yang berarti fungsi akan terus memanggil dirinya dengan nilai pangkat dikurangi satu sampai mencapai 0. 
# Setelah itu, hasilnya dikalikan kembali hingga diperoleh hasil akhir.