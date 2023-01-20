# Argumen buffering pada method open() di Python digunakan untuk mengatur buffer ketika file dibuka.
# Buffering adalah proses menyimpan data dalam memori sementara sebelum ditulis ke dalam file atau dibaca dari file. 
# Dengan mengatur buffer, kita dapat mengontrol seberapa sering data ditulis atau dibaca dari file, 
# yang pada gilirannya dapat mempengaruhi performa program.
# Ini dapat meningkatkan kinerja operasi file dengan mengurangi jumlah panggilan sistem yang dilakukan ke sistem operasi.

# Argumen buffering dapat diatur menjadi tiga nilai:
# 0 (atau None) : buffering tidak digunakan(dinon-aktifkan) dan data dibaca atau ditulis dari file satu per satu. 
# Ini dapat digunakan jika Anda ingin membaca atau menulis data dari file secara real-time dan tidak ingin menunggu buffer penuh.
# (hanya dapat digunakan dalam mode binary/biner)

# 1 : buffering digunakan dan setiap kali program membaca atau menulis satu baris dari file, 
# itu akan ditampung dalam buffer sebelum ditulis atau dikembalikan sebagai output. 
# Ini dapat digunakan jika Anda ingin membaca atau menulis data dari file per baris dan tidak ingin menunggu buffer penuh.
# (hanya dapat digunakan dalam mode teks)

# 8192 (atau jumlah byte lainnya) : buffering digunakan dan setiap kali program membaca atau menulis jumlah byte tertentu dari file,
# itu akan ditampung dalam buffer sebelum ditulis atau dikembalikan sebagai output. 
# Ini dapat digunakan jika Anda ingin membaca atau menulis data dari file dalam jumlah besar dan tidak ingin menunggu buffer penuh.
# (untuk digunakan dalam mode binary atau teks)

# Gambaran buffering output python
#       ------------------
#      |      Memory      |
#       ------------------  
#               |
#               V
#       ------------------
#      |      Buffer      |
#       ------------------  
#               |
#               V
#       ------------------
#      |    Hard disk     |
#       ------------------  

# Contoh penggunaan argumen buffering pada method open():

# menggunakan buffering=0 (None) 
# 0 : tidak ada buffering, data ditulis atau dibaca langsung ke file (buffering=0 khusus untuk mode binary)
# membuka file dengan mode 'rb'(read binary/baca biner) dan 'ab'(append binary/tambah biner)
with open("demo_unbuffer.txt", mode='rb') as frb, open("demo_unbuffer.txt", mode='ab', buffering=0) as fab:
    # data akan ditulis ke hard disk tidak peduli ukurannya
    # menulis string ke file dalam bentuk biner/objek bytes
    fab.write("hello".encode())

    # untuk membaca isi file yang sudah dibaca atau ditulis
    # kita harus pindahkan posisi pointer file ke awal
    # posisi pointer(cursor) saat ini berada di akhir file
    # mengatur posisi pointer(cursor) saat ini ke awal file
    frb.seek(0)

    # membaca isi file dalam bentuk biner/objek bytes
    # print(frb.read())
    # membaca isi file dalam bentuk string
    print(frb.read().decode())  # menggunakan method-string .encode()
    # Output:
    # hello

    # data akan ditulis ke hard disk tidak peduli ukurannya
    # menulis string ke file dalam bentuk biner/objek bytes
    fab.write(b" world")    # menggunakan b""

    # untuk membaca isi file yang sudah dibaca atau ditulis
    # kita harus pindahkan posisi pointer file ke awal
    # posisi pointer(cursor) saat ini berada di akhir file
    # mengatur posisi pointer(cursor) saat ini ke awal file 
    frb.seek(0)

    # membaca isi file dalam bentuk biner/objek bytes
    # print(frb.read())
    # membaca isi file dalam bentuk string
    print(frb.read().decode())
    # Output:
    # hello world
# File akan ditutup secara otomatis setelah selesai mengolah.
#--------------------------------------------------------------------------------------------------
# [!] jika anda masih kurang paham dengan contoh diatas hapus seluruh isi file "demo_unbuffer.txt"
# dan jalankan kode program berulang-ulang sampai anda memahaminya
#--------------------------------------------------------------------------------------------------

