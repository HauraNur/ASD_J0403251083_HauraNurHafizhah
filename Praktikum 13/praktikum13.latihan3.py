# Nama: Haura Nur Hafizhah
# NIM: J0403251083
# Kelas: TPL A1
# Praktikum 13 - Graph III: Spanning Tree

import heapq

# Representasi graph berbobot
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}


def prim(graph, start):

    # Menyimpan node yang sudah dikunjungi
    visited = set([start])

    # Priority queue untuk edge
    edges = []

    # Memasukkan edge dari node awal
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    # Proses Prim
    while edges:

        # Mengambil edge dengan bobot terkecil
        weight, u, v = heapq.heappop(edges)

        # Jika node belum dikunjungi
        if v not in visited:

            visited.add(v)

            mst.append((u, v, weight))
            total_weight += weight

            # Menambahkan edge baru ke heap
            for neighbor, w in graph[v].items():

                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight


# Menjalankan algoritma Prim
mst, total = prim(graph, 'A')

# Menampilkan hasil
print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total bobot =", total)

# 1. Node awal apa yang digunakan?
# Node awal yang digunakan adalah node A.

# 2. Edge mana yang dipilih pertama kali?
# Edge (A, C) dengan bobot 2 dipilih pertama kali
# karena merupakan bobot terkecil dari node A.

# 3. Bagaimana Prim menentukan edge berikutnya?
# Prim memilih edge dengan bobot terkecil yang
# menghubungkan node yang sudah dikunjungi
# dengan node yang belum dikunjungi.

# 4. Berapa total bobot MST yang dihasilkan?
# Total bobot MST yang dihasilkan adalah 6.

# 5. Apa perbedaan pendekatan Prim dan Kruskal?
# Prim memulai dari satu node lalu memperluas tree
# sedikit demi sedikit, sedangkan Kruskal memilih
# edge terkecil dari seluruh graph tanpa memulai
# dari node tertentu.