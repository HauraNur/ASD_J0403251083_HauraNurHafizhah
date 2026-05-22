# Nama: Haura Nur Hafizhah
# NIM: J0403251083
# Kelas: TPL A1
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Program Mencari Jalur Terpendek Antar Kota
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Representasi weighted graph menggunakan dictionary
# Bobot menunjukkan jarak antar kota
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Jakarta': {'Bandung': 7},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Bandung': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node awal
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak saat ini lebih besar dari jarak yang tersimpan,
        # maka proses dilewati
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika ditemukan jarak yang lebih kecil,
            # maka perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Menentukan node awal
start_node = 'Bogor'

# Menjalankan algoritma Dijkstra
hasil = dijkstra(graph, start_node)

# Menampilkan hasil jarak terpendek
print("Jarak terpendek dari Bogor:")

for kota, jarak in hasil.items():
    print("Bogor ->", kota, "=", jarak)

# Jawaban Analisis:
# 1. Node awal yang digunakan apa?
# Node awal yang digunakan adalah Bogor.

# 2. Node mana yang memiliki jarak paling kecil dari node awal?
# Node yang memiliki jarak paling kecil dari node awal adalah Depok dengan jarak 2.

# 3. Node mana yang memiliki jarak paling besar dari node awal?
# Node yang memiliki jarak paling besar dari node awal adalah Bandung dengan jarak 8.

# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
# Algoritma Dijkstra bekerja dengan mencari jalur dengan total bobot terkecil dari node awal
# ke node lain. Pada kasus ini, algoritma mulai dari Bogor lalu membandingkan semua kemungkinan
# jalur menuju kota lain. Jika ditemukan jalur yang lebih pendek, maka jaraknya diperbarui hingga
# diperoleh jarak terpendek ke seluruh kota.