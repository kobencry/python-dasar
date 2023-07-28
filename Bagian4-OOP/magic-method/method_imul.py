# Dalam Python, magic method __imul__ adalah method khusus dalam Python
# yang digunakan untuk mengimplementasikan operasi perkalian dan penugasan *= pada suatu objek.
# method ini memungkinkan Anda untuk menentukan perilaku perkalian dan penugasan kustom pada objek Anda.

# Deskripsi:
# method __imul__ digunakan untuk mengimplementasikan operasi perkalian dan penugasan *= pada objek.
# method ini memodifikasi objek saat ini dengan menambahkanya dengan objek yang diberikan.

# Syntax:
# def __imul__(self, other):
    # Implementasikan operasi penggandaan dalam tempat pada objek

# Parameter:
# self: Merujuk pada objek saat ini.
# other: Merupakan objek kedua yang akan digunakan untuk operasi penggandaan.
# nama parameter "other" bisa diganti dengan nama apapun

class Menghitung:
    def __init__(self, nilai):
        self.nilai = nilai
    
    def __imul__(self, other):
        if isinstance(other, Menghitung):
            return self.nilai * other.nilai
        else:
            return self.nilai * other