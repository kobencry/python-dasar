# Mode 'wb' untuk menulis data ke file dalam format biner
# Saat menggunakan mode ini, kita tidak dapat membaca isi file,
# namun dapat menulis atau mengubah isi file tersebut. 
# Jika file yang dibuka dengan mode ini sudah ada, 
# maka isi file tersebut akan ditimpa (overwritten) dengan data yang baru ditulis.
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
# dalam contoh ini menggunakan jenis file .png, .txt

# Contoh penggunaan mode 'wb' pada objek file adalah sebagai berikut:
with open("file_gambar.png", mode='rb') as frb:
    # menyalin file_gambar.png
    with open("file_gambar2.png", mode='wb') as fileku:
        # membaca seluruh bytes dari file_gambar.png
        isi_file = frb.read()

        # menulis objek bytes dari isi_file
        fileku.write(isi_file)
# File akan ditutup secara otomatis setelah selesai mengolah
# buka file_gambar2.png

# Mode 'wb+' sama seperti mode 'wb' dan bisa membaca dalam format biner
# Saat menggunakan mode ini, kita dapat melakukan operasi baca dan tulis pada file tersebut.
# Jika file yang dibuka dengan mode ini sudah ada, 
# maka isi file tersebut akan ditimpa (overwritten) dengan data yang baru ditulis. 
# Jika file belum ada, maka file tersebut akan dibuat dengan sendirinya.

# Contoh penggunaan mode 'wb+' pada objek file adalah sebagai berikut:
dataku = ("\x61\x6c\x69\x63\x65", "\x63\x61\x72\x6c", "\x65\x6c\x69\x6f\x74")
with open("filedemo3.txt", mode='wb+') as fileku:
    # menulis string ke file dalam bentuk biner (objek bytes)
    fileku.write("\x68\x65\x6c\x6c\x6f\x20\x77\x6f\x72\x6c\x64\n".encode())
    for i in dataku:
        # menulis string ke file dalam bentuk biner (objek bytes)
        fileku.write(i.encode() + '\n'.encode())
    # menulis string ke file dalam bentuk biner (objek bytes)
    fileku.write("ini adalah file demo 3".encode())
    # untuk membaca isi file yang sudah dibaca atau ditulis
    # kita harus pindahkan posisi pointer ke awal file
    # posisi pointer saat ini berada diakhir file
    # mengatur posisi pointer ke awal
    fileku.seek(0)

    # membaca bytes atau karakter dari file
    # print(fileku.read())

    # jika ingin membaca isi file dalam objek string
    # decode objek bytes menjadi string
    print(fileku.read().decode())
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# hello world
# alice
# carl
# eliot
# ini adalah file demo 3

# Perhatikan bahwa saat menggunakan mode 'wb' atau 'wb+', 
# isi file akan ditimpa (overwritten) dengan data yang baru ditulis.
# Jika ingin menambahkan data ke file tanpa menghapus isi file yang sebelumnya,
# dapat menggunakan mode 'ab+' (append and read binary).
