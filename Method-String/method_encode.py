# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=encode#str.encode

# https://docs.python.org/3/library/codecs.html#standard-encodings

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

# strict (default)      : menimbulkan pengecualian UnicodeError pada kegagalan
# backslashreplace      : karakter yang tidak dapat dikodekan diganti dengan garis miring terbalik
# ignore                : karakter yang tidak dapat dikodekan diabaikan
# namereplace           : karakter yang tidak dapat dikodekan diganti dengan namanya
# replace               : karakter yang tidak dapat dikodekan diganti dengan tanda tanya
# xmlcharrefreplace     : karakter yang tidak dapat dikodekan diganti dengan karakter xml
# surrogateescape       : karakter yang tidak dapat diwakili dalam encoding yang digunakan saat ini. 

txt1 = "ålice"
print(txt1.encode(encoding="ascii",errors="backslashreplace"))   # b'\\xe5lice'

txt2 = "ålice"
print(txt2.encode(encoding="ascii",errors="ignore"))             # b'lice'

txt3 = "ålice"
print(txt3.encode(encoding="ascii",errors="namereplace"))        # b'\\N{LATIN SMALL LETTER A WITH RING ABOVE}lice'

txt4 = "ålice"
print(txt4.encode(encoding="ascii",errors="replace"))            # b'?lice'

txt5 = "ålice"
print(txt5.encode(encoding="ascii",errors="xmlcharrefreplace"))  # b'&#229;lice'

print(txt1.encode(encoding="utf-8",errors="surrogateescape"))   # b'\xc3\xa5lice'
print(txt2.encode(encoding="utf-8",errors="surrogateescape"))   # b'\xc3\xa5lice'
print(txt3.encode(encoding="utf-8",errors="surrogateescape"))   # b'\xc3\xa5lice'
print(txt4.encode(encoding="utf-8",errors="surrogateescape"))   # b'\xc3\xa5lice'
print(txt5.encode(encoding="utf-8",errors="surrogateescape"))   # b'\xc3\xa5lice'

txt7 = "ålice"
print(txt7.encode(encoding="ascii",errors="strict"))             # kesalahan runtime Traceback UnicodeEncodeError
