# ASCII (American Standard Code for Information Interchange) adalah standar yang digunakan untuk menentukan set karakter yang digunakan dalam komputer.
# ASCII hanya mencakup 128 karakter yang hanya meliputi karakter yang digunakan dalam bahasa Inggris saja. 
# ASCII menentukan kode point untuk setiap karakter, yang merupakan nomor unik yang digunakan untuk mengidentifikasi karakter tersebut.

# Apa itu kode point?
# Kode point adalah sebuah angka unik yang digunakan untuk mengidentifikasi sebuah karakter dalam sistem encoding seperti Unicode.
# Setiap karakter Unicode memiliki kode point yang unik, yang digunakan untuk menentukan posisi karakter tersebut dalam tabel karakter Unicode. 
# Kode point dapat dinyatakan dalam bentuk hexadecimal atau decimal, dan dapat digunakan dalam berbagai aplikasi seperti pemrograman dan markup. 
# Contoh kode point dalam Unicode adalah "U+0041" atau "\u0041" yang menyatakan karakter "A" dalam tabel karakter Unicode.

# mengembalikan kode point dan karakter ascii
def char_ascii(kode_point: int) -> str:
    for i in range(kode_point):
      print(f"{i:<4} {chr(i)}")
char_ascii(128)
# kunjungi tabel ascii di file "tabel_ascii.txt"

# Unicode adalah standar internasional untuk menentukan set karakter yang digunakan dalam komputer dan jaringan.
# Unicode menyediakan ruang nomor untuk setiap karakter dari setiap jenis bahasa yang digunakan di dunia. 
# Setiap karakter dalam Unicode memiliki nomor unik yang disebut "kode poin". 
# Unicode memungkinkan kita untuk membuat aplikasi yang dapat menangani berbagai jenis bahasa dan karakter tanpa kesulitan. 
# Unicode digunakan dalam berbagai aplikasi seperti teks editor, browser web, dan aplikasi jaringan.
# Unicode menyediakan beberapa encoding utama yang digunakan seperti UTF-8, UTF-16, UTF-32 
# yang digunakan untuk mengubah karakter Unicode ke dalam format yang dapat dibaca dan ditulis oleh sistem komputer dan jaringan.
# kunjungi tabel unicode di "https://en.wikipedia.org/wiki/List_of_Unicode_characters"

# mengembalikan karakter yang sesuai dari kode point karakter unicode
def char_unicode(kode_point: str) -> str:
   return chr(int(kode_point.lstrip("u+").zfill(8), 16)) 
print(char_unicode("u+0041"))  # A
print(char_unicode("u+2728"))  # ✨
print(char_unicode("u+1F600")) # 😀
# jika anda menggunakan os windows �😀 atau 😀

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

# Beberapa format yang paling umum digunakan adalah UTF-8, UTF-16, dan UTF-32.
#-----------------------------------------------------------------------------
# UTF-8 adalah salah satu standar encoding yang digunakan untuk mewakili karakter Unicode. 
# UTF-8 adalah varian dari UTF (Unicode Transformation Format) yang menggunakan satu hingga empat byte untuk mewakili sebuah karakter. 
# UTF-8 sangat populer karena menghemat ruang penyimpanan dan dapat digunakan dengan baik dalam lingkungan yang menggunakan ASCII.
# Keuntungan lain dari UTF-8 adalah mudah diterjemahkan ke dalam kode ASCII yang dapat dibaca oleh komputer yang tidak mendukung Unicode.
# Karena itu, UTF-8 sering digunakan dalam jaringan internet dan sistem file.
# Ini adalah format yang variable-length, yang berarti bahwa setiap karakter Unicode dapat dinyatakan dengan jumlah byte yang berbeda. 
# UTF-8 cocok untuk digunakan dalam situasi di mana karakter yang digunakan cenderung lebih banyak dari karakter yang digunakan dalam ASCII.

s = "hello world✨"
# Hasil s.encode() adalah objek byte. 
# Baik aslinya byte (seperti b'hello world\xe2\x9c\xa8') dan representasi byte hanya mengizinkan karakter ASCII.
# saat memanggil "hello world✨".encode("utf-8"), "hello world" yang kompatibel dengan ASCII diizinkan untuk direpresentasikan apa adanya,
# tetapi dengan karakter unicode "✨(Sparkles/Berkilau)" diloloskan ke "\xe2\x9c\xa8" . 
# Urutan yang tampak berantakan itu mewakili tiga byte, 0xe2 0x9c dan 0xa8 dalam hexa
# Artinya, karakter ✨ membutuhkan tiga byte untuk representasi binernya di bawah UTF-8.
print(" ".join(f"{i:08b}" for i in (0xe2, 0x9c, 0xa8))) # 11100010 10011100 10101000
# UTF-8 adalah format yang paling populer dari UTF.
# Keuntungan utama dari UTF-8 adalah bahwa ini lebih efisien dalam penyimpanan dan transmisi dibandingkan dengan UTF-16 dan UTF-32.

# UTF-16 adalah format yang fixed-length, yang berarti bahwa setiap karakter Unicode dinyatakan dengan 2 byte.
# Ini cocok untuk digunakan dalam situasi di mana karakter yang digunakan cenderung lebih sedikit dari karakter yang digunakan dalam ASCII.
# Keuntungan utama dari UTF-16 adalah bahwa ini lebih mudah digunakan dibandingkan dengan UTF-8 dan UTF-32.

# UTF-32 adalah format yang fixed-length, yang berarti bahwa setiap karakter Unicode dinyatakan dengan 4 byte. 
# Ini cocok untuk digunakan dalam situasi di mana karakter yang digunakan cenderung lebih sedikit dari karakter yang digunakan dalam ASCII.
# Keuntungan utama dari UTF-32 adalah bahwa ini memungkinkan karakter untuk ditampilkan dengan baik dibandingkan dengan UTF-8 dan UTF-16.


# Selain itu, bytes dalam Python dapat juga dinyatakan dalam format hexadecimal dan octal. 
# Format hexadecimal menggunakan 16 simbol (0-9 dan A-F) untuk menyatakan setiap byte, 
# sementara format octal menggunakan 8 simbol (0-7) untuk menyatakan setiap byte. 
# Anda dapat menggunakan fungsi hex() dan oct() untuk mengubah bytes ke format hexadecimal dan octal 
# dan fungsi int() dengan basis 16 atau 8 untuk mengubah kembali ke format byte.
# kunjungi folder_name: "Fungsi-Bawaan/fungsi_int.py" 

# Secara keseluruhan, Unicode, UTF-8, UTF-16, dan UTF-32 adalah berbagai jenis encoding yang digunakan untuk menyimpan dan mentransmisikan teks. 
# Masing-masing memiliki kelebihan dan kekurangan, dan digunakan dalam situasi yang berbeda. 
# Encoding dan decoding adalah proses untuk mentransformasikan teks dari satu format ke format lain, dan bytes dapat dinyatakan dalam format hexadecimal dan octal.