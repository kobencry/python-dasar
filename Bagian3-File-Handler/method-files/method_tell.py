# Method tell() digunakan untuk mengetahui posisi pointer(cursor) pada file yang terbuka saat ini.
# Method ini tidak memiliki argument dan selalu mengembalikan nilai integer yang menunjukkan posisi file pointer dalam byte.

# Syntax
# file.tell()

# Nilai Parameter
# tidak ada nilai parameter

# Berikut ini adalah contoh penggunaan method tell() di Python:

# membuka file dengan mode default 'r' (read/baca) atau 't' (text\teks)
with open('file_demo_tell.txt') as fileku:
    # mengetahui posisi pointer(cursor) saat ini
    print("posisi pointer saat ini:", fileku.tell())
    # membaca sebanyak 6 byte atau karakter dari file
    s = fileku.read(6)
    print(s)
    # mengetahui posisi pointer(cursor) saat ini
    posisi = fileku.tell()
    print("posisi pointer saat ini:", posisi)
    # tampilkan dengan method repr() dan slice string
    print("posisi karakter saat ini:", repr(s[posisi - 1]))
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# posisi pointer saat ini: 0
# hello
# posisi pointer saat ini: 6
# posisi karakter saat ini: ' '

# membuka file dengan mode 'w' (write/tulis)
with open('file_demo_tell2.txt', 'w') as fileku:
    # mengetahui posisi pointer(cursor) saat ini
    print("posisi pointer saat ini:", fileku.tell())
    fileku.write("hello world")
    print("posisi pointer saat ini:", fileku.tell())
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# posisi pointer saat ini: 0
# posisi pointer saat ini: 11

# jika ingin mengetahui tentan fungsi bawaan repr() pada python kunjungi folder_name: 'Fungsi-Bawaan/fungsi_repr.py'
