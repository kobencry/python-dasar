# Argumen buffering pada method open() di Python digunakan untuk mengatur buffer ketika file dibuka.
# Buffering adalah proses menyimpan data dalam memori sementara sebelum ditulis ke dalam file atau dibaca dari file. 
# Dengan mengatur buffer, kita dapat mengontrol seberapa sering data ditulis atau dibaca dari file, 
# yang pada gilirannya dapat mempengaruhi performa program.
# Ini dapat meningkatkan kinerja operasi file dengan mengurangi jumlah panggilan sistem yang dilakukan ke sistem operasi.

# Di Python, buffering secara default dinon-aktifkan ketika kita membuka file menggunakan built-in function open().
# Jika kita tidak menentukan argumen buffering ketika memanggil open(), maka buffering tidak akan digunakan 
# dan data akan langsung ditulis atau dibaca dari file tanpa menunggu buffer penuh.
# Argumen buffering dapat diatur menjadi tiga nilai:
# 0 : tidak ada buffering, data ditulis atau dibaca langsung ke file (buffering=0 khusus untuk mode binary)
# 1 : buffering baris, data di buffer sampai karakter baris baru ditemukan
# n : buffer data dengan ukuran n byte (n=jumlah nilai).

# Contoh penggunaan argumen buffering pada method open():
import io
import time

# membuka file dengan mode 'rb'(read binary/baca binary)
# mengatur buffering = 0, maka buffering otomatis di non-aktifkan dan data 
# akan langsung ditulis atau dibaca ke/dari file tanpa menunggu buffer penuh.
with open("demo.txt", mode='rb', buffering=0) as frb:
    for i in frb:
        print(i, end='')
        time.sleep(1)
# File akan ditutup secara otomatis setelah selesai mengolah

with open("demo.txt", mode='r', buffering=1) as fr:
    for i in fr:
        print(i, end='')
        time.sleep(1)
# File akan ditutup secara otomatis setelah selesai mengolah
# Pada contoh kode yang saya berikan sebelumnya, buffer akan diisi sebesar 1 baris sebelum dibaca dari file.
# Ini berarti bahwa setiap kali program membaca 1 baris dari file, itu akan ditampung dalam buffer sebelum dikembalikan sebagai output. Hal ini dapat membantu meningkatkan performa program karena program tidak perlu membaca data dari file satu baris per satu. Namun, jika buffer harus diisi dan dikosongkan secara terus-menerus, ini dapat membuat program menjadi lebih lambat.

# menggunakan ukuran buffer default (8192) di python
ukuran_buffer = io.DEFAULT_BUFFER_SIZE # 8192
with open("demo.txt", mode='r', buffering=ukuran_buffer) as fr:
    for i in fr:
        print(i, end='')
        time.sleep(1)
# File akan ditutup secara otomatis setelah selesai mengolah

# Pada contoh kode yang saya berikan sebelumnya, buffer akan diisi sebesar 8192 byte sebelum ditulis ke dalam file. 
# Hal ini dapat membantu meningkatkan performa program karena data akan ditulis ke file
# dalam blok besar (8192 byte) daripada ditulis satu per satu.
# Namun, ingat bahwa buffering juga dapat membuat program menjadi lebih lambat jika buffer terus-menerus harus diisi dan dikosongkan.
        
# Jika buffering diaktifkan, Anda akan mendapatkan output sekaligus di layar setelah menunggu selama 13 detik.

# Perlu diingat bahwa buffering tidak selalu bermanfaat, tergantung pada konteks dan jenis aplikasi yang digunakan.
# Beberapa aplikasi memerlukan buffering yang tepat untuk memastikan performa yang baik, 
# sementara yang lain mungkin lebih baik tanpa buffering.