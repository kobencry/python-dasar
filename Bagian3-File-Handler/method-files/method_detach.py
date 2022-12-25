# Method detach() Mengembalikan aliran mentah yang dipisahkan dari buffer.
# berguna untuk memisahkan objek file dari objek wrapper yang mengelola file tersebut.

# Syntax
# file.detach()

# Nilai Parameter
# tidak ada nilai parameter

# membuka file dengan mode 'r' (read/baca)
fileku =  open('file_demo_detach.txt', 'r')
    # periksa jika fileku ada tampilkan pesan
if fileku:
    print("berhasil membuka file:", fileku.name)
# berikutnya jalankan kode dibawah ini
print(fileku.detach())
# Setelah itu, diperoleh hasil dari metode detach(). 
# Ini menampilkan aliran mentah file dari kelas BufferedReader.
# output:
# berhasil membuka file: file_demo_detach.txt
# <_io.BufferedReader name='file_demo_detach.txt'>

# membuka file dengan mode 'w+' untuk membaca dan menulis
fileku = open('file_demo_detach.txt', 'w+')
fileku.write('hello world')
fileku.seek(0)
print(fileku.read())
print(fileku.detach())
# mengembalikan isi file dan aliran mentah I/O teks
# output:
# hello world
# <_io.BufferedRandom name='file_demo_detach.txt'>
