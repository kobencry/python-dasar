# -- Method String --

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi decode() digunakan untuk mengkonversi dari satu skema pengkodean, 
# di mana string argumen dikodekan ke skema encoding/pengkodean yang diinginkan.
# Ini bekerja berlawanan dengan fungsi encode(). 
# Ia menerima pengkodean string encoding/pengkodean untuk memecahkan kode 
# dan mengembalikan string asli.

# Syntax
# string.decode(encoding=encoding, errors=errors)

# Nilai Parameter
# Parameter         Deskripsi
# encoding          opsional. Menentukan pengkodean atas dasar yang decoding harus dilakukan
# errors            opsional. String yang menentukan method kesalahan. Nilai-nilai yang diperbolehkan adalah
#                   backslashreplace, ignore, namereplace, strict, replace, xmlcharrefreplace

alphabet = "αβγδεζηθικλμνξοπρςστυφχψ"
alpha_utf_8 = alphabet.encode()
print(alpha_utf_8)
print(alpha_utf_8.decode())

# Contoh-contoh ini menggunakan ascii encoding ,  dan karakter yang tidak dapat dikodekan, 
# menunjukkan hasil dengan kesalahan yang berbeda:

# 'backslashreplace'  : Menggunakan backslash bukan karakter yang tidak bisa dikodekan 
# 'ignore'            : Mengabaikan karakter yang tidak dapat dikodekan
# 'namereplace'       : Mengganti karakter dengan teks yang menjelaskan karakter
# 'strict'            : Default, memunculkan kesalahan runtime pada kegagalan
# 'replace'           : Mengganti karakter dengan tanda tanya
# 'xmlcharrefreplace' : Mengganti karakter dengan karakter xml

# ini hanyalah sebuah contoh sederhana untuk memahaminya, 
# tutorial ini parameternya diubah menjadi 'ascii', bagaimana cara fungsi decode()
# bekerja jika karakter string tidak tertangani.

txt = "ålice"
var = txt.encode()
# errors
print(var.decode(encoding="ascii", errors="backslashreplace"))  # \xc3\xa5lice
# passed
# print(var.decode(encoding="utf-8", errors="backslashreplace"))  # ålice

# ingat perameter maupun di tulis atau tidak opsional defaultnya utf-8
txt = "ålice"
var = txt.encode()
# errors
print(var.decode("ascii", "ignore"))    # lice
# passed
# print(var.decode("utf-8", "ignore"))    # ålice

txt = "ålice"
var = txt.encode()
# errors
print(var.decode("ascii", "replace"))   # ��lice
# passed
# print(var.decode()) # ålice

txt = "ålice"
var = txt.encode()
# errors
print(var.decode("latin", "namereplace"))   # Ã¥lice
# passed
print(var.decode()) # ålice

txt = "ålice"
var = txt.encode()
# errors
print(var.decode("latin", "xmlcharrefreplace")) # Ã¥lice
# passed
print(var.decode()) # ålice

txt = "ålice"
var = txt.encode()
# passed
print(var.decode("latin", "strict")) # Ã¥lice

# errors
print(var.decode("ascii", "strict")) # kesalahan runtime Traceback UnicodeEncodeError
