# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=islower#str.islower

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi islower() mengembalikan nilai boolean True jika semua karakter dalam huruf kecil,
# jika tidak, maka akan mengembalikan nilai boolean False. 
# Angka, simbol, dan spasi di abaikan, hanya karakter alfabet (a-zA-Z).

# Syntax
# string.islower()

# Nilai Parameter
# tidak ada nilai parameter

x = "hello 123 world"
y = "hello_world@gmil.com"
print(x.islower())  # True
print(y.islower())  # True
print("#!/usr/bin/python".islower()) # True

x = "Hello 123 World"
y = "hello_World@gmail.com"
print(x.islower())  # False
print(y.islower())  # False
print("#!/usr/bin/Python".islower()) # False

# periksa apakah karakter huruf kecil semua?
if "python3.8|3.9|3.10".islower():
    print("passed")
else:
    print("failed")
