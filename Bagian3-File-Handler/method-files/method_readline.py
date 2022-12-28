# Method readline() mengembalikan satu baris dari file

# Syntax
# file.readline(size)

# Nilai Parameter
# Parameter             Deskripsi
# size                  Opsional. Jumlah karakter yang ingin dibaca dari file. Nilai default adalah -1, yang berarti semua baris akan dikembalikan.

# membuka file dengan mode default 'r' (read/baca) atau 't' (text/teks)
with open('file_demo_readline.txt') as fileku:
    # membaca baris pertama dari file
    baris_pertama = fileku.readline()
    print("baris 1:", baris_pertama)
    # Output:
    # baris 1: hello world

    # membaca baris kedua dari file
    baris_kedua = fileku.readline()
    print("baris 2:", baris_kedua)
    # Output:
    # baris 2: ini adalah file demo readline
# File akan ditutup secara otomatis setelah selesai mengolah
 
# menggunakan parameter size/ukuran untuk membatasi jumlah karakter yang dibaca.
# Jika jumlah karakter yang dikembalikan melebihi jumlah size/ukuran,
# tidak ada lagi baris yang akan dikembalikan. 
with open('file_demo_readline.txt') as f:
    print("seluruh isi file dari:", f.name) # menggunakan attribut name
    print("-" * 50)
    print(f.read())
    print("-" * 50)
with open('file_demo_readline.txt', 'r') as fileku:
    print("baris 1:", fileku.readline(5))
    print("baris 2:", fileku.readline(20))
    print("baris 3:", fileku.readline(10))
    print("baris 4:", fileku.readline(50))
# Output:
# baris 1: hello
# baris 2:  world
# 
# baris 3: ini adalah
# baris 4:  file demo readline
