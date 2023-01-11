# Argumen newline pada method open() di Python merupakan argumen opsional 
# yang digunakan untuk menentukan cara menangani newline (baris baru) 
# saat membuka file yang berisi teks (text file). 
# Newline merupakan karakter yang digunakan untuk menandakan akhir dari suatu baris teks.

# Beberapa sistem operasi menggunakan karakter newline yang berbeda. 
# Pada Windows, newline ditandai dengan karakter CRLF (carriage return dan line feed), yaitu "\r\n".
# Sedangkan pada Linux dan MacOS, newline ditandai dengan hanya karakter LF (line feed) yaitu "\n".

# Argumen newline digunakan untuk menentukan cara menangani newline saat membaca file.
# Beberapa pilihan yang tersedia adalah:
# '' (default): mengabaikan newline dan menganggap seluruh isi file sebagai satu baris saja
# '\n': menganggap newline ditandai dengan karakter LF (line feed)
# '\r': menganggap newline ditandai dengan karakter CR (carriage return)
# '\r\n': menganggap newline ditandai dengan karakter CRLF (carriage return dan line feed)
# Contoh penggunaan argumen newline pada method open() adalah sebagai berikut:

# attribut 'newlines' menyimpan informasi tentang newline yang digunakan pada file.
# Nilainya hanya berlaku untuk file yang berisi teks (text file).

# Syntax
# file.newlines

# Nilai Parameter
# tidak ada nilai parameter

# menggunakan argumen newliine='' (default)
# membuka file dengan mode default 'r' (read/baca) atau 't' (text/teks)
with open("demo.txt", mode='r', encoding='utf-8') as fileku:
    # membaca isi file dalam bentuk list
    print("isi file:", fileku.readlines())
    print("newlines:", repr(fileku.newlines))
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# isi file: ['hello world ✨\n', 'ålice\n', 'carl 😀\n', 'eliot 😉\n', 'ini adalah file example ♞']
# jika anda menggunakan os windows
# newlines: '\r\n'
# Jika anda menggunakan os linux dan macos
# newlines: '\n'

# menggunakan argumen newline='\n'
# membuka file dengn mode default 'r' (read/baca) atau 't' (text/teks)
with open("demo.txt", mode='r', encoding='utf-8', newline='\n') as fileku:
    # membaca isi file dalam bentuk list
    print("isi file:", fileku.readlines())
    print("newlines:", repr(fileku.newlines))
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# isi file: ['hello world ✨\r\n', 'ålice\r\n', 'carl 😀\r\n', 'eliot 😉\r\n', 'ini adalah file example ♞']
# newlines: None

# menggunakan argumen newline='\r'
with open("demo.txt", mode='r', encoding='utf-8', newline='\r') as fileku:
    # membaca isi file dalam bentuk list
    print("isi file:", fileku.readlines())
    print("newlines:", repr(fileku.newlines))
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# isi file: ['hello world ✨\r', '\nålice\r', '\ncarl 😀\r', '\neliot 😉\r', '\nini adalah file example ♞']
# newlines: None