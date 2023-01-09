# attribut 'errors' menyimpan informasi tentang error yang terjadi saat membuka atau menulis file. 
# Nilainya hanya berlaku untuk file yang berisi teks (text file).

# Syntax
# file.errors

# Nilai Parameter
# tidak ada nilai parameter

# Tabel di bawah ini menentukan skema penanganan kesalahan yang berbeda 

# strict (Default)  - memunculkan pengecualian UnicodeError pada kegagalan
# backslashreplace  - karakter yang tidak dapat dikodekan diganti dengan garis miring terbalik
# ignore            - karakter yang tidak dapat dikodekan diabaikan
# namereplace       - karakter yang tidak dapat dikodekan diganti dengan namanya
# replace           - karakter yang tidak dapat dikodekan diganti dengan tanda tanya
# xmlcharrefreplace - karakter yang tidak dapat dikodekan diganti dengan karakter xml
# surrogateescape   - karakter yang tidak dapat diwakili dalam encoding yang digunakan saat ini. 

# membuka file dengan mode default 'r' (read/baca) atau 't' (text/teks)
with open("example.txt") as f:
    print("jenis penanganan error:", f.errors)
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# jenis penanganan error: strict

# membuka file dengan mode default 'r' (read/baca) atau 't' (text/teks)
with open("example.txt", errors='ignore') as f:
    print("jenis penanganan error:", f.errors)
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# jenis penanganan error: ignore 
