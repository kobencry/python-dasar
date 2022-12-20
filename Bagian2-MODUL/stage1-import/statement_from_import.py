# Peringatan: Secara default python akan membuat folder __pycache__ tidak perlu khawatirkan folder tersebut abaikan saja.
# Jika ingin mengetahui tentang folder__pycache__ kunjungi file.txt

# Import statement adalah perintah yang digunakan dalam bahasa pemrograman Python 
# untuk mengimport modul atau paket yang telah dibuat oleh orang lain atau
# yang telah tersedia di Python Standard Library. 
# Import statement juga dapat digunakan untuk mengimport fungsi, kelas, atau variabel dari modul atau paket tersebut.

# Syntax
# import <nama_modul>

# Cara menggunakannya
# nama_modul.nama_fungsi()

# contoh ini menggunakan file matematika.py anda bisa melihat isi kode programnya.
import matematika

# menggunakan fungsi tambah() dalam modul matematika
print(matematika.tambah(2, 3))  # 5

# menggunakan fungsi kali() dalam modul matematika
print(matematika.kali(2, 10))   # 20

# menggunakan fungsi bagi() dalam modul matematika
print(matematika.bagi(10, 2))   # 5

# menampilkan pesan error
print(matematika.bagi(10, 0))
# (!) Error: integer division or modulo by zero

# menggunakan keywrod as 'alias' untuk singkatan dari nama modul matematika
import matematika as mtk

print(mtk.tambah(10, 20))   # 30

print(mtk.kali(2, 5))   # 10


#==========================================================================

# Keyword from adalah sebuah perintah yang digunakan dalam import statement di Python
# untuk mengimport modul atau bagian spesifik dari modul. 
# Keyword ini memungkinkan Anda untuk mengambil bagian spesifik dari modul
# dan menggunakannya dalam program Anda tanpa perlu menyebut nama modul setiap 
# kali Anda ingin menggunakan bagian tersebut.

# Syntax
# from nama_modul import nama_fungsi

# hanya mengimport fungsi tambah()
from matematika import tambah

# anda tidak perlu menggunakan notasi nama_modul.nama_fungsi()
# cukup memanggil nama fungsinya.
print(tambah(10, 20))   # 30

# jika anda ingin menggunakan nama fungsi lain dari modul matematika
from matematika import tambah, kurang, kali, bagi

# memanggil fungsi kurang() dalam modul matematika
print(kurang(10, 5))  # 5

# memanggil fungsi kali() dalam modul matematika
print(kali(2, 3))   # 6

# menggunakan tanda '*' bintang untuk memanggil semua fungsi dari modul matematika.
from matematika import *

print(tambah(100, 200)) # 300

print(kurang(10, 2))    # 8

# Catatan:
# Import statement dengan tanda bintang * di Python digunakan untuk mengimport semua 
# fungsi, variabel, dan objek dari suatu modul ke dalam program Python. 
# Penggunaan tanda bintang * pada import statement dianggap kurang disarankan karena 
# dapat menyebabkan konflik nama dan membuat kode menjadi tidak terbaca.

# Salah satu alasan mengapa tidak disarankan menggunakan tanda bintang * pada import statement
# adalah karena mengimport semua fungsi, variabel, dan objek dari modul ke dalam program dapat 
# membuat program menjadi lebih berat dan lebih sulit dioptimalkan. 
# Selain itu, penggunaan tanda bintang * juga dapat menyebabkan konflik nama dengan 
# fungsi, variabel, atau objek yang sudah ada di program, sehingga dapat menyebabkan error atau masalah lainnya.

# Untuk menghindari masalah tersebut, lebih disarankan untuk mengimport 
# fungsi, variabel, atau objek yang spesifik saja dari modul yang diperlukan, 
# sehingga program menjadi lebih terstruktur dan mudah dibaca.
