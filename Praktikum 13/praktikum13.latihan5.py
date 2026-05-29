# Nama: Haura Nur Hafizhah
# NIM: J0403251083
# Kelas: TPL A1
# Praktikum 13 - Graph III: Spanning Tree

import heapq

# Representasi weighted graph
graph = {
    'Bogor': {
        'Jakarta': 5,
        'Depok': 2
    },

    'Jakarta': {
        'Bogor': 5,
        'Depok': 3,
        'Bandung': 6
    },

    'Depok': {
        'Bogor': 2,
        'Jakarta': 3,
        'Bandung': 4
    },

    'Bandung': {
        'Jakarta': 6,
        'Depok': 4
    }
}


def prim(graph, start):

    # Node yang sudah dikunjungi
    visited = set([start])

    # Priority queue untuk edge
    edges = []

    # Memasukkan edge dari node awal
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    # Proses algoritma Prim
    while edges:

        # Mengambil edge dengan bobot terkecil
        weight, u, v = heapq.heappop(edges)

        # Jika node belum dikunjungi
        if v not in visited:

            visited.add(v)

            mst.append((u, v, weight))
            total_weight += weight

            # Menambahkan edge baru
            for neighbor, w in graph[v].items():

                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight


# Menjalankan algoritma Prim
mst, total = prim(graph, 'Bogor')

# Menampilkan hasil MST
print("Minimum Spanning Tree:\n")

for edge in mst:
    print(edge)

print("\nTotal bobot minimum =", total)

# 1. Kasus apa yang dipilih?
# Kasus yang dipilih adalah Jaringan Jalan Antar Kota.

# 2. Algoritma apa yang digunakan?
# Algoritma yang digunakan adalah Prim.

# 3. Edge mana saja yang dipilih dalam MST?
# Edge yang dipilih adalah:
# - Bogor - Depok = 2
# - Depok - Jakarta = 3
# - Depok - Bandung = 4

# 4. Berapa total bobot MST?
# Total bobot MST adalah 9.

# 5. Mengapa edge tertentu tidak dipilih?
# Karena edge tersebut memiliki bobot lebih besar
# atau dapat membentuk cycle pada graph.