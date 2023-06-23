# Dalam Python, magic method __add__() adalah metode khusus yang digunakan 
# untuk mengimplementasikan operator penjumlahan + pada suatu objek. 
# Metode ini memungkinkan Anda untuk menentukan perilaku penjumlahan antara dua objek.

# Ketika operator + digunakan untuk menjumlahkan dua objek, 
# Python secara otomatis memanggil metode __add__() pada objek yang pertama, 
# dan mengirimkan objek kedua sebagai argumen. 
# Metode ini harus mengembalikan hasil penjumlahan objek tersebut.

# Deskripsi:
# Metode __add__() digunakan untuk mengimplementasikan operator penjumlahan +. 
# Metode ini harus mengembalikan hasil penjumlahan objek saat ini dengan objek kedua.

# Syntax:
# def __add__(self, other):
    # Implementasi logika penjumlahan

# Parameter:
# self: Merujuk pada objek saat ini.
# other: Merupakan objek kedua yang akan dijumlahkan dengan objek saat ini.
# nama parameter "other" bisa diganti dengan nama apapun 

# Contoh penggunaan magic method __add__():
class Tambah:
    def __init__(self, nilai):
        self.nilai = nilai

    def __add__(self, other):
        return Tambah(self.nilai + other.nilai)

# membuat objek Tambah
x = Tambah(10)
y = Tambah(20)

# menjumlahkan dari kedua objek
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


# Contoh menggunakan 2 attribute
class Tambah:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Tambah(self.x + other.x, self.y + other.y)

# membuat objek Tambah
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