# Magic method __mul__ adalah method khusus dalam Python
# yang digunakan untuk mengimplementasikan operasi perkalian (*) pada objek.
# method ini memungkinkan objek untuk berperilaku seperti tipe data bawaan yang mendukung operasi perkalian.

# Ketika Anda menggunakan operator perkalian (*) antara dua objek,
# Python akan mencari dan memanggil magic method __mul__ pada objek pertama,
# dan meneruskan objek kedua sebagai argumen.
# method ini harus mengembalikan hasil perkalian objek tersebut.

# Berikut adalah contoh penggunaan magic method __mul__ pada suatu kelas:

class Kali:
    def __init__(self, nilai):
        self.nilai = nilai

    def __mul__(self, other):
        return Kali(self.nilai * other.nilai)

# membuat objek Kali
obj1 = Kali(2)
obj2 = Kali(3)

# mengalikan dari kedua objek
hasil = obj1 * obj2
print(hasil.nilai)
# Output:
# 6

# Contoh menggunakan  2 attribute
class Kali:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, other):
        return Kali(self.x * other.x, self.y * other.y)

# membuat objek Kali
obj1 = Kali(2, 3)
obj2 = Kali(5, 6)

# mengalikan  objek dari obj1.x dengan obj1.y
hasil = obj1.x * obj1.y
print(hasil)
# Output:
# 6

# mengalikan objek dari obj1 dengan obj2
hasil = obj1 * obj2
print(hasil.x)
# Output:
# 10

print(hasil.y)
# Output:
# 18
