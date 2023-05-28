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
        return 
