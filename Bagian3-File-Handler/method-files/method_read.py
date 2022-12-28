# Method read() adalah method yang digunakan untuk membaca isi dari sebuah file.
# Method ini akan mengembalikan seluruh isi file yang dibaca sebagai string.

# Syntax
# file.read(size)

# Nilai Parameter
# Parameter                 Deskripsi
# size                      Opsional. Jumlah karakter yang ingin dibaca dari file. Nilai default adalah -1, yang berarti semua baris akan dikembalikan.

# Berikut ini adalah contoh penggunaan method read():
# membuka file dengan mode default 'r' (read/baca) atau 't' (text/teks)
with open('file_demo_read.txt') as fileku:
    isi_file = fileku.read()
# File akan ditutup secara otomatis setelah selesai mengolah
print(isi_file)
# Output:
# hello world
# ini adalah file demo read

# Jumlahkan seluruh karakter 
with open('file_demo_read.txt') as fileku:
    isi_file = fileku.read()
    print("jumlah karakter:", len(isi_file))
    # Output:
    # 38
    # karakter spesial juga dihitung seperti \n(newline), spasi dll.
# File akan ditutup secara otomatis setelah selesai mengolah

# Jika anda ingin membaca file dengan ukuran yang lebih kecil, atau sebagian dari isi file
with open('file_demo_read.txt') as fileku:
    # membaca 11 karakter pertama dari file
    isi_file = fileku.read(11)
    print(isi_file)
    # Output:
    # hello world
# File akan ditutup secara otomatis setelah selesai mengolah

# menggunakan parameter size/ukuran untuk membatasi jumlah karakter yang dibaca.
# Jika jumlah karakter yang dikembalikan melebihi jumlah size/ukuran,
# tidak ada lagi baris yang akan dikembalikan. 
with open('file_demo_read.txt') as fileku:
    # membaca 50 karakter dari file
    isi_file2 = fileku.read(50)
    print(isi_file2)
    # Output:
    # hello world
    # ini adalah file demo read

# Perlu diingat bahwa method read() akan mengembalikan seluruh isi file sebagai string, 
# jadi jika file tersebut merupakan file teks biasa, maka kamu bisa langsung 
# menampilkan isi file tersebut dengan mencetak string tersebut. 
# Namun, jika file tersebut merupakan file biner (misalnya, file gambar atau file audio), 
# maka kamu harus menggunakan library yang sesuai untuk memproses file tersebut sebelum dapat menampilkannya.
