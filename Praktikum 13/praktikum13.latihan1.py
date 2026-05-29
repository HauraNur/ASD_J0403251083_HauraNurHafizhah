# Nama: Haura Nur Hafizhah
# NIM: J0403251083
# Kelas: TPL A1
# Praktikum 13 - Graph III: Spanning Tree

# Daftar edge graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree yang valid
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

# Menampilkan edge graph
print("Edge pada graph:")
for edge in edges:
    print(edge)

# Menampilkan spanning tree
print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

# Menampilkan jumlah edge
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# 1. Graph awal memiliki semua hubungan antar node,
# sedangkan spanning tree hanya mengambil edge tertentu
# agar semua node tetap terhubung tanpa cycle.

# 2. Spanning tree tidak boleh memiliki cycle karena
# tujuan spanning tree adalah menghubungkan semua node
# dengan jalur paling sederhana tanpa putaran.

# 3. Jumlah edge spanning tree selalu lebih sedikit karena
# spanning tree hanya mengambil edge minimum yang diperlukan
# untuk menghubungkan semua node.
# Pada graph dengan n node, spanning tree selalu memiliki n-1 edge.