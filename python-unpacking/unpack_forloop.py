# unpacking/membongkar Forloop

# Kita juga dapat menggunakan iterable unpacking dalam konteks for loop.
# Saat kita menjalankan perulangan for, perulangan tersebut menetapkan satu 
# item iterable-nya ke variabel target di setiap iterasi.
# Jika item yang akan ditugaskan adalah iterable, maka kita bisa menggunakan tupel variabel target.
# Loop akan unpacking/membongkar iterable yang ada ke dalam tuple variabel target.

# Sebagai contoh, misalkan kita memiliki file yang berisi tentang
# data mahasiswa atau data penjualan suatu perusahaan sebagai berikut:

# data mahasiswa
mahasiswa = [('alice', 23, 'jakarta'), ('carl', 26, 'bandung'), ('eliot', 20, 'surabaya')]

# contoh biasa
# for mhs in mahasiswa:
#     print(f"nama:{mhs[0]} usia:{mhs[1]} alamat:{mhs[2]}")

# contoh unpacking
for nama, usia, alamat in mahasiswa:
    print(f"nama:{nama} usia:{usia} alamat:{alamat}")

# nama:alice usia:23 alamat:jakarta
# nama:carl usia:26 alamat:bandung
# nama:eliot usia:20 alamat:surabaya

# data penjualan
penjualan = [('buku', 2500, 50), ('pensil', 1500, 25), ('penggaris', 2000, 10)]

for produk, harga, terjual in penjualan:
    print(f"pendapatan untuk {produk} adalah {harga * terjual}")
# pendapatan untuk buku adalah 125000
# pendapatan untuk pensil adalah 37500
# pendapatan untuk penggaris adalah 20000

# Dimungkinkan juga untuk menggunakan operator * dalam forloop untuk 
# mengemas beberapa item dalam satu variabel target:
for x, *y in [(1, 2, 3), (4, 5, 6, 7), (8, 9), (10, 20, 30)]:
    print(f"variabel x: {x}")
    print(f"variabel y: {y}")
# variabel x: 1
# variabel y: [2, 3]
# variabel x: 4
# variabel y: [5, 6, 7]
# variabel x: 8
# variabel y: [9]
# variabel x: 10
# variabel y: [20, 30]
# Dalam hal ini forloop, kita menangkap elemen pertama dari setiap urutan x.
# Kemudian operator * menangkap daftar nilai dalam y variabel targetnya.

dataku = [(('alice', 23), 'jakarta'), (('carl', 22), 'bandung'), (('eliot', 26), 'surabaya')]
for (nama, usia), alamat in dataku:
    print(nama, usia, alamat)
# alice 23 jakarta
# carl 22 bandung
# eliot 26 surabaya

# struktur variabel target harus sesuai dengan struktur iterable.
# Jika tidak, kita akan mendapatkan pesan kesalahan ValueError. 
# Lihatlah contoh berikut:
for nama, usia, alamat in dataku:
    print(nama, usia, alamat)
# Traceback (most recent call last):
#   File "unpack_forloop.py", line 62, in <module>
#     for nama, usia, alamat in dataku:
# ValueError: not enough values to unpack (expected 3, got 2)
