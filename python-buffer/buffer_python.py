# Apa itu buffer
# Buffer adalah area penyimpanan sementara yang digunakan untuk menyimpan data sementara 
# sebelum diteruskan ke proses selanjutnya atau disimpan dalam media penyimpanan permanen.
# Buffer dapat digunakan dalam berbagai situasi, seperti dalam sistem operasi, pemrograman, jaringan, dan lainnya.

# Dalam pemrograman, buffer dapat digunakan untuk meningkatkan efisiensi program dengan menyimpan 
# data sementara sebelum diteruskan ke proses selanjutnya atau ditampilkan sebagai output. 
# Hal ini dapat membantu dalam menangani data yang besar atau dalam jumlah besar karena data
# dapat diolah secara bertahap dari buffer tanpa harus menunggu untuk seluruh proses untuk selesai.

# Dalam sistem operasi, buffer dapat digunakan untuk meningkatkan efisiensi disk dengan menyimpan data 
# sementara dari disk sebelum diteruskan ke proses selanjutnya atau disimpan dalam media penyimpanan permanen.
# Ini dapat membantu dalam mengurangi waktu yang dihabiskan untuk menulis atau membaca data dari disk.

# Dalam jaringan, buffer dapat digunakan untuk mengumpulkan paket data yang diterima
# sebelum diteruskan ke proses selanjutnya atau disimpan dalam media penyimpanan permanen. 
# Ini dapat membantu dalam menangani jumlah data yang besar atau dalam jumlah besar yang diterima dari jaringan.


# Dalam tutorial ini adalah untuk input/output standar dengan Python.
# Tapi ide dasar dari buffer itu sama. 
# Anda dapat menganggap buffer adalah lapisan tengah antara apa yang telah dilakukan program dan
# apa yang telah ditunjukkan oleh program kepada kita, dan kebijakan buffer memutuskan apa yang dapat kita lihat.
# Gambaran output buffer python:

#  .------------------.
#  | program executed |
#  '------------------'  
#           |
#           V
#  .------------------.
#  |      Buffer      |
#  '------------------'
#           | buffer policy/kebijakan buffer
#           V
#  .------------------.
#  |  program output  |
#  '------------------'

# Setelah program dijalankan, hasil dari program akan disimpan dalam buffer sebelum diteruskan ke output.

# Kapan dan Mengapa kita ingin menutup buffer
# Pada artikel di atas, kita berbicara tentang keuntungan dari buffer.
# Itu dapat mengurangi jumlah penulisan hard disk. 
# Namun ketika skenario datang ke program interaksi, kerugiannya juga muncul.
# Kita tidak bisa melihat hasilnya secara real time.

# import os
# import sys
# import time
import os, sys, time # kode ini setara dengan diatas

# Jika Anda menjalankan skrip Python di bawah ini, Anda akan menemukan semua angka ditampilkan bersamaan.
# Ini karena kebijakan buffer.
# secara default buffer aktif di python
print("-- buffer aktif --")
for i in range(10): # dimulai dari 0 sampai 9
    # mencetak angka dari 0 sampai 9 tanpa baris baru (menggunakan end='')
    print(i, end='')
    # program akan dihentikan selama 1 detik pada setiap iterasi (menggunakan time.sleep(1)).
    time.sleep(1)
# Jika buffering diaktifkan, Anda akan mendapatkan output sekaligus di layar setelah menunggu selama 10 detik.
# Output: "menunggu selama 10 detik"
# 0123456789

print() # kode ini setara dengan baris baru '\n(newline)'

# Jika kita menutup buffer dengan argumen 'flush=True', kita bisa melihat angka yang muncul setiap 1 detik. 
# Sehingga kita bisa melihat hasilnya secara real time.
print("-- buffer dinonaktifkan --")
for i in range(10): # dimulai dari 0 sampai 9
    # mencetak angka dari 0 sampai 9 tanpa baris baru (menggunakan end='')
    print(i, end='', flush=True)
    time.sleep(1)
# Jika buffering dinonaktifkan, angka akan ditampilkan satu per satu setiap 1 detik.
# Output:
# 0123456789


# Bagaimana cara mengatur unbuffer?

# Metode 1: Baris perintah
# Anda dapat menjalankan skrip python dengan opsi python -u nama_file
# -u : stdout dan stderr biner tanpa buffer, stdin selalu di-buffer; juga PYTHONUNBUFFERED=x

# Metode 2: flush
# Jika Anda hanya menggunakan print dan tidak memodifikasi terlalu banyak bagian,
# Anda dapat menambahkan flush di setiap pernyataan print.
# print(data, flush=True)

# Metode 3: ubah pengaturan default dalam kode
# Kami menetapkan buffering sebagai 1, ini adalah buffering baris. 
# Ini buffer setiap kali ketemu baris baru '\n(newline)'. Tersedia dalam mode file teks.
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', buffering=1)
sys.stderr = os.fdopen(sys.stderr.fileno(), 'w', buffering=1)
sys.stdin = os.fdopen(sys.stdin.fileno(), 'r', buffering=1)

print("\nmasukan apapun:")
baris = sys.stdin.readline()
for i in baris:
    print(i)
    time.sleep(1)

# Jika kita mengatur buffering=0, itu berarti unbuffered(tidak ada buffer).
# Tapi itu hanya tersedia dalam mode file biner (w->wb).
# Kita dapat menggunakan buffer baris untuk mencapai efek yang mungkin terjadi sebagai kebijakan unbuffering.