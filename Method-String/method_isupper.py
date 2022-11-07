# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=isupper#str.isupper

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi isupper() mengembalikan nilai boolean True jika semua karakter dalam huruf besar.
# jika tidak, maka akan mengembalikan nilai boolean False.
# Angka, simbol, dan spasi tidak diperiksa atau diabaikan, hanya karakter alfabet(a-zA-Z).

# Syntax
# string.isupper()

# Nilai Parameter
# tidak ada nilai parameter

x = "HELLO WORLD"
y = "#HELLO@123WORLD"
print(x.isupper())  # True
print(y.isupper())  # True

print("HELLO @ALICE, @CARL, @ELIOT".isupper())  # True
print("!A@B#C$D%E^F&G*H(I)J-K+L_M=".isupper())  # True

x = "Hello World"
y = "Hello123WorlD"
print(x.isupper())  # False
print(y.isupper())  # False

print("HELLO @Alice, @Carl, @Eliot".isupper())  # False
print("!A@B#C$D%E^F&G*H(I)J-K+L_m=".isupper())  # False

# Periksa apakah karakter memiliki huruf besar semua?
if "PYTHON3.8|PYTHON3.9|PYTHON3.10".isupper():
    print("passed")
else:
    print("failed")
