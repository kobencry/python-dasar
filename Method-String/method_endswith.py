# -- Method String --

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi endswith() mengembalikan nilai boolean True jika string diakhiri dengan
# nilai yang ditentukan, jika tidak ada akan mengembalikan nilai boolean False.

# Syntax
# string.endswith(value, start, end)

# Nilai Parameter
# paramter          Deskripsi
# value             Dibutuhkan. Nilai untuk memeriksa apakah string diakhiri dengan karakter tertentu.
# start             opsional. Nilai integer yang menentukan di posisi mana untuk memulai pencarian.
# end               opsional. Nilai integer yang menentukan di posisi mana untuk mengakhiri pencarian.

nama = "alice, bob, carl, eliot"
x = nama.endswith('eliot')
print(x)    # True

s = "hello world!"
x = s.endswith("world!")
y = s.endswith("!")
print(x)    # True
print(y)    # True

print("hello world.".endswith(".")) # True
