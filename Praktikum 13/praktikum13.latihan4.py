# Nama: Haura Nur Hafizhah
# NIM: J0403251083
# Kelas: TPL A1
# Praktikum 13 - Graph III: Spanning Tree

# Daftar edge: (bobot, gedung1, gedung2)

edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]

# Mengurutkan edge dari bobot terkecil
edges.sort()

mst = []
total_cost = 0

# Menyimpan node yang sudah terhubung
connected = set()

# Proses Kruskal sederhana
for weight, u, v in edges:

    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:

        mst.append((u, v, weight))
        total_cost += weight

        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST
print("Jaringan kabel minimum:\n")

for edge in mst:
    print(edge)

print("\nTotal biaya minimum =", total_cost)

# 1. Algoritma apa yang digunakan?
# Algoritma yang digunakan adalah Kruskal.

# 2. Edge mana saja yang dipilih?
# Edge yang dipilih adalah:
# - GedungC - GedungD = 1
# - GedungA - GedungC = 2
# - GedungB - GedungD = 3

# 3. Berapa total biaya minimum?
# Total biaya minimum yang dihasilkan adalah 6.

# 4. Mengapa MST cocok digunakan pada kasus ini?
# Karena MST dapat menghubungkan seluruh gedung
# dengan biaya pemasangan kabel seminimal mungkin
# tanpa membuat jalur yang berulang (cycle).