# menggunakan buffering=1
# 1 : buffering baris, data di buffer sampai karakter baris baru ditemukan (hanya dapat digunakan dalam mode teks)
# membuka file dengan mode 'r'(read/baca) dan 'a'(append/tambah)
with open("buffer_line.txt", mode='r') as fr, open("buffer_line.txt", mode='a', buffering=1) as fa:
    # menggunakan karakter \n(newline) "baris baru"
    # berarti kita menyelesaikan satu baris, jadi baris ini ditulis ke hard disk
    fa.write("hello world\n") 
    print(fr.read())
    # Output:
    # hello world

    # untuk membaca isi file yang sudah dibaca atau ditulis
    # kita harus pindahkan posisi pointer(cursor) file ke awal
    # posisi pointer(cursor) saat ini berada di akhir file
    # mengatur posisi pointer(cursor) saat ini ke awal file
    fr.seek(0)

    # tidak menggunakan karakter \n(newline) "baris baru"
    # sehingga data tidak akan ditulis ke hard disk
    fa.write("alice carl eliot") 
    print(fr.read())
    # Output:
    # hello world

    # untuk membaca isi file yang sudah dibaca atau ditulis
    # kita harus pindahkan posisi pointer(cursor) file ke awal
    # posisi pointer(cursor) saat ini berada di akhir file
    # mengatur posisi pointer(cursor) saat ini ke awal file
    fr.seek(0)

    # buffer menemukan karakter baris baru "\n(newline)"
    # menulis data alice carl eliot ke hard disk
    fa.write("\n") # menggunakan karakter \n(newline) "baris baru"
    print(fr.read())
    # Output:
    # hello world
    # alice carl eliot
# File akan ditutup secara otomatis setelah selesai mengolah.
# Jika Anda menggunakan buffering=1 dalam mode binary, 
# maka program akan membaca atau menulis satu byte data biner dari file sekaligus dan menyimpannya dalam buffer.
# Setelah buffer penuh, data akan ditulis atau dikembalikan sebagai output. 
# Namun, ini tidak digunakan dalam mode binary karena dalam mode binary, 
# data yang dibaca atau ditulis biasanya dalam jumlah yang besar, 
# sehingga buffering=1 tidak akan efektif dalam meningkatkan performa program. 
# Jadi, buffering=1 digunakan dalam mode teks yang membaca atau menulis data per baris.
#------------------------------------------------------------------------------------------------
# [!] jika anda masih kurang paham dengan contoh diatas hapus seluruh isi file "buffer_line.txt"
# dan jalankan kode program berulang-ulang sampai anda memahaminya
#------------------------------------------------------------------------------------------------

# menggunakan buffering > 1(lebih besar dari 1)

# Jika anda menggunakan nilai buffering=2
# membuka file dengan mode 'r'(read/baca)
with open("buffer_size2.txt", mode='r') as fr:
    # membuka file dengan mode 'ab'(append binary/tambah biner)
    with open(f"{fr.name}", mode='ab', buffering=2) as fab:

        # print(len(b"hello world\n")) # 12 bytes
        # menulis 12 byte data
        fab.write(b"hello world\n")

        # untuk membaca isi file yang sudah dibaca atau ditulis
        # kita harus pindahkan posisi pointer(cursor) file ke awal
        # posisi pointer(cursor) saat ini berada di akhir file
        # mengatur posisi pointer(cursor) saat ini ke awal file 
        fr.seek(0)

        # buffer penuh, menulis data ke hard disk
        print(fr.read())
        # Output:
        # hello world
# File akan ditutup secara otomatis setelah selesai mengolah.
#------------------------------------------------------------------------------------------------
# [!] jika anda masih kurang paham dengan contoh diatas hapus seluruh isi file "buffer_size2.txt"
# dan jalankan kode program berulang-ulang sampai anda memahaminya
#------------------------------------------------------------------------------------------------

