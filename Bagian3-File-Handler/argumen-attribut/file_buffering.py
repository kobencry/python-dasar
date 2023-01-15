# Argumen buffering pada method open() di Python digunakan untuk mengatur buffer ketika file dibuka.
# Buffering adalah proses menyimpan data dalam memori sementara sebelum ditulis ke dalam file atau dibaca dari file. 
# Dengan mengatur buffer, kita dapat mengontrol seberapa sering data ditulis atau dibaca dari file, 
# yang pada gilirannya dapat mempengaruhi performa program.
# Ini dapat meningkatkan kinerja operasi file dengan mengurangi jumlah panggilan sistem yang dilakukan ke sistem operasi.

# Di Python, buffering secara default dinon-aktifkan ketika kita membuka file menggunakan built-in function open().
# Jika kita tidak menentukan argumen buffering ketika memanggil open(), maka buffering tidak akan digunakan 
# dan data akan langsung ditulis atau dibaca dari file tanpa menunggu buffer penuh.

# Argumen buffering dapat diatur menjadi tiga nilai:
# 0 (atau None) : buffering tidak digunakan dan data dibaca atau ditulis dari file satu per satu. 
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

# Contoh penggunaan argumen buffering pada method open():

# menggunakan buffering=0 (None)
# membuka file dengan mode 'rb' (read binary/baca biner)
with open("demo.txt", mode='rb', buffering=0) as fb:
    print(fb.read())
# File akan ditutup secara otomatis setelah selesai mengolah.

# menggunakan buffering=1
# membuka file dengan mode 'r' (read/baca)
with open("demo.txt", mode='r', buffering=1) as fr:
    print(fr.read())
# File akan ditutup secara otomatis setelah selesai mengolah.
# Jika Anda menggunakan buffering 1 dalam mode binary, 
# maka program akan membaca atau menulis satu byte data biner dari file sekaligus dan menyimpannya dalam buffer.
# Setelah buffer penuh, data akan ditulis atau dikembalikan sebagai output. 
# Namun, ini tidak digunakan dalam mode binary karena dalam mode binary, 
# data yang dibaca atau ditulis biasanya dalam jumlah yang besar, 
# sehingga buffering 1 tidak akan efektif dalam meningkatkan performa program. 
# Jadi, buffering 1 digunakan dalam mode teks yang membaca atau menulis data per baris.

# menggunakan buffering=(lebih besar dari 1)
import io
ukuran_buffer = io.DEFAULT_BUFFER_SIZE
print("Default ukuran buffer:", ukuran_buffer)

# membuka file dengan mode 'r' (read/baca)
with open("demo.txt", mode='r', buffering=ukuran_buffer) as fr:
    print(fr.read())
# File akan ditutup secara otomatis setelah selesai mengolah

# membuka file dengan mode 'r' (read/baca)
with open("demo.txt", mode='r', buffering=5) as fr:
    print(fr.read())
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