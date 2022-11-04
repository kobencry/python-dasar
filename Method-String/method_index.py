# -- Method String --

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi index() menemukan kemunculan pertama dari nilai yang ditentukan.
# menimbulkan pengecualian jika nilai tidak ditemukan.
# hampir sama dengan fungsi find() , satu-satunya perbedaan adalah 
# fungsi find() mengembalikan -1 jika nilainya tidak ditemukan.

# Syntax
# string.index(value, start, end)

# Nilai Parameter
# Parameter         Deskripsi
# value             Dibutuhkan. nilai yang harus dicari
# start             opsional. Di mana untuk memulai pencarian. Standarnya adalah 0
# end               opsional. Di mana untuk mengakhiri pencarian. Standarnya adalah ke akhir string

s = "hello alice"
i = s.index("e")
f = s.index("e")
# ingat indeks string dimulai dari 0
print(i)    # 1
print(f)    # 1

i = s.index("e", 2)
f = s.index("e", 2)
print(i)    # 10
print(f)    # 10

print("hello world".find("l",4))    # 9
print("hello world".index("l", 4))  # 9

s = "alice carl eliot"
f = s.find("xxx")
print(f)    # mengembalikan -1
i = s.index("xxx")
print(i)    # mengembalikan kesalahan ValueError:
