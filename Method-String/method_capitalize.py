# -- Method String --

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi capitalize()
# mengembalikan string di mana karakter pertama adalah huruf besar.

# Syntax
# string.capitalize()

# Nilai Parameter
# Tidak ada nilai parameter

print("hello world".capitalize())   # Hello world

x = "hello world".capitalize()
print(x)  # Hello world

y = "100 hello world".capitalize()
print(y) # 100 hello world


# Ingat: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.
s = "hello world"
print(s.capitalize())   # Hello world
# string tidak melakukan perubahan
print(s)                # hello world

# string tidak melakukan perubahan
s = "hello world"
s.capitalize()
print(s)    # hello world