# jika anda menggunakan nilai buffering=13
with open("buffer_size13.txt", mode='r') as fr:
    # membuka file dengan mode 'ab'(append binary/tambah biner)
    with open(f"{fr.name}", mode='ab', buffering=13) as fab:

        # print(len(b"hello world\n")) # 12 bytes
        # menulis 12 byte data
        fab.write(b"hello world\n")

        # untuk membaca isi file yang sudah dibaca atau ditulis
        # kita harus pindahkan posisi pointer file ke awal
        # posisi pointer(cursor) saat ini berada di akhir file
        # mengatur posisi pointer(cursor) saat ini ke awal file 
        fr.seek(0)

        # buffer tidak penuh, data akan ditampung dibuffer.
        # data tidak ditampilkan di Output menunggu buffer penuh
        print(fr.read())
        # Output tidak ada:
# File akan ditutup secara otomatis setelah selesai mengolah.
#------------------------------------------------------------------------------------------------
# [!] jika anda masih kurang paham dengan contoh diatas hapus seluruh isi file "buffer_size13.txt"
# dan jalankan kode program berulang-ulang sampai anda memahaminya
#------------------------------------------------------------------------------------------------

import io
# jika anda menggunakan buffering=8192 nilai default yang digunakan oleh Python dari method open()

# nilai default buffering pada python
ukuran_buffer = io.DEFAULT_BUFFER_SIZE
print("Default ukuran buffer:", ukuran_buffer)

# membuka file dengan mode 'r'(read/baca)
with open("buffer_default.txt", mode='r') as fr:
    # membuka file dengan mode 'ab'(append binary/tambah biner)
    with open(f"{fr.name}", mode='ab', buffering=ukuran_buffer) as fab:
        #print(len(b"hello world\n")) # 12
        # menulis 12 bytes data
        fab.write(b"hello world\n")
        # menulis lebih banyak data bytes
        fab.write(b"hello world\n")
        fab.write(b"hello world\n")
        # fab.write...dst(dan seterusnya) sampai buffer penuh

        # untuk membaca isi file yang sudah dibaca atau ditulis
        # kita harus pindahkan posisi pointer(cursor) file ke awal
        # posisi pointer(cursor) saat ini berada di akhir file
        # mengatur posisi pointer(cursor) saat ini ke awal file 
        fr.seek(0)

        # jika data bytes kurang dari buffering=8192, buffer tidak penuh, data akan ditampung dibuffer.
        # data tidak ditampilkan di Output menunggu buffer penuh
        print(fr.read())
        # Output tidak ada:
# File akan ditutup secara otomatis setelah selesai mengolah.
#------------------------------------------------------------------------------------------------
# [!] jika anda masih kurang paham dengan contoh diatas hapus seluruh isi file "buffer_default.txt"
# dan jalankan kode program berulang-ulang sampai anda memahaminya
#------------------------------------------------------------------------------------------------


# Attribut buffer pada objek file Python adalah properti yang menyimpan 
# informasi tentang buffer yang digunakan oleh objek file. 
# Attribut buffer dapat digunakan untuk mendapatkan atau mengubah
# buffer yang digunakan oleh objek file, seperti posisi pointer(cursor) saat ini dalam buffer,
# data yang disimpan dalam buffer.
# Anda dapat mengakses buffer pada objek file dengan menggunakan buffer atribut, misalnya :
with open("demo.txt", mode='r', encoding='utf-8') as fr:
    obj_buffer = fr.buffer
    # menampilkan data dalam format bytes
    # print(obj_buffer.read())

    # menampilkan data dalam format string
    print(obj_buffer.read().decode())
# File akan ditutup secara otomatis setelah selesai mengolah.


# Jadi, dalam menentukan nilai buffering yang digunakan dalam program, 
# Anda harus mempertimbangkan konteks dan kebutuhan aplikasi Anda. 
# Jika Anda membutuhkan akses data real-time, Anda dapat menggunakan buffering 0 atau None.
# Namun, jika Anda ingin meningkatkan performa program dengan menyimpan data dalam buffer, 
# Anda dapat menggunakan buffering 1 atau 8192 atau jumlah byte lainnya yang sesuai dengan kebutuhan aplikasi Anda.

# Buffering bisa juga dapat membuat program menjadi lebih lambat jika buffer terus-menerus harus diisi 
# dan dikosongkan, tidak ditentukan oleh nilai tertentu.
# Hal ini tergantung pada konteks dan jenis aplikasi yang digunakan.
# Beberapa aplikasi memerlukan buffering yang tepat untuk memastikan performa yang baik, 
# sementara yang lain mungkin lebih baik tanpa buffering.

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