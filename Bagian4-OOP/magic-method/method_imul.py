# Dalam Python, magic method __imul__ digunakan untuk mengimplementasikan operasi inplace multiplication(penggandaan dalam tempat) pada objek. 
# Ketika objek mendukung operasi penggandaan inplace (dengan menggunakan operator *= ), 
# Python akan mencoba untuk memanggil magic method __imul__ untuk melakukan operasi tersebut.

# Deskripsi:
# Magic method __imul__ digunakan untuk mengimplementasikan operasi penggandaan dalam tempat pada objek.
# Saat objek mendukung operasi inplace multiplication (dengan menggunakan operator *= ), 
# Python akan mencoba untuk memanggil magic method __imul__ pada objek tersebut.

# Syntax:
# def __imul__(self, other):
    # Implementasikan operasi penggandaan dalam tempat pada objek

# Parameter:
# self: Merujuk pada objek saat ini.
# other: Merupakan objek kedua yang akan digunakan untuk operasi penggandaan.