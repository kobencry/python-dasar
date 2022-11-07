# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=isspace#str.isspace

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli. 

# fungsi isspace() mengembalikan nilai boolean True jika semua karakter dalam string adalah spasi putih.
# jika tidak, maka akan mengembalikan nilai boolean False.

# Syntax
# string.isspace()

# Nilai Parameter
# tidak ada nilai parameter

x = " "
y = "\n"
print(x.isspace())  # True
print(y.isspace())  # True

print("\t".isspace())   # True
print("\f".isspace())   # True
print("\r".isspace())   # True

x = " hello world "
y = "  \b"
z = "   s   "
print(x.isspace())  # False
print(y.isspace())  # False
print(z.isspace())  # False
