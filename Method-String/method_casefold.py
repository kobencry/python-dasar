# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=casefold#str.casefold

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi casefold() mengembalikan string di mana semua karakter adalah huruf kecil.

# Syntax
# string.casefold()

# Nilai Parameter
# tidak ada nilai parameter

print("Hello WoRLd".casefold())     # hello world

x = "Hello WoRLd".casefold()
print(x)    # hello world

y = "100 Hello WoRLd".casefold()
print(y)    # 100 hello world


# Ingat: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.
s = "Hello WoRLd"
# string melakukan perubahan
print(s.casefold())     # hello world
# string tidak melakukan perubahan
print(s)    # Hello WoRLd

# string tidak melakukan perubahan
s = "Hello WoRLd"
s.casefold()
print(s)    # Hello WoRLd
