# Argumen encoding pada method open() di Python merupakan argumen opsional yang digunakan
# untuk menentukan encoding yang akan digunakan saat membuka file yang berisi teks (text file).
# Encoding merupakan suatu metode penyimpanan karakter di dalam file yang menentukan bagaimana 
# setiap karakter dari suatu teks akan disimpan dalam bentuk biner (binary).

# https://docs.python.org/3/library/codecs.html#standard-encodings

# Contoh penggunaan argumen encoding pada method open() adalah sebagai berikut:

# menggunakan encoding 'utf-8' (standar global)
with open("example.txt", mode='r', encoding='utf-8') as fileku:
    print(fileku.read())
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# hello world ✨
# ålice
# carl 😀
# eliot 😉
# ini adalah file example ♞

# menggunakan encoding 'latin-1' (os windows)
with open("example.txt", mode='r', encoding='latin-1') as fileku:
    print(fileku.read())
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# hello world â¨
# Ã¥lice
# carl ð
# eliot ð
# ini adalah file example â
