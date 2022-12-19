# Iterator adalah sebuah object yang menyimpan informasi tentang 
# proses iterasi (perulangan) pada sebuah object yang mendukung iterasi. 
# Di Python, objek yang mendukung iterasi disebut "iterable", dan objek 
# yang menyimpan informasi tentang proses iterasi disebut "iterator".

# Sebagai contoh, objek seperti list, tuple, dan dictionary adalah 
# objek yang mendukung iterasi, dan kita dapat mengiterasi objek tersebut
# dengan menggunakan perintah for atau dengan memanggil method __iter__ pada object tersebut.

# Berikut ini adalah contoh kode menggunakan iterator di Python:
# membuat objek iterable dari tipe list
listku = ['alice', 20, False, 'jakarta']

# membuat objek iterator dari objek iterable
obj_iterator = iter(listku)

print(obj_iterator) # <list_iterator object at 0x0000022CDD4C8910>

# menggunakan fungsi next() untuk mengiterasi objek iterator 
print(next(obj_iterator))   # alice
print(next(obj_iterator))   # 20
print(next(obj_iterator))   # False
print(next(obj_iterator))   # jakarta

# membuat objek iterable dari tipe string
s = "hello!"

# membuat objek iterator dari objek iterable
obj_string = iter(s)
print(next(obj_string))     # h
print(next(obj_string))     # e
print(next(obj_string))     # l
print(next(obj_string))     # l
print(next(obj_string))     # o
print(next(obj_string))     # !

# Jika object iterator telah mencapai akhir object iterable, maka perintah next akan menyebabkan exception StopIteration.
# mencoba mengakses element selanjutnya
# print(next(obj_string)) # Akan menyebabkan exception StopIteration

# jika anda ingin mengetahui tentang fungsi-bawaan iter() dan next() kunjungi folder_name: "Fungsi-Bawaan"
