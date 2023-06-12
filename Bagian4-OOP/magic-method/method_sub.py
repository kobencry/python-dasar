# Magic method __sub__ adalah method khusus dalam Python
# yang digunakan untuk mengimplementasikan operasi pengurangan (-) pada objek.
# method ini memungkinkan objek untuk berperilaku seperti tipe data bawaan yang mendukung operasi pengurangan.

# Syntax:
# __sub__(self, other)
# Metode __sub__ dijalankan ketika operator - digunakan pada objek.
# Metode ini menerima dua parameter: self (objek saat ini) dan other (objek yang dikurangkan).
# nama parameter "other" bisa diganti dengan nama apapun 

# Ketika Anda menggunakan operator pengurangan (-) antara dua objek,
# Python akan mencari dan memanggil magic method __sub__ pada objek pertama,
# dan meneruskan objek kedua sebagai argumen.
# method ini harus mengembalikan hasil pengurangan objek tersebut.

# Berikut adalah contoh penggunaan magic method __sub__ pada suatu kelas:

class Kurang:
    def __init__(self, nilai):
        self.nilai = nilai

    def __sub__(self, other):
        return Kurang(self.nilai - other.nilai)

# membuat objek Kurang
obj1 = Kurang(50)
obj2 = Kurang(30)

hasil = obj1 - obj2
print(hasil.nilai)
# Output:
# 20

# membuat objek Kurang menggunakan tipe data string dan set
obj1 = Kurang({'alice', 'carl', 'eliot'})
obj2 = Kurang({'carl'})

hasil = obj1 - obj2
print(hasil.nilai)
# Output:
# {'eliot', 'alice'}

# Contoh menggunakan 2 attribute
class Kurang:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Kurang(self.x - other.x, self.y - other.y)

# membuat objek Kurang
obj1 = Kurang(50, 20)
obj2 = Kurang(5, 2)

# mengurangi objek dari obj1.x dengan obj1.y
hasil = obj1.x - obj1.y
print(hasil)
# Output:
# 30

# mengurangi objek dari obj1 dengan obj2
hasil = obj1 - obj2
print(hasil.x)
# Output:
# 45

print(hasil.y)
# Output:
# 18
