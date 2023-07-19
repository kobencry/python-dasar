# Dalam Python, magic method __add__() adalah Method khusus yang digunakan 
# untuk mengimplementasikan operator penjumlahan + pada suatu objek. 
# Method ini memungkinkan Anda untuk menentukan perilaku penjumlahan antara dua objek.

# Ketika operator + digunakan untuk menjumlahkan dua objek, 
# Python secara otomatis memanggil Method __add__() pada objek yang pertama, 
# dan mengirimkan objek kedua sebagai argumen. 
# Method ini harus mengembalikan hasil penjumlahan objek tersebut.

# Deskripsi:
# Method __add__() digunakan untuk mengimplementasikan operator penjumlahan +. 
# Method ini harus mengembalikan hasil penjumlahan objek saat ini dengan objek kedua.

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
        # Jika objek other juga merupakan objek dari kelas Mahasiswa 
        if isinstance(other, Tambah):
            return self.nilai + other.nilai
        
        # Jika objek other bukan merupakan objek Mahasiswa,
        # kita asumsikan bahwa other adalah objek lain (tipe data apapun).
        else:
            return self.nilai + other

# membuat objek Tambah
x = Tambah(10)
y = Tambah(20)

# menjumlahkan antara dua objek x dengan y dari kelas Tambah
hasil = x + y

print(hasil)
# Output:
# 30

# menggunakan tipe data list yang berisi string
nama1 = Tambah(['alice', 'carl'])
nama2 = Tambah(['eliot', 'geral', 'hello world'])

# menambahkan antara dua objek nama1 dengan nama2 dari kelas Tambah
hasil = nama1 + nama2
print(hasil)
# Output:
# ['alice', 'carl', 'eliot', 'geral', 'hello world']

# membandingkan dengan cara penggunaan magic method __add__()
# Syntax:
# object.__add__(object/value)

hasil = x.__add__(y)
print(hasil)
# Output:
# 30

hasil = nama1.__add__(nama2)
print(hasil)
# Output:
# ['alice', 'carl', 'eliot', 'geral', 'hello world']

# Contoh penggunaan magic method __add__() dengan 2 atribut
class Tambah:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Jika objek other juga merupakan objek dari kelas Mahasiswa
        if isinstance(other, Tambah):
            return Tambah(self.x + other.x, self.y + other.y)
        
        # Jika objek other bukan merupakan objek Mahasiswa,
        # kita asumsikan bahwa other adalah objek lain (tipe data apapun).
        else:
            return Tambah(self.x + other, self.y + other)

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

# membandingkan dengan cara penggunaan magic method __add__()
# Syntax:
# object.__add__(object/value)

hasil = obj1.__add__(obj2)
print(hasil.x)
# Output:
# 41

print(hasil.y)
# Output:
# 62