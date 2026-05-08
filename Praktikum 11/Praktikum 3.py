# ==========================================================
# Nama: Haura Nur Hafizhah
# NIM: J0403251083
# Kelas: TPL A1
# ==========================================================


# Membuat adjacency matrix
# Angka 1 berarti ada hubungan antar node
# Angka 0 berarti tidak ada hubungan

matrix = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
]


# Membuat dictionary kosong
# untuk menyimpan adjacency list
adj_list = {}


# Perulangan untuk setiap baris pada matrix
for i in range(len(matrix)):

    # Membuat list kosong untuk setiap node
    adj_list[i] = []


    # Perulangan setiap kolom pada matrix
    for j in range(len(matrix[i])):

        # Jika bernilai 1,
        # berarti node saling terhubung
        if matrix[i][j] == 1:

            # Menambahkan node yang terhubung
            # ke adjacency list
            adj_list[i].append(j)


# Menampilkan judul output
print("Adjacency List:")


# Menampilkan isi adjacency list
for node in adj_list:

    # Menampilkan node dan tetangganya
    print(node, "->", adj_list[node])