# Mode 'w' (write/tulis) untuk menulis isi file
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

# Contoh penggunaan mode 'w' pada objek file adalah sebagai berikut:
with open("filedemo.txt", mode="w") as fileku:
    # menulis string ke file
    fileku.write("hello world\n")
    fileku.write("alice\n")
# File akan ditutup secara otomatis setelah selesai mengolah

# membaca file dengan mode default 'r' (read/baca) atau 't' (text/teks)
with open("filedemo.txt") as f:
    # membaca seluruh isi file
    print(f.read())
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# hello world
# alice

# jika file tersebut sudah ada maka isi file akan ditimpa(overwrite)
dataku = ('='*25, 'carl', 'eliot')
with open("filedemo.txt", mode='w') as fileku:
    # menulis string ke file
    fileku.write("isi file telah ditimpah\n")
    for i in dataku:
        fileku.write(i + '\n')
    fileku.write("ini adalah file demo")
# File akan ditutup secara otomatis setelah selesai mengolah

# membaca file dengan mode default
with open("filedemo.txt") as f:
    print(f.read())
# Output:
# isi file telah ditimpah
# =========================
# carl
# eliot
# ini adalah file demo

# Mode 'w+' untuk menulis dan membaca file
# Saat menggunakan mode ini, kita dapat melakukan operasi baca dan tulis pada file tersebut.
# Jika file yang dibuka dengan mode ini sudah ada, 
# maka isi file tersebut akan ditimpa (overwritten) dengan data yang baru ditulis. 
# Jika file belum ada, maka file tersebut akan dibuat dengan sendirinya.

# Contoh penggunaan mode 'w+' pada objek file adalah sebagai berikut:
dataku = ('alice', 'carl', 'eliot')
with open("filedemo2.txt", mode="w+") as fileku:
    # menulis string ke file
    fileku.write("hello world\n")
    # menulis string lain dari dataku ke file
    for i in dataku:
        fileku.write(i + '\n')
    # menulis string lain lagi ke file
    fileku.write("ini adalah file demo 2")

    print("menulis data ke file selesai.")

    # posisi pointer saat ini ada di akhir file

    # setelah data ditulis ke file berikutnya baca isi file tersebut
    # untuk membaca file yang barusan ditulis ubah dulu posisi pointer file
    # mengatur posisi pointer ke awal file
    fileku.seek(0)
    # membaca seluruh isi file
    print(fileku.read())

# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# menulis data ke file selesai.
# hello world
# alice
# carl
# eliot
# ini adalah file demo 2

# membuat salinan dari file mode_write.py
# with open("mode_write.py", mode='r') as fr:
#     with open("mode_write.py2", mode='w+') as fwr:
#         # membaca isi file
#         isi_file = fr.read()
#         # menulis isi file
#         fwr.write(isi_file)
#         # mengatur posisi pointer ke awal file
#         fwr.seekable(0)
#         # membaca isi file
#         print(fwr.read())

# kode ini setara dengan diatas
# with open("mode_write.py", mode='r') as fr, open("mode_write2.py", mode='w+') as fwr:
#     # membaca isi file
#     isi_file = fr.read()
#     # menulis isi file
#     fwr.write(isi_file)
#     # untuk membaca isi file yang sudah dibaca atau ditulis
#     # kita harus pindahkan posisi pointer file ke awal
#     # posisi pointer saat ini berada di akhir file
#     # mengatur posisi pointer ke awal file
#     fwr.seek(0)
#     # membaca isi file
#     print(fwr.read())
# File akan ditutup secara otomatis setelah selesai mengolah


# Perhatikan bahwa saat menggunakan mode 'w' atau 'w+', 
# isi file akan ditimpa (overwritten) dengan data yang baru ditulis.
# Jika ingin menambahkan data ke file tanpa menghapus isi file yang sebelumnya, 
# dapat menggunakan mode 'a+' (append and read).
