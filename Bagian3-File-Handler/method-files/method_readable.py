# Method readable() mengembalikan nilai boolean True jika file tersebut bisa dibaca, 
# jika file tersebut tidak bisa dibaca mengembalikan nilai boolean False.

# Syntax
# file.readable()

# Nilai Parameter
# tidak ada nilai parameter

# membuka file dengan mode default 'r' (read/baca) atau 't' (text/teks)
with open('file.txt') as fileku:
    print(fileku.readable())
    # Output:
    # True
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

'''
Beberapa jenis file yang mungkin tidak bisa dibaca oleh program Python di atas adalah:

1. File yang tidak ada: 
* Jika kita mencoba membuka file yang tidak ada, maka akan terjadi error "FileNotFoundError".

2. File yang tidak memiliki izin baca: 
* Jika file tersebut tidak memiliki izin baca, maka akan terjadi error "PermissionError".

3. File yang dalam format yang tidak dapat dibaca oleh program: 
* Misalnya, jika kita mencoba membaca file dengan format gambar (seperti JPEG atau PNG) 
* dengan menggunakan method read(), maka akan terjadi error "UnicodeDecodeError".

4. File yang terproteksi password: 
* Jika file tersebut terproteksi dengan password, 
* maka kita perlu memasukkan password terlebih dahulu sebelum dapat membacanya.

Perlu diingat bahwa tergantung pada konteks dan cara menggunakannya, 
ada kemungkinan bahwa beberapa jenis file di atas mungkin bisa dibaca
oleh program Python dengan menggunakan cara yang berbeda. 
Sebagai contoh, untuk membaca file gambar, kita dapat menggunakan library image processing seperti Pillow.
'''
