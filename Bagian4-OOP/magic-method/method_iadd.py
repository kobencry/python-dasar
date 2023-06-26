# Dalam Python, magic method __iadd__() adalah metode khusus dalam Python 
# yang digunakan untuk mengimplementasikan operasi penjumlahan dan penugasan += pada suatu objek.
# Metode ini memungkinkan Anda untuk menentukan perilaku penjumlahan dan penugasan kustom pada objek Anda.

# Definisi:
# Metode __iadd__() digunakan untuk mengimplementasikan operasi penjumlahan dan penugasan += pada objek. 
# Metode ini memodifikasi objek saat ini dengan menambahkannya dengan objek yang diberikan.

# Syntax:
# def __iadd__(self, other):
#   Implementasi logika penjumlahan dan penugasan

# Parameter:
# self: Merujuk pada objek saat ini.
# other: Objek yang akan ditambahkan ke objek saat ini.

# Contoh penggunaan magic method __iadd__():
class Menghitung:
    def __init__(self, nilai):
        self.nilai = nilai
    
    def __iadd__(self, other):
        # Jika objek other juga merupakan objek dari kelas Mahasiswa
        if isinstance(other, Menghitung):
            self.nilai += other.nilai
            return self
        
        # Jika objek other bukan merupakan objek Mahasiswa, 
        # kita asumsikan bahwa other adalah objek lain (tipe data apapun).
        else:
            self.nilai += other
            return self

# membuat objek Menghitung
x = Menghitung(5)
y = Menghitung(10)

# penjumlahan dan penugasan antara dua objek x dengan y dari kelas Menghitung
x += y
print(x.nilai)
# Output:
# 15

# penjumlahan dan penugasan antara dua objek x dengan bilangan bulat
x += 5
print(x.nilai)
# Output:
# 20

# membuat objek Menghitung
obj = Menghitung(2)
