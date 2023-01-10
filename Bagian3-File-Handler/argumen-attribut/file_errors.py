# Argumen errors pada method open() di Python merupakan argumen opsional
# yang menentukan bagaimana kesalahan encoding dan decoding ditangani. 
# Argumen ini tidak dapat digunakan dalam mode biner. 
# Berbagai penangan kesalahan standar tersedia (tercantum di bawah Penangan Kesalahan).
# Menangani Kesalahan Encoding dan Decoding
# Secara default, Python memunculkan pengecualian UnicodeError pada kesalahan encoding atau decoding.
# Namun, Anda dapat menentukan bagaimana kesalahan ini ditangani menggunakan parameter errors.
# Tabel di bawah ini menentukan skema penanganan kesalahan yang berbeda

# strict (Default)  - memunculkan pengecualian UnicodeError pada kegagalan
# backslashreplace  - karakter yang tidak dapat dikodekan diganti dengan garis miring terbalik
# ignore            - karakter yang tidak dapat dikodekan diabaikan
# namereplace       - karakter yang tidak dapat dikodekan diganti dengan namanya
# replace           - karakter yang tidak dapat dikodekan diganti dengan tanda tanya
# xmlcharrefreplace - karakter yang tidak dapat dikodekan diganti dengan karakter xml
# surrogateescape   - karakter yang tidak dapat diwakili dalam encoding yang digunakan saat ini. 

# membuka file dengan mode default 'r' (read/baca) atau 't' (text/teks)
with open("demo.txt", encoding='ascii', errors='replace') as fr:
    # membaca isi file
    print(fr.read())
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# hello world ���
# ��lice
# carl ����
# eliot ����
# ini adalah file example ���

# Diatas hanya sebagai contoh untuk menghasilkan Output karakter tanda tanya
# jika ingin Outputnya normal gunakan encoding='utf-8'
# with open("demo.txt", encoding='utf-8', errors='replace')

#--------------------------------------------------------------------

# attribut 'errors' menyimpan informasi tentang error yang terjadi saat membuka atau menulis file. 
# Nilainya hanya berlaku untuk file yang berisi teks (text file).

# Syntax
# file.errors

# Nilai Parameter
# tidak ada nilai parameter
# membuka file dengan mode default 'r' (read/baca) atau 't' (text/teks)
with open("demo.txt", encoding='ascii', errors='ignore') as fr:
    # membaca isi file
    print(fr.read())
    print("jenis penanganan error:", fr.errors)
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# hello world
# lice
# carl
# eliot
# ini adalah file example
# jenis penanganan error: ignore

# Diatas hanya sebagai contoh untuk menghasilkan Output karakter diabaikan
# jika ingin Outputnya normal gunakan encoding='utf-8'
# with open("demo.txt", encoding='utf-8', errors='replace')

# menggunakan jenis errors default
# membuka file dengan mode default 'r' (read/baca) atau 't' (text/teks)
with open("demo.txt") as f:
    print("jenis penanganan error:", f.errors)
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# jenis penanganan error: strict