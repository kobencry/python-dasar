# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=encode#str.encode

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi encode() mengkodekan string, menggunakan pengkodean tertentu.
# Jika tidak ada pengkodean yang ditentukan, secara default UTF-8 akan digunakan.

# Syntax
# string.encode(encoding=encoding, errors=errors)

# Nilai Parameter
# Parameter         Deskripsi
# encoding          opsional. String yang menentukan pengkodean yang akan digunakan. Standarnya adalah UTF-8
# errors            opsional. String yang menentukan method kesalahan. Nilai-nilai yang diperbolehkan adalah
#                   backslashreplace, ignore, namereplace, strict, replace, xmlcharrefreplace

nama1 = "alice"
nama2 = "ålice"
print(nama1.encode())   # b'alice'
print(nama2.encode())   # b'\xc3\xa5lice'

# pelajari lebih lanjut tentang decode() folder_name: "Method-String/method_decode.py"
print(b'\xc3\xa5lice'.decode()) # ålice

# Contoh-contoh ini menggunakan ascii encoding ,  dan karakter yang tidak dapat dikodekan, 
# menunjukkan hasil dengan kesalahan yang berbeda:

# 'backslashreplace'  : Menggunakan backslash bukan karakter yang tidak bisa dikodekan 
# 'ignore'            : Mengabaikan karakter yang tidak dapat dikodekan
# 'namereplace'       : Mengganti karakter dengan teks yang menjelaskan karakter
# 'strict'            : Default, memunculkan kesalahan runtime pada kegagalan
# 'replace'           : Mengganti karakter dengan tanda tanya
# 'xmlcharrefreplace' : Mengganti karakter dengan karakter xml

txt = "ålice"

print(txt.encode(encoding="ascii",errors="backslashreplace"))   # b'\\xe5lice'
print(txt.encode(encoding="ascii",errors="ignore"))             # b'lice'
print(txt.encode(encoding="ascii",errors="namereplace"))        # b'\\N{LATIN SMALL LETTER A WITH RING ABOVE}lice'
print(txt.encode(encoding="ascii",errors="replace"))            # b'?lice'
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))  # b'&#229;lice'
print(txt.encode(encoding="ascii",errors="strict"))             # kesalahan runtime Traceback UnicodeEncodeError
