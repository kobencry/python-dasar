# -- Fungsi bawaan python --

# https://docs.python.org/3/library/functions.html?#zip

# fungsi zip() mengembalikan objek zip, yang merupakan iterator tupel di mana 
# item pertama di setiap iterator yang diteruskan dipasangkan bersama, 
# dan kemudian item kedua di setiap iterator yang diteruskan dipasangkan bersama, dll.

# Jika iterator yang diteruskan memiliki panjang yang berbeda,
# iterator dengan item paling sedikit akan menentukan panjang iterator baru.

# Syntax
# zip(iterator1, iterator2, iterator3, ...dst)

# Nilai Parameter
# Parameter                 Deskripsi
# iterator1,                Objek Iterator yang akan digabungkan bersama
# iterator2,
# iterator3, ...dst

# menggabungkan dua tuple bersama-sama
nama = ('alice', 'carl', 'eliot')
usia = (23, 22, 20)

hasil = zip(nama, usia)
print(hasil)        # <zip object at 0x0000021E54A1A580>
print(tuple(hasil)) # (('alice', 23), ('carl', 22), ('eliot', 20))

# menggabungkan tiga list bersama-sama
nama = ['alice', 'carl', 'eliot']
usia = [23, 22, 20]
alamat = ['jakarta', 'bandung', 'surabaya']

hasil = list(zip(nama, usia, alamat))
print(hasil)  # [('alice', 23, 'jakarta'), ('carl', 22, 'bandung'), ('eliot', 20, 'surabaya')]

# menggunakan forloop untuk menampilkan data
nama = ['alice', 'carl', 'eliot']
usia = (20, 22, 24)
alamat = ['jakart', 'bandung', 'surabaya']

for x, y, z in zip(nama, usia, alamat):
    print(f"nama:{x} usia:{y} alamat:{z}")
# nama:alice usia:20 alamat:jakart
# nama:carl usia:22 alamat:bandung
# nama:eliot usia:24 alamat:surabaya

# jika panjang item berbeda maka item tersebut diabaikan
nama = ('alice', 'carl', 'eliot')
usia = (23, 20)

hasil = zip(nama, usia)
print(hasil)        # <zip object at 0x0000019F2334AEC0>
print(tuple(hasil)) # (('alice', 23), ('carl', 20))
# lihat item 'eliot' diabaikan

# menggunakan tipe dict
x = ['nama', 'usia', 'alamat']
y = ['alice', 23, 'jakarta']

hasil = dict(zip(x, y))
print(hasil)    # {'nama': 'alice', 'usia': 23, 'alamat': 'jakarta'}

# anda dapat menggunakan operator * untuk unpack
dataku = [('nama', 'alice'), ('usia', 23), ('alamat', 'jakarta')]
x, y = zip(*dataku)
print(x)    # ('nama', 'usia', 'alamat')
print(y)    # ('alice', 23, 'jakarta')
