# -- Fungsi bawaan python --

# https://docs.python.org/3/library/stdtypes.html?highlight=lower#bytes

# fungsi bytes() mengembalikan objek byte.
# itu dapat mengubah objek menjadi objek byte, atau membuat objek byte 
# kosong dengan ukuran yang ditentukan.
# Perbedaan antara fungsi-bawaan bytes() dan bytearray() adalah 
# fungsi bytes() mengembalikan objek yang tidak dapat dimodifikasi, dan
# fungsi bytearray() mengembalikan objek yang dapat dimodifikasi.

# Syntax
# bytes(x, encoding, errors)

# Nilai Parameter:
# Parameter	                Deskripsi
# x                         Sumber untuk digunakan saat membuat objek byte.
#                           Jika itu adalah bilangan bulat, objek byte kosong dengan ukuran yang ditentukan akan dibuat.
#                           Jika itu adalah String, pastikan Anda menentukan pengkodean sumbernya.

# encoding                  pengkodean string
# errors                    Menentukan apa yang harus dilakukan jika penyandian/pengkodean gagal.

# menggunakan tipe string
x = "hello world!"
byte_x = bytes(x, 'utf-8')
print(byte_x)   # b'hello world!'

x = "python 🐍"
byte_x = bytes(x, encoding='utf-8')
print(byte_x)   # # bytearray(b'python \xf0\x9f\x90\x8d')

# 'ignore' mengabaikan karakter yang tidak dapat dikodekan.
x = "python 🐍"
byte_x = bytes(x, encoding='ascii', errors="ignore")
print(byte_x)   # b'python '

# menggunakan tipe integer
# Membuat instance/hal yang berisi nol dengan panjang tertentu
x = 10
byte_x = bytes(x)
print(byte_x)   # b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

# menggunakan tipe range
# Membuat instance/hal yang berisi tabel ascii
x = range(97, 123)
byte_x = bytes(x)
print(byte_x)   # b'abcdefghijklmnopqrstuvwxyz'

# menggunakan tipe list
# Membuat instance/hal yang berisi tabel ascii
x = [104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]
byte_x = bytes(x)
print(byte_x)   # b'hello world'

# menggunakan tipe tuple
# Membuat instance/hal yang berisi tabel ascii
x = (97, )
print(bytes(x)) # b'a'
# nilai tabel kode ascii
print(bytes((104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100)))
# b'hello world'
# nilai hexa
x = (0x68, 0x65, 0x6c, 0x6c, 0x6f, 0x20, 0x77, 0x6f, 0x72, 0x6c, 0x64)
print(bytes(x)) # b'hello world'

# bytes.fromhex(string)
# Metode kelas byte ini mengembalikan objek byte, mendekode objek string yang diberikan.
# String harus berisi dua digit heksadesimal per byte, dengan karakter spasi kosong ASCII diabaikan.

# Syntax
# bytes.fromhex(string)

# Nilai Parameter
# Parameter             Deskripsi
# string                Dibutuhkan. string yang berisi angka hex.

str_hexa = "48 65 6c 6c 6f 20 77 6f 72 6c 64"
x = bytes.fromhex(str_hexa)
print(x)    # b'Hello world'

# bytes().hex()
# Mengembalikan objek string yang berisi dua digit heksadesimal untuk setiap byte dalam instance.
x = b"\x68\x65\x6c\x6c\x6f\x20\x77\x6f\x72\x6c\x64"
print(bytes(x).hex())   # 68656c6c6f20776f726c64

str_hex = bytes(x).hex() # 68656c6c6f20776f726c64
print(bytes.fromhex(str_hex))   # b'hello world'

# jika ingin mempelajari lebih lanjut tentang python-encoding tabel ascii kunjungi folder_name: "python-encoding"
# jika ingin mempelajari lebih lanjut tentang python-encoding kunjungi folder_name: "python-encoding"
# jika ingin mempelajari lebih lanjut tentang Method-String encode() kunjungi folder_name: "Method-String/method_encode.py"
