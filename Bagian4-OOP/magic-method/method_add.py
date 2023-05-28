# Magic method __add__ adalah method khusus dalam Python
# yang digunakan untuk mengimplementasikan operasi penjumlahan (+) pada objek.
# method ini memungkinkan objek untuk berperilaku seperti tipe data bawaan yang mendukung operasi penjumlahan.

# Ketika Anda menggunakan operator penjumlahan (+) antara dua objek,
# Python akan mencari dan memanggil magic method __add__ pada objek pertama,
# dan meneruskan objek kedua sebagai argumen.
# method ini harus mengembalikan hasil penjumlahan objek tersebut.

# Berikut adalah contoh penggunaan magic method __add__ pada suatu kelas:

class Tambah:
    def __init__(self, nilai):
        self.nilai = nilai

    def __add__(self, other):
        return Tambah(self.nilai + other.nilai)

x = Tambah(10)
y = Tambah(20)

hasil = x + y

print(hasil.nilai)
# Output:
# 30

# menggunakan tipe data string dan list
nama1 = Tambah(['alice', 'carl'])
nama2 = Tambah(['eliot', 'geral', 'hello world'])

hasil = nama1 + nama2
print(hasil.nilai)
# Output:
# ['alice', 'carl', 'eliot', 'geral', 'hello world']


class Tambah:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Tambah(self.x + other.x, self.y + other.y)

obj1 = Tambah(1, 2)
obj2 = Tambah(40, 60)

# menjumlahkan objek dari obj1.x dengan obj1.y
hasil = obj1.x + obj1.y
print(hasil)
# Output:
# 3

# menjumlahkan objek dari obj2.x dengan obj2.y
hasil = obj2.x + obj2.y
print(hasil)
# Output:
# 100

# menjumlahkan objek dari obj1 dengan obj2 
hasil = obj1 + obj2
print(hasil.x)
# Output:
# 41

print(hasil.y)
# Output:
# 62
