# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=isidentifier#str.isidentifier

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi isidentifier() mengembalikan True jika string adalah pengidentifikasi yang valid.
# jika tidak, maka akan mengemblaikan nilai boolean False.

# Sebuah string dianggap sebagai pengenal yang valid jika hanya berisi huruf 
# alfanumerik (a-zA-Z) dan (0-9), atau garis bawah (_). 
# Pengidentifikasi yang valid tidak boleh dimulai dengan angka, atau berisi spasi apa pun.

# Syntax
# string.isidentifier()

# Nilai Parameter
# tidak ada nilai parameter

x = "HelloWorld"
y = "Hello002"
print(x.isidentifier()) # True
print(x.isidentifier()) # True

x = "5hello"
y = "hello world"
print(x.isidentifier()) # False
print(y.isidentifier()) # False
