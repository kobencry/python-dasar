# Operator overloading dalam konsep OOP Python adalah kemampuan untuk mendefinisikan 
# perilaku operator yang berbeda pada objek yang berbeda dalam sebuah kelas. 
# Ini berarti kita dapat mendefinisikan cara objek dalam sebuah kelas bereaksi terhadap operator tertentu 
# seperti operator penjumlahan (+), operator perkalian (*), dan operator lainnya.

# Dalam Python, operator overloading dapat dilakukan dengan mendefinisikan method-method khusus 
# yang disebut "magic methods" atau "dunder methods" (double underscore methods) 
# dengan nama yang sesuai dengan operator yang ingin di-overload. 
# Misalnya, untuk operator penjumlahan (+), kita dapat mendefinisikan method add() pada kelas objek. 
# Ketika operator diaplikasikan pada objek dari kelas tersebut, Python akan memanggil method add() 
# yang telah didefinisikan dalam kelas tersebut.

# Berikut adalah beberapa contoh operator overloading dalam konsep OOP Python:
# Operator penjumlahan (+) - Untuk menambahkan dua objek dalam kelas, kita dapat mendefinisikan method add() pada kelas objek.
# Operator kurang (-) - Untuk mengurangi dua objek dalam kelas, kita dapat mendefinisikan method sub() pada kelas objek.
# Operator perkalian (*) - Untuk mengalikan dua objek dalam kelas, kita dapat mendefinisikan method mul() pada kelas objek.
# Operator pembagian (/) - Untuk membagi dua objek dalam kelas, kita dapat mendefinisikan method truediv() pada kelas objek.
# Dengan menggunakan operator overloading, kita dapat membuat kode Python lebih intuitif dan mudah dibaca, 
# serta memungkinkan kita untuk menyesuaikan perilaku operator pada objek sesuai dengan kebutuhan.

# kunjungi dokumentasi python: https://docs.python.org/3/reference/datamodel.html

# jika tidak menggunakan operator overloading
# class A:
#     # inisialisasi
#     def __init__(self, angka):
#         # variabel instance
#         self.angka = angka

# membuat objek
# obj1 = A(10)
# obj2 = A(10)

# print(obj1 + obj2)
# Output:
# TypeError: unsupported operand type(s) for +: 'A' and 'A'

# menggunakan operator overloading
class A:
    # inisialisasi
    def __init__(self, angka):
        self.angka = angka
    
    # operator overloading +
    def __add__(self, objek):
        return A(self.angka + objek.angka)

# membuat objek
obj1 = A(10)
obj2 = A(10)
obj3 = obj1 + obj2
print(obj3.angka)
# Output:
# 20

print(obj2.angka + 20)
# Output:
# 30 

print(obj1 == obj2)
# Output:
# False

# kita akan menambahkan operator overloading
# menggunakan operator overloading __eq__ atau ==
class A:
    # inisialisasi
    def __init__(self, angka):
        self.angka = angka
    
    # operator overloading +
    def __add__(self, objek):
        return A(self.angka + objek.angka)

    # operator overloading ==
    def __eq__(self, objek):
       return self.angka == objek.angka
   
    # menampilkan objek string
    def __str__(self):
        return f"{self.angka}"

obj1 = A(10)
obj2 = A(10)
print(obj1 == obj2)
# Output:
# True

# contoh implementasi operator overloading pada kelas Mahasiswa untuk menambahkan nilai bonus IPK pada objek Mahasiswa:
class Mahasiswa:
    # menginisialisasi
    def __init__(self, nama, jurusan, ipk):
        # variabel instance
        self.nama = nama
        self.jurusan = jurusan
        self.ipk = ipk
    
    # method instance
    def display(self):
        return f"Nama:{self.nama}, Jurusan:{self.jurusan}, IPK:{self.ipk}"
    
    # method operator overloading +
    def __add__(self, bonus):
        ipk_baru = self.ipk + bonus
        return Mahasiswa(self.nama, self.jurusan, ipk_baru)

# membuat objek mahasiswa
alice = Mahasiswa("alice", "Teknik Informatika", 2.7)
carl = Mahasiswa("carl", "Teknik Informatika", 2.6)
print("-- sebelum --")
print(alice.display())
print(carl.display())
# Output:
# -- sebelum --
# Nama:alice, Jurusan:Teknik Informatika, IPK:2.7
# Nama:carl, Jurusan:Teknik Informatika, IPK:2.6

print("-- setelah --")
alice = alice + 0.5
print(alice.display())
carl = carl + 0.4
print(carl.display())
# Output:
# -- setelah --
# Nama:alice, Jurusan:Teknik Informatika, IPK:3.2
# Nama:carl, Jurusan:Teknik Informatika, IPK:3.0

# jika ingin mempelajari lebih lanjut tentang "magic methods" folder_name: magic-method