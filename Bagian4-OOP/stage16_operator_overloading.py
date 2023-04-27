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

# jika ingin mempelajari lebih lanjut tentang "magic methods" folder_name: magic-method