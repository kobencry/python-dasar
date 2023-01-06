# Mode 'r' (read/baca) untuk membaca isi file.
# Saat menggunakan mode ini, kita tidak dapat menulis atau mengubah isi dari file tersebut.
# Jika file tidak ditemukan atau file tidak ada atau tidak bisa dibuka dengan mode 'r', 
# maka akan terjadi exception FileNotFoundError atau PermissionError.

# Contoh penggunaan mode 'r' pada objek file adalah sebagai berikut:
with open("filedemo.txt", mode='r') as fileku:
    # membaca seluruh isi file
    print(fileku.read())
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# hello world
# alice
# carl
# eliot
# ini adalah file demo

# anda juga bisa menggunakan mode default ini setara dengan mode 'r' atau 'rt' (read/baca, text/teks)
with open("filedemo.txt") as fileku:
    # membaca sebanyak 17 bytes atau karakter dari file
    print(fileku.read(17))
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# hello world
# alice

# Mode 'r+' (read/baca, write/tulis) untuk membaca dan menulis isi file.
# Saat menggunakan mode ini, kita dapat melakukan operasi baca dan tulis pada file tersebut.
# Jika file tidak ditemukan atau file tidak ada atau tidak bisa dibuka dengan mode 'r+',
# maka akan terjadi exception FileNotFoundError atau PermissionError.

# Contoh penggunaan mode 'r+' pada objek file adalah sebagai berikut:
with open("filedemo2.txt", mode='r+') as fileku:
    # membaca isi file
    print(fileku.read())
    # Output:
    # hello world

    # menulis string ke file
    fileku.write('Ini adalah string yang ditulis menggunakan mode r+\n')
    print("menulis ke file selesai.")

    # mengatur posisi pointer ke awal
    fileku.seek(0)

    # membaca isi file
    print(fileku.read())
    # Output:
    # menulis ke file selesai.
    # hello world
    # Ini adalah string yang ditulis menggunakan mode r+
# File akan ditutup secara ototmatis setelah selesai mengolah

# menyalin file dengan mode 'r+'
with open("filedemo.txt", mode='r') as f:
    with open("filedemo_copy.txt", mode='r+') as fileku:
        # membaca isi file
        isi_file = f.read()

        # menulis string ke file
        fileku.write(isi_file)

        # untuk membaca isi file yang sudah dibaca atau ditulis
        # kita harus pindahkan posisi pointer file ke awal
        # posisi pointer saat ini berada di akhir file
        # mengatur posisi pointer saat ini ke awal file
        fileku.seek(0)

        # membaca isi file
        print(fileku.read())
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# hello world
# alice
# carl
# eliot
# ini adalah file demo 
