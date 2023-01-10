# Method seek() adalah method yang terdapat pada objek file di Python yang 
# digunakan untuk mengatur posisi file pointer(cursor) pada file yang terbuka saat ini.
# Method ini memiliki dua argument yaitu "offset" dan "whence".

# Syntax
# file.seek(offset, whence)

# Argument "offset" menentukan jumlah byte yang akan ditambahkan atau dikurangi
# dari posisi file pointer(cursor) saat ini. 
# Jika "offset" bernilai positif, maka file pointer(cursor) akan berpindah ke depan sebanyak "offset" byte. 
# Sebaliknya, jika "offset" bernilai negatif, maka file pointer(cursor) akan berpindah ke belakang sebanyak "offset" byte.

# Argument "whence" menentukan dari mana offset akan ditambahkan atau dikurangi.
# Nilai "whence" dapat bernilai:
# 0 (mengacu pada awal file)
# 1 (mengacu pada posisi file pointer(cursor) saat ini) atau 
# 2 (mengacu pada akhir file).

# Berikut ini adalah contoh penggunaan method seek() di Python:

# membuka file dengan mode default 'r' (read/baca) atau 't' (text/teks)
with open('file_demo_seek.txt') as fileku:
    # baca seluruh isi file
    print(fileku.read())
    # Output:
    # hello world
    # alice
    # carl
    # eliot
    # ini adalah file demo seek

    # baca lagi seluruh isi file
    print(fileku.read())
    # Outputnya string kosong

    # menggunakan method repr()
    # baca lagi seluruh isi file
    print(repr(fileku.read()))
    # Outputnya: ''
    # ternyata posisi pointer(cursor) berada diakhir baris

    # mengatur posisi pointer(cursor) ke awal
    fileku.seek(0)
    # baca sebanyak 11 byte dari file
    print(fileku.read(11))
    # Output:
    # hello world
# File akan ditutup secara otomatis setelah selesai mengolah

# membaca isi file dimulai dari karakter ke 6
# membuka file dengan mode default 'r' (read/baca) atau 't' (text/teks)
with open('file_demo_seek.txt') as fileku:
    # mengatur posisi pointer
    posisi = fileku.seek(6)
    print("posisi pointer saat ini:", posisi)
    # baca isi file
    s = fileku.read(posisi)
    print("posisi karakter saat ini:", s[posisi - posisi])
    # Output:
    # posisi pointer saat ini: 6
    # posisi karakter saat ini: w

    # baca seluruh baris dari file
    print(fileku.read())
    # Output:
    # alice
    # carl
    # eliot
    # ini adalah file demo seek
# File akan ditutup secara otomatis setelah selesai mengolah

# menggunakan argumen "whence"
# 0 (mengacu pada awal file),
# 1 (mengacu pada posisi file pointer(cursor) saat ini), atau 
# 2 (mengacu pada akhir file).
with open('file_demo_seek.txt') as fileku:
    s = fileku.read(23)
    print(s)
    # Output:
    # hello
    # alice
    # carl

    # mengatur posisi pointer ke awal "hello world"
    # argumen "offset" 1 dengan posisi karakter berada di "e"
    # argumen "whence" 0 dengan posisi diawal file 
    posisi = fileku.seek(1, 0)
    print("posisi pointer saat ini:", posisi)
    print("posisi karakter saat ini:", s[posisi])
    print(fileku.read(16))
    # Output:
    # osisi pointer saat ini: 1
    # posisi karakter saat ini: e
    # ello world
    # alice

# whence yang bernilai 1 dan 2 hanya untuk menangani file biner (bytes)
# membuka file dengan mode 'rb' (read/baca, binnary/biner)
with open("file_demo_seek.bin", mode='rb') as fb:
    # membaca isi file biner
    # print(fb.read())
    # Output:
    # b'ABCDEFGHIJKLMNOPQRSTUVWXYZ\r\n'
    # jika ingin Outputnya dalam format string
    print(fb.read().decode())
    # Output:
    # ABCDEFGHIJKLMNOPQRSTUVWXYZ

    # untuk membaca isi file yang sudah dibaca atau ditulis
    # kita harus pindahkan posisi pointer file ke awal
    # posisi pointer(cursor) saat ini berada di akhir file
    # mengatur posisi pointer(cursor) saat ini ke awal file
    # fb.seek(0)

    # mengatur posisi pointer(cursor) saat ini ke baris 3
    fb.seek(3)
    print(fb.read(1).decode())
    # Output:
    # D

    # 'whence' bernilai 1 (mengacu pada posisi file pointer(cursor) saat ini) 
    fb.seek(3, 1)
    print(fb.read(1).decode())
    # Output:
    # H

    # 'whence' bernilai 2 (mengacu pada akhir file)
    fb.seek(-5, 2)
    # print(fb.read().decode())
    # Output:
    # b'XYZ\r\n'
    print(fb.read().decode())
    # Output:
    # XYZ

# File akan ditutup secara ototatis setelah selesai mengolah


# Catatan:
# Perlu diingat bahwa penggunaan method seek() hanya dapat dilakukan pada file yang terbuka 
# dengan mode "read", "write+" atau yang mengandung mode "read".
# Jika file tersebut dibuka dengan mode "write", maka method seek() akan menyebabkan error
