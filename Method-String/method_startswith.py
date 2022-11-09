# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=startswith#str.startswith

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.
# fungsi startwith() mengembalikan nilai boolean True jika string dimulai dengan nilai yang ditentukan,
# jika tidak, maka akan mengembalikan nilai boolean False.

# Syntax
# string.startswith(value, start, end)

# Nilai Parameter
# Parameter             Deskripsi
# value                 Dibutuhkan. Nilai untuk memeriksa apakah string dimulai dengan
# start                 Opsional. Integer menentukan di mana posisi untuk memulai pencarian
# end                   Opsional. Integer yang menentukan di posisi mana untuk mengakhiri pencarian

x = "hello world"
print(x.startswith('hello'))    # True
print(x.startswith('world', 6)) # True

x = "hello alice carl eliot world"
print(x.startswith('hello', 6))     # False
print(x.startswith('world', -5))    # True
print(x.startswith('alice', 6, 20)) # True

# jika ingin mempelajari lebih lanjut tentang string slice[start:end] kunjungi folder_name: "Bagian1-DASAR/stage09_slice_string.py"
