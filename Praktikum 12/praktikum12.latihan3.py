# Nama: Haura Nur Hafizhah
# NIM: J0403251083
# Kelas: TPL A1
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):

        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():

                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances

hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")

for node, distance in hasil.items():
    print(node, "=", distance)

# Jawaban Analisis:
# 1. Berapa bobot langsung dari A ke B?
# Bobot langsung dari A ke B adalah 5.

# 2. Berapa total bobot jalur A -> C -> B?
# Total bobot jalur A → C → B adalah 2 (4 + (-2))

# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
# Jalur yang menghasilkan jarak lebih kecil menuju B adalah A → C → B karena
# total bobotnya lebih kecil dibanding jalur langsung.

# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
# Bellman-Ford dapat digunakan pada graph dengan bobot negatif karena algoritma ini memeriksa
# dan memperbarui jarak secara berulang, sehingga masih bisa menemukan jalur terpendek meskipun
# ada edge bernilai negatif.

# 5. Apa yang dimaksud dengan proses relaksasi edge?
# Relaksasi edge adalah proses membandingkan jarak lama dengan jarak baru yang lebih kecil
# melalui suatu jalur. Jika ditemukan jarak yang lebih pendek, maka nilai jaraknya diperbarui.

# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
# Perbedaan utama Bellman-Ford dan Dijkstra adalah Bellman-Ford dapat menangani bobot negatif,
# sedangkan Dijkstra tidak. Selain itu, Dijkstra biasanya lebih cepat, sementara Bellman-Ford
# lebih fleksibel untuk graph tertentu.