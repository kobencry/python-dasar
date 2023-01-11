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

# Contoh 1
# membuka file dengan mode default 'r'(read/baca) atau 't'(text/teks)
f = open("mode_file.txt") # jalur file saat ini 
# membaca isi file
print(f.read())
# menutup file
f.close()

# Contoh 2
# membuka file dengan mode default 'r'(read/baca) atau 't'(text/teks)
with open("mode_file.txt") as f:
    # membaca isi file
    print(f.read())
# File akan ditutup secara otomatis setelah selesai mengolah