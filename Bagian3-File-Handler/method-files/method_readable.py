# Method readable() mengembalikan nilai boolean True jika file tersebut bisa dibaca, 
# jika file tersebut tidak bisa dibaca mengembalikan nilai boolean False.

# Syntax
# file.readable()

# Nilai Parameter
# tidak ada nilai parameter

# membuka file dengan mode default 'r' (read/baca) atau 't' (text/teks)
with open('file.txt') as fileku:
    print("periksa apakah file dapat dibaca:", fileku.readable())
    # Output:
    # periksa apakah file dapat dibaca: True
# File akan ditutup secara otomatis setelah selesai mengolah

# membaca file gambar
with open('file_logo_python.png', 'rb') as fileku:
    # periksa apakah file tersebut bisa dibaca.
    if fileku.readable():
        # baca isi file dalam 20 karakter
        print(fileku.read(20))
    # jika kondisi diatas tidak terpenuhi jalankan kode ini
    else:
        print("file tidak bisa dibaca")
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\xc8'

# membuka file dengan mode 'w' (write/tulis)
with open('file.txt', 'w') as fileku:
    print("periksa apakah file dapat dibaca:", fileku.readable())
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# periksa apakah file dapat dibaca: False

# Jadi, method readable() bahwa file hanya dapat dibaca saat dibuka dalam mode “r” 
# untuk semua mode lainnya, itu tidak dapat dibaca.
