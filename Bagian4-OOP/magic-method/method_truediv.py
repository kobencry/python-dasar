# Magic method __truediv__ adalah method khusus dalam Python 
# yang digunakan untuk mendefinisikan perilaku operasi pembagian sejati (/) antara objek. 
# Ketika kita menggunakan operator / antara dua objek, 
# Python akan mencari dan menggunakan method __truediv__ untuk menentukan hasil pembagian tersebut.

# Deskripsi:
# Method __add__() digunakan untuk mengimplementasikan operator penjumlahan +. 
# Method ini harus mengembalikan hasil penjumlahan objek saat ini dengan objek kedua.


# Syntax:

# nama parameter "other" bisa diganti dengan nama apapun 

# Ketika method __truediv__ didefinisikan dalam sebuah kelas, 
# kita dapat mengontrol bagaimana objek dari kelas tersebut berperilaku saat dibagi dengan objek lain.
# Kita dapat mengimplementasikan method __truediv__ untuk melakukan operasi pembagian sejati 
# sesuai dengan kebutuhan aplikasi atau kelas yang kita definisikan.

# Berikut adalah contoh penggunaan method __truediv__ dalam sebuah kelas:
class TrueDiv:
    def __init__(self, nilai):
        self.nilai = nilai

    def __truediv__(self, other):
        return TrueDiv(self.nilai / other.nilai)

# membuat objek TrueDiv
obj1 = TrueDiv(10)
obj2 = TrueDiv(2)

# membagi antara dua objek obj1 dengan obj2
hasil = obj1 / obj2
print(hasil.nilai)
# Output:
# 5.0

# Berikut adalah contoh penggunaan magic method __truediv__() dengan 2 atribut
class Fraction:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __truediv__(self, other):
        return Fraction(self.x / other.x, self.y / other.y)

# membuat objek Fraction
obj1 = Fraction(100, 20)
obj2 = Fraction(2, 5)

# membagi objek dari obj1.x dengan obj1.y
hasil = obj1.x / obj1.y # 100 / 20
print(hasil)
# Output:
# 5.0

# membagi objek dari obj1 dengan obj2
hasil = obj1 / obj2
print(hasil.x)
# Output:
# 50.0

print(hasil.y)
# Output:
# 4.0