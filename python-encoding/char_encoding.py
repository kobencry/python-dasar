# Karakter encoding adalah representasi unik dari setiap karakter dalam sebuah sistem komputer.
# Karakter encoding digunakan untuk mengubah karakter fisik seperti 
# huruf, angka, dan simbol menjadi representasi numerik yang dapat diterima oleh komputer.
# Beberapa contoh dari karakter encoding yang umum digunakan adalah ASCII, UTF-8, UTF-16, dan ISO-8859.
# ASCII adalah encoding karakter yang paling dasar yang hanya menyediakan 128 karakter, termasuk huruf, angka, dan simbol.
# UTF-8 dan UTF-16 adalah encoding karakter yang lebih canggih yang dapat menyimpan lebih banyak karakter, termasuk karakter non-latin.
# ISO-8859 adalah keluarga encoding karakter yang digunakan untuk bahasa Eropa.
# Karakter encoding digunakan dalam berbagai aplikasi, seperti pemrograman, jaringan, dan sistem operasi.
# Dalam pemrograman, encoding karakter digunakan untuk mengubah string atau file dari satu format karakter ke format karakter lain.
# Dalam jaringan, encoding karakter digunakan untuk mengubah data yang diterima dari jaringan menjadi format yang dapat diterima oleh sistem.

# Decoding karakter adalah proses mengubah representasi numerik karakter yang disimpan dalam sistem komputer
# kembali menjadi karakter fisik seperti huruf, angka, dan simbol. 
# Ini sering dilakukan saat membaca atau menerima data yang dikodekan dalam format tertentu, 
# seperti file teks atau data jaringan.
# Dengan menggunakan fungsi decoding, kita dapat mengubah data tersebut menjadi format 
# yang dapat diterima oleh program kita seperti Unicode atau ASCII. 
# Ini memungkinkan program kita untuk memproses dan menggunakan data dengan benar.

# kunjungi dokumentasi python https://docs.python.org/3/library/codecs.html#standard-encodings

# Encoding dan decoding adalah proses berpindah dari satu ke yang lain:
# Gambaran karakter encoding dan decoding

#                   b = s.encode("utf-8")
#           .-----------------------------------.
#           |                                   |
#           |                                   |
#           |                                   V
#  .---------------------.         .----------------------------.
#  | s = "hello world✨" |         | b'hello world\xe2\x9c\xa8' |
#  '---------------------'         '----------------------------'
#           A                                   |
#           |                                   |
#           |                                   |
#           '-----------------------------------'
#                   s = b.decode("utf-8") 

# Contoh program encode() dan decode()
s = "hello world✨"
b = s.encode("utf-8")
print(b)    # b'hello world\xe2\x9c\xa8'
s = b.decode("utf-8")
print(s)    # hello world✨

s = "😀"
b = s.encode("utf-8")
print(b)    # b'\xf0\x9f\x98\x80'
s = b.decode("utf-8")
print(s)    # 😀
# secara default encoding decoding di os windows menggunakan "cp1252"