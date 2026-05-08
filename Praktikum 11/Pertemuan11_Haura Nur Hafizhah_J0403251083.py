# ==========================================================
# Nama: Haura Nur Hafizhah
# NIM: J0403251083
# Kelas: TPL A1
# ==========================================================


# ==========================================================
# Adjacency List
# ==========================================================

# Membuat adjacency list menggunakan dictionary
# Key menunjukkan node
# Value menunjukkan node yang terhubung

graph = {

    # Router terhubung ke Switch1 dan Switch2
    "Router": ["Switch1", "Switch2"],

    # Switch1 terhubung ke beberapa perangkat
    "Switch1": ["Router", "PC1", "PC2", "Switch2"],

    # Switch2 terhubung ke Router, Switch1, dan Server
    "Switch2": ["Router", "Switch1", "Server"],

    # PC1 terhubung ke Switch1
    "PC1": ["Switch1"],

    # PC2 terhubung ke Switch1
    "PC2": ["Switch1"],

    # Server terhubung ke Switch2
    "Server": ["Switch2"]
}


# Menampilkan adjacency list
print("Adjacency List:\n")


# Perulangan untuk setiap node
for node in graph:

    # Menampilkan node dan node yang terhubung
    print(node, "->", graph[node])



# ==========================================================
# Adjacency Matrix
# ==========================================================

# List nama node
nodes = ["Router", "Switch1", "Switch2", "PC1", "PC2", "Server"]


# Membuat adjacency matrix
# Nilai 1 berarti ada hubungan
# Nilai 0 berarti tidak ada hubungan

matrix = [

# R  S1 S2 P1 P2 SV

 # Router terhubung ke Switch1 dan Switch2
 [0, 1, 1, 0, 0, 0],

 # Switch1 terhubung ke Router, Switch2, PC1, dan PC2
 [1, 0, 1, 1, 1, 0],

 # Switch2 terhubung ke Router, Switch1, dan Server
 [1, 1, 0, 0, 0, 1],

 # PC1 hanya terhubung ke Switch1
 [0, 1, 0, 0, 0, 0],

 # PC2 hanya terhubung ke Switch1
 [0, 1, 0, 0, 0, 0],

 # Server hanya terhubung ke Switch2
 [0, 0, 1, 0, 0, 0]
]


# Menampilkan adjacency matrix
print("\nAdjacency Matrix:\n")


# Perulangan untuk setiap baris matrix
for row in matrix:

    # Menampilkan isi baris matrix
    print(row)



# ==========================================================
# Nama Node dan Hubungan Antar Node
# ==========================================================

# Menampilkan judul output
print("\nHubungan Antar Node:\n")


# Membuat set kosong
# untuk mencegah edge tercetak dua kali
sudah_dicetak = set()


# Perulangan setiap node
for node in graph:

    # Perulangan node tetangga
    for neighbor in graph[node]:

        # Mengurutkan pasangan node
        # agar hubungan dianggap sama
        # contoh:
        # Router-Switch1 sama dengan Switch1-Router
        edge = tuple(sorted([node, neighbor]))


        # Jika edge belum pernah dicetak
        if edge not in sudah_dicetak:

            # Menampilkan hubungan antar node
            print(node, "<->", neighbor)

            # Menyimpan edge ke set
            sudah_dicetak.add(edge)