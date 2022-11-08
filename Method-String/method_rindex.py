# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=rindex#str.rindex

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi rindex() menemukan kemunculan terakhir dari nilai yang ditentukan.
# jika nilainya tidak ditemukan, maka akan menampilkan kesalahan runtime ValueError.
# fungsi rindex() hampir sama dengan fungsi rfind().

# Syntax
# string.rindex(value, start, end)

# Nilai Parameter
# Parameter             Deskripsi
# value                 Dibutuhkan. Nilai yang harus dicari
# start                 Opsional. Di mana untuk memulai pencarian. Standarnya/default adalah 0.
# end                   Opsional. Di mana untuk mengakhiri pencarian. Standarnya/default adalah ke akhir string.

text = "hello alice carl eliot"
x = text.rindex('alice')
y = text.rindex('carl')

print(x)    # 6
print(y)    # 12
print(text[x:]) # alice carl eliot
print(text[y:]) # carl eliot

text = "hello alice carl eliot alice world"
x = text.rindex('alice')
y = text.rindex('e')
z = text.rindex('e', 14, 20)

print(x)    # 23 
print(y)    # 27
print(z)    # 17
print(text[x:]) # alice world
print(text[y:]) # e world
print(text[z:]) # eliot alice world

print("hello world".rindex('war')) # kesalahan runtime ValueError: substring not found
# jika ingin mempelajari lebih lanjut tentang string slice[start:end] kunjungi folder_name: "Bagian1-DASAR/stage09_slice_string.py"
