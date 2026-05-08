# ==========================================================
# Nama: Haura Nur Hafizhah
# NIM: J0403251083
# Kelas: TPL A1
# ==========================================================


# Fungsi untuk membuat adjacency matrix
def createGraph(V, edges):

    # Membuat matrix berukuran V x V
    # Semua isi awalnya 0
    # 0 berarti belum ada hubungan antar node
    mat = [[0 for _ in range(V)] for _ in range(V)]

    # Melakukan perulangan untuk setiap edge
    for u, v in edges:

        # Menandakan node u terhubung ke node v
        mat[u][v] = 1

        # Karena graph tidak berarah (undirected),
        # maka node v juga terhubung ke node u
        mat[v][u] = 1

    # Mengembalikan adjacency matrix
    return mat


# Program utama dijalankan dari sini
if __name__ == "__main__":

    # Jumlah vertex/node
    V = 4

    # Daftar edge pada graph
    # [0,1] berarti node 0 terhubung ke node 1
    edges = [
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 3]
    ]

    # Memanggil fungsi createGraph
    # untuk membuat adjacency matrix
    mat = createGraph(V, edges)

    # Menampilkan judul output
    print("Adjacency Matrix:")

    # Perulangan untuk menampilkan isi matrix
    for i in range(V):

        # Perulangan setiap kolom
        for j in range(V):

            # Menampilkan isi matrix
            print(mat[i][j], end=" ")

        # Pindah ke baris berikutnya
        print()