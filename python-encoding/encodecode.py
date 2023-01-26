# Unicode adalah standar internasional untuk menentukan set karakter yang digunakan dalam komputer dan jaringan.
# Unicode menyediakan ruang nomor untuk setiap karakter dari setiap jenis bahasa yang digunakan di dunia. 
# Setiap karakter dalam Unicode memiliki nomor unik yang disebut "kode poin". 
# Unicode memungkinkan kita untuk membuat aplikasi yang dapat menangani berbagai jenis bahasa dan karakter tanpa kesulitan. 
# Unicode digunakan dalam berbagai aplikasi seperti teks editor, browser web, dan aplikasi jaringan.
# Unicode menyediakan beberapa encoding utama yang digunakan seperti UTF-8, UTF-16, UTF-32 
# yang digunakan untuk mengubah karakter Unicode ke dalam format yang dapat dibaca dan ditulis oleh sistem komputer dan jaringan.

# Encoding karakter adalah representasi unik dari setiap karakter dalam sebuah sistem komputer.
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
#           |                                  \|/
#           |                                   V
#  .---------------------.         .----------------------------.
#  | s = "hello world✨" |        |  b'hello world\xe2\x9c\xa8' |
#  '---------------------'         '----------------------------'
#           ^                                   |
#          /|\                                  |
#           |                                   |
#           '-----------------------------------'
#                   s = b.decode("utf-8") 

# Contoh program encode() dan decode()
s = "hello world✨"
b = s.encode("utf-8")
print(b)    # b'hello world\xe2\x9c\xa8'
s = b.decode("utf-8")
print(s)    # hello world✨

# kita harus berhati-hati saat encoding/decoding. 
# Jika kita menggunakan format yang salah, maka akan menghasilkan keluaran yang salah dan dapat menimbulkan kesalahan.
# secara default encoding decoding di python menggunakan "utf-8"

# UTF-8 adalah salah satu pengkodean yang paling umum digunakan, dan secara default python menggunakannya. 
# UTF adalah singkatan dari "Unicode Transformation Format", dan '8' berarti bahwa nilai 8-bit digunakan dalam pengkodean. 
# (Ada juga pengkodean UTF-16 dan UTF-32, tetapi lebih jarang digunakan daripada UTF-8.)
# aturan menggunakan UTF-8  sebagai berikut:
# Jika kode poin < 128, itu diwakili oleh nilai byte yang sesuai.
# Jika kode poin >= 128, itu diubah menjadi urutan dua, tiga, atau empat byte, 
# di mana setiap byte urutannya antara 128 dan 255.

# Apa itu kode point?
# Kode point adalah sebuah angka unik yang digunakan untuk mengidentifikasi sebuah karakter dalam sistem encoding seperti Unicode.
# Setiap karakter Unicode memiliki kode point yang unik, yang digunakan untuk menentukan posisi karakter tersebut dalam tabel karakter Unicode. 
# Kode point dapat dinyatakan dalam bentuk hexadecimal atau decimal, dan dapat digunakan dalam berbagai aplikasi seperti pemrograman dan markup. 
# Contoh kode point dalam Unicode adalah "U+0041" yang menyatakan karakter "A" dalam tabel karakter Unicode.
# kunjungi tabel ascii di file "tabel_ascii.txt"

