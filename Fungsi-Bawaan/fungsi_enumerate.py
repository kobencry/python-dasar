# -- Fungsi bawaan python --

# https://docs.python.org/3/library/functions.html?#enumerate

# fungsi enumerate() mengambil koleksi (misalnya tuple, list, dll.) dan mengembalikannya sebagai objek enumerate.
# dan menambahkan penghitung sebagai kunci dari objek enumerate (dari awal yang defaultnya adalah 0)
# Kita dapat menggunakan perintah enumerate jika ingin mendapatkan keterangan indeks dalam 
# proses iterasi terhadap suatu type list, tuple.

# Syntax
# enumerate(iterable, start)

# Nilai Parameter
# Parameter             Deskripsi
# iterable              Objek yang dapat diulang
# start                 Sebuah angka. Menentukan nomor awal dari objek enumerasi. Default/Standar 0

nama = ('alice', 'carl', 'eliot')
for i in enumerate(nama):
    print(i)
# (0, 'alice')
# (1, 'carl')
# (2, 'eliot')

# Saat Anda menggunakan fungsi enumerate(), mengembalikan dua variabel loop
# key jumlah iterasi saat ini
# val item pada iterasi saat ini
for key, val in enumerate(nama):
    print(key, val)
# 0 alice
# 1 carl
# 2 eliot

# jika anda ingin jumlah nilai dimulai dari 1 bukan 0
# menggunakan parameter start pada fungsi enumerate()
for nomor, nama in enumerate(nama, start=1):
    print(nomor, nama)
# 1 alice
# 2 carl
# 3 eliot

# menggunakan kode dengan cara biasa
listku = ['alice', 'carl', 'eliot']
nomor = 0
for nama in listku:
    # nomor = nomor + 1
    # kode ini setara dengan di atas
    nomor += 1
    print(nomor, nama)
# 1 alice
# 2 carl
# 3 eliot

# Catatan: anda bisa mengabaikan variabel loop 'key' untuk dicetak.
#for _, val in enumerate(iterable):
#    print(val)
