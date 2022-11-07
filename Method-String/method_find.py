# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=find#str.find

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi find() menemukan kemunculan pertama dari nilai yang ditentukan.
# jika nilai tidak ditemukan akan mengembalikan -1

# Syntax
# string.find(value, start, end)

# Nilai Parameter
# Parameter         Deskripsi
# value             Dibutuhkan. Nilai yang harus dicari
# start             opsional. Di mana untuk memulai pencarian. defaultnya adalah 0
# end               opsional. Di mana untuk mengakhiri pencarian. Defaultnya adalah ke akhir string

s = "alice bob carl bob"
hasil = s.find("bob")
# ingat index string dimulai dari 0
print(hasil)    # 6
print(s[6])     # b
print(s[6:])    # bob carl bob

s = "alice bob carl alice eliot"
print(s.find("alice", 2))   # 15
print(s.find("alice", 10))  # 15
print(s[s.find("alice", 2):])   # alice eliot

s = "python3.8|python3.9|python3.10"
print(s.find("python3"))    # 0
print(s.find("python2"))    # -1
