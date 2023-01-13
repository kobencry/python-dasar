# Argumen buffering pada method open() di Python digunakan untuk mengontrol perilaku buffering dari file ketika dibuka. 
# Buffering adalah proses menyimpan data dalam sebuah buffer sementara sebelum ditulis ke file atau dikirim ke perangkat keluaran. 
# Ini dapat meningkatkan kinerja operasi file dengan mengurangi jumlah panggilan sistem yang dilakukan ke sistem operasi.

# Argumen buffering dapat diatur menjadi tiga nilai:

# 0 : tidak ada buffering, data ditulis ke file segera
# 1 : buffering baris, data di buffer sampai karakter baris baru ditemukan
# n : buffer data dengan ukuran n byte (n=jumlah nilai).
# Contoh penggunaan argumen buffering pada method open():

import time

# membuka file dengan mode default 'r'(read/baca) atau 't'(text/teks)
with open("buffer.txt", buffering=1) as fr:
    print(fr.line_buffering)
    for i in fr.buffer:
        time.sleep(1)
        print(i, end='', flush=True)

