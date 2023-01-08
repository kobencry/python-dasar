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
