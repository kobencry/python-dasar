# Dalam Python, magic method __imul__ adalah method khusus dalam Python
# yang digunakan untuk mengimplementasikan operasi perkalian dan penugasan *= pada suatu objek.
# method ini memungkinkan Anda untuk menentukan perilaku perkalian dan penugasan kustom pada objek Anda.

# Deskripsi:
# method __imul__ digunakan untuk mengimplementasikan operasi perkalian dan penugasan *= pada objek.
# method ini memodifikasi objek saat ini dengan menambahkanya dengan objek yang diberikan.

# Syntax:
# def __imul__(self, other):
    # Implementasikan operasi perkalian dan penugasan dalam tempat pada objek

# Parameter:
# self: Merujuk pada objek saat ini.
# other: objek yang akan dikalikan ke objek saat ini.
# nama parameter "other" bisa diganti dengan nama apapun

# Berikut adalah contoh penggunaan magic method __imul__ dalam sebuah kelas:
class Menghitung:
    def __init__(self, nilai):
        self.nilai = nilai
    
    def __imul__(self, other):
        # Jika objek other juga merupakan objek dari kelas Menghitung
        if isinstance(other, Menghitung):
            self.nilai *= other.nilai
            return self
        # Jika objek other bukan merupakan objek dari kelas Menghitung, 
        # kita asumsikan bahwa other adalah objek lain (tipe data apapun).
        else:
            self.nilai *= other
            return self

# membuat objek Menghitung
x = Menghitung(5)
y = Menghitung(2)

# perkalian dan penugasan antara dua objek x dengan y dari kelas Menghitung
x *= y
print(x.nilai)
# Output:
# 10

# perkalian dan penugasan antara dua objek x dengan bilangan bulat
x *= 10
print(x.nilai)
# Output:
# 100