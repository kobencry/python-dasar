# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=swapcase#str.swapcase

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi swapcase() mengembalikan string di mana semua huruf besar menjadi huruf kecil dan sebaliknya.

# Syntax
# string.swapcase()

# Nilai Parameter
# tidak ada nilai parameter

x = "Hello World"
y = "HELLO WoRlD!"
print(x.swapcase())
print(y.swapcase())

print("Alice#Carl#ELIOT".swapcase())    # aLICE#cARL#eliot
