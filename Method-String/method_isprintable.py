# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=isprintable#str.isprintable

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli. 

# fungsi isprintable() mengembalikan nilai boolean True jika semua karakter dapat dicetak.
# jika tidak, maka akan mengembalikan nilai boolean False.
# Contoh karakter yang tidak dapat dicetak dapat berupa karakter escape/pelarian
# \r(carriage return), \n(newline), \t(tab), \b(backspace), \f(form feed)

# Syntax
# string.printable()

# Nilai Parameter
# tidak ada nilai parameter

x = "hello world"
y = "#hello123world_@gmail.com"
print(x.isprintable())  # True
print(y.isprintable())  # True

x = "hello\nworld"
y = "hello\tworld"
print(x.isprintable())  # False
print(y.isprintable())  # False

print("hello\rworld".isprintable()) # False
print("hello\fworld".isprintable()) # False
print("hello\bworld".isprintable()) # False

# periksa apakah ada kerakter pelarian/escape?
if "\u0030".isprintable():
    print("passed")
else:
    print("failed")
