# -- Fungsi bawaan python --

# https://docs.python.org/3/library/functions.html?#hex

# fungsi hex() mengubah angka yang ditentukan menjadi nilai heksadesimal.
# String yang dikembalikan selalu dimulai dengan awalan 0x.

# Syntax
# hex(angka)

# Nilai Parameter
# Parameter                 Deskripsi
# angka                     Bilangan bulat/angka

x = 255
print(hex(x))       # 0xff
print(hex(192))     # 0xc0

for i in range(10):
    print(hex(i))
# 0x0
# 0x1
# 0x2
# 0x3
# 0x4
# 0x5
# 0x6
# 0x7
# 0x8
# 0x9

# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan range() kunjungi folder_name: "Fungsi-Bawaan/fungsi_range.py"
