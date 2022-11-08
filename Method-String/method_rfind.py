# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=rfind#str.rfind

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi rfind() menemukan kemunculan terakhir dari nilai yang ditentukan.
# jika nilainya tidak ditemukan mengembalikan -1.
# fungsi rfind() hampir sama dengan fungsi rindex().

# Syntax
# string.rfind(value, start, end)

# Nilai Parameter
# Parameter             Deskripsi
# value                 Dibutuhkan. Nilai yang harus dicari
# start                 Opsional. Di mana untuk memulai pencarian. Standarnya/default adalah 0
# end                   Opsional. Di mana untuk mengakhiri pencarian. Standanya/default adalah ke akhir string.

text = "hello alice carl eliot"
x = text.rfind('alice')
y = text.rfind('carl')

print(x)    # 6
print(y)    # 12
print(text[x:]) # alice carl eliot
print(text[y:]) # carl eliot

text = "hello alice carl eliot alice world"
x = text.rfind('alice')
y = text.rfind('e')

print(x)    # 23
print(y)    # 27
print(text[x:]) # alice world
print(text[y:]) # e world

print("hello world".rfind('war'))   # -1
# jika ingin mempelajari lebih lanjut tentang string slice[:] kunjungi folder_name: "Bagian1-DASAR/stage09_slice_string.py"
