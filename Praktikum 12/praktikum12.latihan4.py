# Nama: Haura Nur Hafizhah
# NIM: J0403251083
# Kelas: TPL A1
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")

for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

# Jawaban Analisis:
# 1. Lokasi mana yang paling dekat dari Gerbang?
# Lokasi yang paling dekat dari Gerbang adalah Kantin dengan waktu tempuh 2 menit.

# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
# Waktu tempuh terpendek dari Gerbang ke Aula adalah 7 menit melalui jalur
# Gerbang → Kantin → Lab → Aula.

# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
# Jalur langsung tidak selalu menghasilkan jarak paling kecil, karena bisa saja
# ada jalur lain dengan total bobot lebih rendah. Pada kasus ini, jalur tidak langsung 
# melalui Lab justru lebih cepat dibanding jalur langsung dari Kantin ke Aula.

# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
# Dijkstra cocok digunakan pada kasus lokasi kampus ini karena semua bobot bernilai positif
# dan algoritma ini efektif untuk mencari rute tercepat dari satu lokasi ke lokasi lainnya.