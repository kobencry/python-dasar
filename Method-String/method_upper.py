# -- Method String -- 

# https://docs.python.org/3/library/stdtypes.html?highlight=upper#str.upper

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi upper() mengembalikan string dimana semua karakter dalam huruf besar.
# simbol dan angka diabaikan.

# Syntax
# string.upper()

# Nilai Parameter
# Tidak ada nilai parameter

s = "hello world!".upper()
print(s)    # HELLO WORLD!

s = "99hello world".upper()
print(s)    # 99HELLO WORLD

print("#hello_world123@gmail.com".upper())  # #HELLO_WORLD123@GMAIL.COM


# Ingat: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.
s = "hello world!"
# string melakukan perubahan
print(s.upper())    # HELLO WORLD!
# string tidak melakukan perubahan
print(s)    # hello world!

# string tidak melakukan perubahan
x = "hello world!"
x.upper()
print(x)    # hello world!
