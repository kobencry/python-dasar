# Magic method __floordiv__ adalah method khusus dalam Python 
# yang digunakan untuk mengimplementasikan operasi pembagian bulat (floor division) (//) pada objek.
# method ini memungkinkan objek untuk berperilaku seperti tipe data bawaan yang mendukung operasi pembagian bulat.

# Ketika Anda menggunakan operator pembagian bulat (//) antara dua objek,
# Python akan mencari dan memanggil magic method __floordiv__ pada objek pertama,
# dan meneruskan objek kedua sebagai argumen. 
# method ini harus mengembalikan hasil pembagian bulat objek tersebut.

# Berikut adalah contoh penggunaan magic method __floordiv__ pada suatu kelas:

class Floordiv:
    def __init__(self, nilai):
        self.nilai = nilai

    def __floordiv__(self, other):
        return Floordiv(self.nilai // other.nilai)

# membuat objek Floordiv
obj1 = Floordiv(10)
obj2 = Floordiv(2)

hasil = obj1 // obj2
print(hasil)
# Output:
# 
