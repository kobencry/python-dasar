# Method truncate() digunakan untuk memotong (truncate) file yang terbuka saat ini. 
# Jika argument "size" tidak diberikan, maka file akan di-truncate/potong 
# hingga ukurannya sama dengan posisi file pointer saat ini.

# Syntax
# file.truncate(size)

# Nilai Parameter
# Parameter                 Deskripsi
# size                      Opsional. Ukuran file (dalam byte) setelah pemotongan. Default None, yang berarti posisi aliran file saat ini

# (!) Peringatan:
# program ini akan error jika menggunakan jalur file saya
# ubah dulu jalur file tersebut

# menggunakan library python
import os

dataku = ('hello world', 'alice', 'carl', 'eliot')

# membuka file dengan mode 'w' (write/tulis) 
with open('file_demo_truncate.txt', 'w') as fileku:
    # mengetahui posisi pointer saat ini
    print("posisi pointer saat ini:", fileku.tell())
    
    # menulis data ke file
    for i in dataku:
        fileku.write(i + '\n')
    # menulis data ke file
    fileku.write('ini adalah file demo truncate')
    
    # menggunakan attribut name dari file objek python
    print("masukan data ke file:", fileku.name)
    
    # mengetahui posisi pointer saat ini
    print("posisi pointer saat ini:", fileku.tell())


    # gunakan jalur file kalian sendiri dimana "file_demo_truncate.txt" ditempatkan 
    # tips untuk menemukan jalur file saat ini jalankan program dibawah ini
    # print(os.getcwd()) 
    # atau anda bisa menggunakan terminal/cmd ketik: python
    # >>> import os
    # >>> os.getcwd() 
    # akan menampilkan jalur file target
    # periksa ukuran file menggunakan modul bawaan python os.path.getsize("jalur_file_target")
    hasil = os.path.getsize(r"C:\Users\USER\OneDrive\Desktop\python-dasar\Bagian3-File-Handler\method-files\file_demo_truncate.txt")
    print("sebelum ukuran file dipotong:", hasil)
    
    # memotong ukuran file menjadi 43 bytes atau karakter dari file
    print("memotong ukuran file dengan jumlah:", fileku.truncate(43))
# File akan ditutup secara otomatis setelah selesai mengolah

# Output:
# posisi pointer saat ini: 0
# masukan data ke file: file_demo_truncate.txt
# posisi pointer saat ini: 62
# sebelum ukuran file dipotong: 62
# memotong ukuran file dengan jumlah: 43

# membuka file dengan mode default
with open('file_demo_truncate.txt') as fileku:
    # membaca seluruh isi file
    print(fileku.read())

    # gunakan jalur file kalian sendiri dimana "file_demo_truncate.txt" ditempatkan
    # periksa ukuran file dengan os.path.getsize("jalur_file_target")
    hasil = os.path.getsize(r"C:\Users\USER\OneDrive\Desktop\python-dasar\Bagian3-File-Handler\method-files\file_demo_truncate.txt")
    print("setelah ukuran file dipotong:", hasil)
# File akan ditutup secara otomatis setelah selesai mengolah

# Output:
# hello world
# alice
# carl
# eliot
# ini adalah
# setelah ukuran file dipotong: 43

# Perlu diingat bahwa method truncate() hanya dapat digunakan 
# pada file yang terbuka dengan mode "write" atau "write+". 
# Jika file tersebut dibuka dengan mode "read", maka method truncate() akan menyebabkan error.

# Jika anda ingin mengetahui lebih lanjut tentang library os pada python kunjungi folder_name: "modul-os"
