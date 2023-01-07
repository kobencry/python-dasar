# Mode 'a' untuk menambah data ke file
# Saat menggunakan mode ini, kita tidak dapat membaca isi file, 
# namun dapat menambahkan data ke file tersebut tanpa menghapus isi file yang sebelumnya.
# Jika file yang dibuka dengan mode ini sudah ada, maka data baru akan ditambahkan di akhir file.
# Jika file belum ada, maka file tersebut akan dibuat dengan sendirinya.

# Contoh penggunaan mode 'a' pada objek file adalah sebagai berikut:
# filedemo.txt hanya memiliki data "hello world"
# membuka file dengan mode default 'r' (read/baca) atau 't' (text/teks)
with open("filedemo.txt") as fr:
    # membaca isi file
    print(fr.read())
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# hello world

dataku = ('alice', 'carl', 'eliot')
# membuka file dengan mode 'a' (append/menambahkan)
with open("filedemo.txt", mode='a') as fa:
    # menambahkan data ke file
    for i in dataku:
        fa.write(i + '\n')
# File akan ditutup secara otomatis setelah selesai mengolah

# setelah file ditambahkan
with open("filedemo.txt") as fr:
    print(fr.read())
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# hello world
# alice
# carl
# eliot

# kode ini setara dengan diatas dimulai dari baris (31 - 38)
with open("filedemo.txt", mode='a') as fa, open("filedemo.txt") as fr:
    # menulis data lain ke file
    fa.write("ini adalah file demo")

    # untuk membaca isi file yang sudah dibaca atau ditulis
    # kita harus pindahkan posisi pointer file ke awal
    # posisi pointer saat ini berada di akhir file
    # mengatur posisi pointer saat ini ke awal file
    fa.seek(0)

    # membaca isi file
    print(fr.read())
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# hello world
# alice
# carl
# eliot
# ini adalah file demo

# Mode 'a+' untuk menambahkan dan membaca isi file
# Saat menggunakan mode ini, kita dapat melakukan operasi baca dan tulis pada file tersebut.
# Jika file yang dibuka dengan mode ini sudah ada, maka data baru akan ditambahkan di akhir file.
# Jika file belum ada, maka file tersebut akan dibuat dengan sendirinya.

# Contoh penggunaan mode 'a+' pada objek file adalah sebagai berikut:
# membuat filedemo2.txt
with open("filedemo2.txt", mode='a+') as far:
    # menambahkan data ke file
    far.write("hello world\n")

    # untuk membaca isi file yang sudah dibaca atau ditulis
    # kita harus pindahkan posisi pointer file ke awal
    # posisi pointer saat ini berada di akhir file
    # mengatur posisi pointer saat ini ke awal file
    far.seek(0)

    # membaca isi file
    print(far.read())
    # Output:
    # hello world

    # menambahkan data lain ke file
    for i in dataku:
        far.write(i + '\n')

    # untuk membaca isi file yang sudah dibaca atau ditulis
    # kita harus pindahkan posisi pointer file ke awal
    # posisi pointer saat ini berada di akhir file
    # mengatur posisi pointer saat ini ke awal file
    far.seek(0)

    # membaca isi file
    print(far.read())
    # setelah data ditambahkan
    # Output:
    # hello world
    # alice
    # carl
    # eliot

    # menambahkan data lain ke file
    far.write("ini adalah file demo 2")

    # posisi pointer saat ini berada di akhir file
    # mengatur posisi pointer saat ini ke awal file
    far.seek(0)

    # membaca isi file
    print(far.read())
    # setelah data ditambahkan
    # Output:
    # hello world
    # alice
    # carl
    # eliot
    # ini adalah file demo 2
# File akan ditutup secara otomatis setelah selesai mengolah

# Perhatikan bahwa saat menggunakan mode 'a+', 
# posisi pointer(cursor) akan berada di akhir file setelah melakukan operasi menambahkan data.
# Jika ingin membaca isi file dari awal, maka perlu dipindahkan terlebih dahulu menggunakan method seek().
