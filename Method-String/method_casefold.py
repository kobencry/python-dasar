# -- Method String --

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi casefold() mengembalikan string di mana semua karakter adalah huruf kecil.

# Syntax
# string.casefold()

# Nilai Parameter
# tidak ada nilai parameter

# contoh yang benar
print("Hello WoRLd".casefold())

x = "Hello WoRLd".casefold()
print(x)

y = "100 Hello WoRLd".casefold()
print(y)


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
