# Argumen encoding pada method open() di Python merupakan argumen opsional yang digunakan
# untuk menentukan encoding yang akan digunakan saat membuka file yang berisi teks (text file).
# Encoding merupakan suatu metode penyimpanan karakter di dalam file yang menentukan bagaimana 
# setiap karakter dari suatu teks akan disimpan dalam bentuk biner (binary).

# https://docs.python.org/3/library/codecs.html#standard-encodings

# Contoh penggunaan argumen encoding pada method open() adalah sebagai berikut:

# menggunakan encoding 'utf-8' (standar global)
with open("demo.txt", mode='r', encoding='utf-8') as fileku:
    print(fileku.read())
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# hello world ✨
# ålice
# carl 😀
# eliot 😉
# ini adalah file example ♞

# menggunakan encoding 'latin-1'
with open("demo.txt", mode='r', encoding='latin-1') as fileku:
    print(fileku.read())
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# hello world â¨
# Ã¥lice
# carl ð
# eliot ð
# ini adalah file example â

#--------------------------------------------------------------------

# attribut 'encoding' menyimpan encoding yang digunakan pada file. 
# Nilainya hanya berlaku untuk file yang berisi teks (text file).

# Syntax
# file.encoding

# Nilai Parameter
# tidak ada nilai parameter

# membuka file dengan mode default 'r' (read/baca) atau 't' (text/teks)
with open("example.txt") as fileku:
    print("jenis encoding:", fileku.encoding)
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# jenis encoding: UTF-8

# jika anda menggunakan os windows
# Output:
# jenis encoding: cp1252

# Karena default encoding adalah sistem operasi yang bergantung pada Microsoft Windows, 
# ini adalah cp1252 tetapi di Linux utf-8. Jadi ketika berhadapan dengan file teks, 
# itu adalah praktik yang baik untuk menentukan pengkodean karakter. 

# jika anda ingin Outputnya: utf-8 di windows gunakan argumen encoding="utf-8"
with open("example.txt", encoding="utf-8") as f:
    print("jenis encoding:", f.encoding)
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# jenis encoding: utf-8