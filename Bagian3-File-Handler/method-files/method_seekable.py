# Method seekable() mengembalikan nilai boolean True jika file dapat dicari.
# Jika tidak maka akan mengembalikan nilai boolean False

# Syntax
# file.seekable()

# Nilai Parameter
# tidak ada nilai parameter

# Berikut ini adalah contoh penggunaan method seekable() di Python:

# membuka file dengan mode default 'r' (read/baca) atau 't' (text/teks)
with open('file_demo_seek.txt') as fileku:
    # periksa apakah isi file dapat dicari
    if fileku.seekable():
        # mengatur posisi pointer ke akhir
        fileku.seek(11)
        # baca seluruh isi file
        print(fileku.read(11))
        # Output:
        # alice
        # carl
    else:
        print("file tidak dapat dicari")
# File akan ditutup secara otomatis setelah selesai mengolah


with open('file_logo_python.png', 'rb') as f:
    print("apakah isi file dapat dicari:", f.seekable())
    # Output:
    # apakah isi file dapat dicari: True
# File akan ditutup secara otomatis setelah selesai mengolah
