# Nama: Haura Nur Hafizhah
# NIM: J0403251083
# Kelas: TPL A1
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Implementasi Sederhana Algoritma Kruskal
# ==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0
connected = set()

for weight, u, v in edges:

    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight

        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST
print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total bobot =", total_weight)

# 1. Edge mana yang dipilih pertama kali?
# Edge ('C', 'D') dengan bobot 1 dipilih pertama kali
# karena memiliki bobot paling kecil.

# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
# Karena algoritma Kruskal bekerja dengan memilih
# edge berbobot terkecil terlebih dahulu agar total
# bobot Minimum Spanning Tree menjadi minimum.

# 3. Berapa total bobot MST yang dihasilkan?
# Total bobot MST yang dihasilkan adalah 6.

# 4. Mengapa edge tertentu tidak dipilih?
# Karena edge tersebut dapat membentuk cycle atau
# sudah ada jalur lain yang menghubungkan node-node tersebut.