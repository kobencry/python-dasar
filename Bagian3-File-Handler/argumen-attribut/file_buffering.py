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
# mengatur buffering=0, maka buffering otomatis di non-aktifkan dan data 
# akan langsung ditulis atau dibaca ke/dari file tanpa menunggu buffer penuh.
with open("demo.txt", mode='rb', buffering=0) as frb:
    for i in frb:
        print(i, end='')
        time.sleep(1)
# File akan ditutup secara otomatis setelah selesai mengolah

# membuka file dengan mode 'r'(read/baca)
# mengatur buffering=1, maka buffering otomatis diaktifkan dan data
# akan mengeluarkan satu per satu setiap kali program membaca atau menulis 1 baris dari file
# itu akan ditampung dalam buffer sebelum dikembalikan sebagai output. 
# (intinya jika ketemu karakter baris baru '\n'(newline))
with open("demo.txt", mode='r', buffering=1) as fr:
    for i in fr:
        print(i, end='')
        time.sleep(1)
# File akan ditutup secara otomatis setelah selesai mengolah

# membuka file dengan mode 'r'(read/baca)
# mengatur buffering=8192, maka buffering otomatis diaktifkan dan data
# akan mengeluarkan satu per satu setiap kali program membaca atau menulis 8192 byte dari file
# itu akan ditampung dalam buffer sebelum dikembalikan sebagai output. 
# (intinya jika ketemu karakter baris baru '\n'(newline))
ukuran_buffer = io.DEFAULT_BUFFER_SIZE # 8192
with open("demo.txt", mode='r', buffering=ukuran_buffer) as fr:
    for i in fr:
        print(i, end='')
        time.sleep(1)
# File akan ditutup secara otomatis setelah selesai mengolah

# Buffering yang dapat membuat program menjadi lebih lambat jika buffer terus-menerus harus diisi 
# dan dikosongkan, tidak ditentukan oleh nilai tertentu.
# Hal ini tergantung pada konteks dan jenis aplikasi yang digunakan. Beberapa aplikasi memerlukan
# buffering yang tepat untuk memastikan performa yang baik, sementara yang lain mungkin lebih baik tanpa buffering.
# Buffering yang terlalu kecil dapat menyebabkan I/O disk yang berlebihan dan menurunkan performa, 
# sementara buffering yang terlalu besar dapat menyebabkan memori yang berlebihan dan juga menurunkan performa. 
# Oleh karena itu, penting untuk menentukan buffering yang sesuai dengan aplikasi dan konteks yang digunakan.

# Jika Anda tidak yakin tentang buffering yang sesuai, Anda dapat mencoba beberapa nilai yang berbeda
# dan mengukur performa program untuk menemukan nilai yang paling sesuai. 
# Namun, jika anda tidak ingin repot, python secara default tidak menggunakan buffering, 
# jadi anda bisa menggunakannya tanpa harus mengatur buffering.

# Perlu diingat bahwa buffering tidak selalu bermanfaat, tergantung pada konteks dan jenis aplikasi yang digunakan.
# Beberapa aplikasi memerlukan buffering yang tepat untuk memastikan performa yang baik, 
# sementara yang lain mungkin lebih baik tanpa buffering.