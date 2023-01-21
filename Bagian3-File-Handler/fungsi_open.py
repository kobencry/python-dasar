# -- Fungsi bawaan --
# fungsi open() membuka file dan mengembalikannya sebagai objek file. 
# Dengan objek file ini Anda dapat membuat, memperbarui, membaca, dan menghapus file.

# Syntax
# open(file, mode, buffering, encoding, errors, newline, closefd, opener)

# Nilai Parameter
# Parameter           kondisi              Deskripsi
# file                Dibutuhkan           Path dan nama file
# mode                Opsional             Menentukan mode yang Anda inginkan untuk membuka file
# buffering           Opsional             Menetapkan kebijakan buffering
# encoding            Opsional             Menentukan pengkodean
# errors              Opsional             Menentukan skema penanganan kesalahan yang berbeda
# newline             Opsional             Mengontrol cara kerja mode baris baru universal
# closefd             Opsional             Menjaga deskriptor file yang mendasari tetap terbuka saat file ditutup
# opener              Opsional             Pembuka khusus yang digunakan untuk operasi I/O tingkat rendah

# nilai default dari fungsi bawaan open() di python
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closfd=True, opener=None)

# file: nama file yang akan dibuka atau path file.
# mode: mode pembukaan file, yaitu 'r' untuk read, 'w' untuk write, dan 'a' untuk append.
# buffering: jumlah byte yang digunakan untuk buffer. Nilai default adalah -1, yang mengaktifkan buffering sistem. Nilai 0 menonaktifkan buffering, dan nilai 1 atau lebih mengaktifkan buffering dengan jumlah byte yang ditentukan.
# encoding: encoding yang digunakan saat membuka file teks. Nilai default adalah 'UTF-8'.
# errors: tindakan yang diambil jika terjadi error saat membuka file. Nilai default adalah 'strict'.
# newline: karakter baris baru yang digunakan. Nilai default adalah None.
# closefd : jika di set True, file descriptor tidak ditutup saat file ditutup.
# opener : fungsi yang digunakan untuk membuka file.
# Semua parameter ini digunakan untuk mengkonfigurasi cara file dibuka dan diolah.
# Namun tidak semua parameter harus digunakan dalam setiap kasus.

# Contoh 1
# membuka file dengan mode default 'r'(read/baca) atau 't'(text/teks)
f = open("mode_file.txt") # jalur file saat ini 
# membaca isi file
print(f.read())
# menutup file
f.close()

# Contoh 2
try:
    # membuka file dengan mode default 'r'(read/baca) atau 't'(text/teks)
    f = open("mode_file.txt")
    print(f.read())
finally:
    # menutup file
    f.close()
    
# Contoh 3
# membuka file dengan mode default 'r'(read/baca) atau 't'(text/teks)
with open("mode_file.txt") as f:
    # membaca isi file
    print(f.read())
# File akan ditutup secara otomatis setelah selesai mengolah