# -- Fungsi bawaan python --

# https://docs.python.org/3/library/stdtypes.html?highlight=lower#bytearray

# fungsi bytearray() mengembalikan objek bytearray.
# itu dapat mengubah objek menjadi objek bytearray, 
# atau membuat objek bytearray kosong dengan ukuran yang ditentukan.

# Syntax
# bytearray(x, encoding, errors)

# Nilai Parameter
# Parameter             Deskripsi
# x                     Sumber untuk digunakan saat membuat objek bytearray.
#                       Jika itu adalah bilangan bulat, objek bytearray kosong
#                       dengan ukuran yang ditentukan akan dibuat.
#                       Jika itu adalah String, pastikan Anda menentukan pengkodean sumber.

# encoding              Pengkodean string
# errors                Menentukan apa yang harus dilakukan jika penyandian/pengkodean gagal.

# menggunakan tipe string
x = "hello world!"
byte_x = bytearray(x, 'utf-8')
print(byte_x)   # bytearray(b'hello world!')

# menggunakan tipe string
x = "python 🐍"
byte_x = bytearray(x, encoding='utf-8')
print(byte_x)   # bytearray(b'python \xf0\x9f\x90\x8d')

# 'ignore' mengabaikan karakter yang tidak dapat dikodekan.
x = "python 🐍"
byte_x = bytearray(x, encoding='ascii', errors="ignore")
print(byte_x)   # bytearray(b'python ')

# menggunakan tipe integer
# Membuat instance/hal yang berisi nol dengan panjang tertentu
x = 10
byte_x = bytearray(x)
print(byte_x)   # bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

# menggunakan tipe range
# Membuat instance/hal yang berisi tabel ascii
x = range(97, 123)
byte_x = bytearray(x)
print(byte_x)   # bytearray(b'abcdefghijklmnopqrstuvwxyz')

# menggunakan tipe list
# Membuat instance/hal yang berisi tabel ascii
x = [104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]
byte_x = bytearray(x)
print(byte_x)   # bytearray(b'hello world')

# menggunakan tipe tuple
# Membuat instance/hal yang berisi tabel ascii
x = (97, )
print(bytearray(x)) # bytearray(b'a')
# nilai tabel kode ascii
print(bytearray((104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100)))
# bytearray(b'hello world')
# nilai hexa
x = (0x68, 0x65, 0x6c, 0x6c, 0x6f, 0x20, 0x77, 0x6f, 0x72, 0x6c, 0x64)
print(bytearray(x)) # bytearray(b'hello world')

# bytearray.fromhex(string)
# Metode kelas bytearray ini mengembalikan objek bytearray, mendekode objek string yang diberikan.
# String harus berisi dua digit heksadesimal per byte, dengan karakter spasi kosong ASCII diabaikan.

# Syntax
# bytearray.fromhex(string)

# Nilai Parameter
# Parameter             Deskripsi
# string                Dibutuhkan. string yang berisi angka hex.

str_hexa = "48 65 6c 6c 6f 20 77 6f 72 6c 64"
x = bytearray.fromhex(str_hexa)
print(x)    # bytearray(b'Hello world')

# bytearray().hex()
# Mengembalikan objek string yang berisi dua digit heksadesimal untuk setiap byte dalam instance.
x = b"\x68\x65\x6c\x6c\x6f\x20\x77\x6f\x72\x6c\x64"
print(bytearray(x).hex())   # 68656c6c6f20776f726c64

str_hex = bytearray(x).hex() # 68656c6c6f20776f726c64
print(bytearray.fromhex(str_hex))   # bytearray(b'hello world')

# jika ingin mempelajari lebih lanjut tentang python-encoding tabel ascii kunjungi folder_name: "python-encoding"
# jika ingin mempelajari lebih lanjut tentang python-encoding kunjungi folder_name: "python-encoding"
# jika ingin mempelajari lebih lanjut tentang Method-String encode() kunjungi folder_name: "Method-String/method_encode.py"
