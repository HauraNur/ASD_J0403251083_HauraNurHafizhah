# ==========================================================
# Nama: Haura Nur Hafizhah
# NIM: J0403251083
# Kelas: TPL A1
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================
def cari_maks(data, index=0):
   # Base case
   if index == len(data) - 1:
     return data[index]
   # Recursive case
   maks_sisa = cari_maks(data, index + 1)
   if data[index] > maks_sisa:
     return data[index]
   else:
     return maks_sisa

angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))

# Program ini mencari nilai maksimum dalam list secara rekursif dengan membandingkan satu elemen dengan sisa elemen setelahnya.
# Base case terjadi saat index berada di elemen terakhir, sehingga langsung mengembalikan nilai tersebut.
# Recursive call ada pada cari_maks(data, index + 1), yang mengecek sisa list. Nilai sekarang lalu dibandingkan dengan hasil tersebut, dan yang lebih besar dikembalikan sebagai maksimum.