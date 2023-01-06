# Mode 'rb' (read binary) untuk membaca file dalam format biner.
# Saat menggunakan mode ini, kita tidak dapat menulis atau mengubah isi dari file tersebut.
# Jika file tidak ditemukan atau file tidak ada atau tidak bisa dibuka dengan mode 'rb',
# maka akan terjadi exception FileNotFoundError atau PermissionError.

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

# Contoh penggunaan mode 'rb' pada objek file adalah sebagai berikut:
with open("file_gambar.png", mode='rb') as fileku:
    # membaca seluruh isi file gambar
    # print(fileku.read())

    # membaca sebanyak 20 bytes atau karakter dari file gambar
    print(fileku.read(20))
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\xc8'

# Baca file executable
with open("test.exe", mode='rb') as fileku:
    # membaca sebanyak 20 bytes atau karakter dari file exe
    print(fileku.read(20))
# Output:
# b'MZ\x90\x00\x03\x00\x00\x00\x04\x00\x00\x00\xff\xff\x00\x00\xb8\x00\x00\x00'

# Mode 'rb+' sama seperti mode 'rb' dan bisa menulis dalam format biner
# Saat menggunakan mode ini, kita dapat melakukan operasi baca dan tulis pada file tersebut.
# Jika file tidak ditemukan atau file tidak ada atau tidak bisa dibuka dengan mode 'rb+',
# maka akan terjadi exception FileNotFoundError atau PermissionError.

# Contoh penggunaan mode 'r+' pada objek file adalah sebagai berikut:
with open("file_demo_write_bytes.txt", mode='rb+') as fileku:
    # Menulis string ke file dalam bentuk biner (objek bytes)
    # dengan Method-String encode()
    fileku.write("hello world\n".encode())
    # atau menggunakan b""
    fileku.write(b"alice \xe2\x9c\xa8")

    # untuk membaca isi file yang sudah dibaca atau ditulis
    # kita harus pindahkan posisi pointer file ke awal
    # posisi pointer saat ini berada di akhir file
    # mengatur posisi pointer ke awal file
    fileku.seek(0)
    # membaca isi file
    # Decode objek bytes menjadi string
    print(fileku.read().decode())

# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# hello world
# alice ✨
# jika anda menggunakan terminal di windows, karakter setelah alice 
# akan menampilkan abstrak kotak, �, atau â¨

# fungsi untuk membaca isi file byte
def baca_file_byte(nama_file, nilai_byte):
    # membaca dengan mode 'rb'
    with open(nama_file, mode='rb') as fileku:
        # looping dengan while jika kondisi bernilai True
        while True:
            # membaca sebanyak 1 bytes atau karakter dari file
            data_byte = fileku.read(1)
            # periksa jika kondisi True masukan data ke keyword "yield"
            if data_byte:
                yield data_byte
            # jika kondisi diatas tidak terpenuhi jalankan kode program dibawah ini:
            else:
                break
            # periksa nilai_byte lebih besar dari 0
            if nilai_byte > 0:
                # nilai_byte akan di dekremen/dikurangi
                nilai_byte -= 1
                # periksa jika nilai_byte sama dengan 0 kode program berhenti
                if nilai_byte == 0:
                    break
# jalankan fungsi baca_file_byte() dengan forloop
for b in baca_file_byte("file_gambar.png", 20):
    i = int.from_bytes(b, 'big')
    print(f"raw: {b} \t hex: {hex(i)} \t int: {i} \t binary: {bin(i)}")
