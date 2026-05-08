# ==========================================================
# Nama: Haura Nur Hafizhah
# NIM: J0403251083
# Kelas: TPL A1
# ==========================================================


# Membuat adjacency list menggunakan dictionary
# Setiap key adalah node
# Isi list menunjukkan node yang terhubung

graph = {

    # Node A terhubung ke B dan C
    'A': ['B', 'C'],

    # Node B terhubung ke A dan D
    'B': ['A', 'D'],

    # Node C terhubung ke A dan D
    'C': ['A', 'D'],

    # Node D terhubung ke B dan C
    'D': ['B', 'C']
}


# Menampilkan judul output
print("Adjacency List:")


# Melakukan perulangan untuk setiap node pada graph
for node in graph:

    # Menampilkan node beserta node yang terhubung
    print(node, "->", graph[node])