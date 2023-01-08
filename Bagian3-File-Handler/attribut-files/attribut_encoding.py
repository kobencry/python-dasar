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
