# -- Fungsi Bawaan --

# https://docs.python.org/3/library/functions.html#func-memoryview

# fungsi memoryview() mengembalikan objek tampilan memori dari objek tertentu.

# Syntax
# memoryview(object)

# Nilai Parameter
# Parameter                 Deskripsi
# object                    Objek Bytes atau objek Bytearray.

x = memoryview(b"hello world")

print(x)
# Output:
# <memory at 0x0000026508A00700>

# mengembalikan karakter unicode 
print(x[0]) 
# Output:
# 104

print(chr(x[0]))
# Output:
# h

for i in x:
    print(chr(i), end='')
# Output:
# hello world