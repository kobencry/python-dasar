# Mode 'ab' untuk menambahkan data dalam format biner
# Saat menggunakan mode ini, kita tidak dapat membaca isi file, 
# namun dapat menambahkan data ke file tersebut tanpa menghapus isi file yang sebelumnya.
# Jika file yang dibuka dengan mode ini sudah ada, maka data baru akan ditambahkan di akhir file.
# Jika file belum ada, maka file tersebut akan dibuat dengan sendirinya.

# anda bisa menggunakan beberapa jenis file:
# File gambar: JPG, PNG, GIF, BMP
# File audio: MP3, WAV, MIDI
# File video: MP4, AVI, MKV
# File aplikasi: EXE, DLL, APK
# File DOC (Microsoft Word)
# File DOCX (Microsoft Word Open XML)
# File ODT (OpenDocument Text)
# File PDF (Portable Document Format)
# File RTF (Rich Text Format)
# dalam contoh ini menggunakan jenis file .txt

# Contoh penggunaan mode 'ab' pada objek file adalah sebagai berikut:
with open("filedemo_binary.txt", mode='ab') as fa:
    # menambahkan data string ke file dalam bentuk biner (objek bytes)
    # menggunakan b"" atau method-string encode()
    fa.write("hello world\n".encode())
# File akan ditutup secara otomatis setelah selesai mengolah

with open("filedemo_binary.txt", mode='rb') as fr:
    # jika ingin membaca isi file dalam objek string
    # decode objek bytes menjadi string
    print(fr.read().decode())
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# hello world

dataku = ("\x61\x6c\x69\x63\x65", "\x63\x61\x72\x6c", "\x65\x6c\x69\x6f\x74")
with open("filedemo_binary.txt", mode='ab') as fa:
    # menambahkan data string lain ke file dalam bentuk biner (objek bytes)
    for i in dataku:
        fa.write(i.encode() + b'\n')
# File akan ditutup secara otomatis setelah selesai mengolah

# Mode 'ab+' sama seperti mode 'ab' dan bisa membaca file dalam format biner
# Saat menggunakan mode ini, kita dapat melakukan operasi baca dan tulis pada file tersebut.
# Jika file yang dibuka dengan mode ini sudah ada, maka data baru akan ditambahkan di akhir file.
# Jika file belum ada, maka file tersebut akan dibuat dengan sendirinya.

# Contoh penggunaan mode 'ab+' pada objek file adalah sebagai berikut:
with open("filedemo_binary.txt", mode='ab+') as far:
    # menambahkan data string lain ke file dalam bentuk biner (objek bytes)
    far.write(b"ini adalah file demo binary")

    # untuk membaca isi file yang sudah dibaca atau ditulis
    # kita harus pindahkan posisi pointer ke awal file
    # posisi pointer(cursor) saat ini berada diakhir file
    # mengatur posisi pointer(cursor) ke awal
    far.seek(0)

    # membaca isi file dalam biner
    # print(far.read())

    # membaca isi file dalam string
    print(far.read().decode())
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# hello world
# alice
# carl
# eliot
# ini adalah file demo binary

# Perhatikan bahwa saat menambahkan data ke file dengan mode 'ab' atau 'ab+',
# data yang ditambahkan harus dalam bentuk objek bytes.
# Oleh karena itu, jika ingin menambahkan string ke file, maka perlu dilakukan encode() terlebih dahulu.
