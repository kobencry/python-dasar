# -- Fungsi bawaan python --

# https://docs.python.org/3/library/stdtypes.html?#chr

# fungsi chr() mengembalikan karakter yang mewakili unicode yang ditentukan.

# Syntax
# chr(angka)

# Nilai Parameter
# Parameter                 Deskripsi
# angka                     Bilangan bulat yang mewakili titik kode Unicode yang valid.


# contoh menggunakan tabel ascii
x = chr(97)
print(x)    # a

kode_ascii = [104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]
for i in kode_ascii:
    print(chr(i), end="")   # hello world
print()


# contoh menggunakan hexa
# print(hex(104))   # 0x68
kode_hexa = [0x68, 0x65, 0x6c, 0x6c, 0x6f, 0x20, 0x77, 0x6f, 0x72, 0x6c, 0x64]
for i in kode_hexa:
    print(chr(i), end="")   # hello world
print()


# contoh menggunakan biner
# print(bin(104))     # 0b1101000
# print(f"{104:08b} atau {104:0b}")   # 01101000 atau 1101000
kode_biner = [0b01101000, 0b01100101, 0b01101100, 0b01101100, 0b01101111, 0b00100000, 0b01110111, 0b01101111, 0b01110010, 0b01101100, 0b01100100]
for i in kode_biner:
    print(chr(i), end="")   # hello world
print()

#for i in range(10000):
#    print(chr(i))

# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan range() kunjungi folder_name: "Fungsi-Bawaan/fungsi_range.py"
# jika ingin mempelajari lebih lanjut tentang python-encoding karakter unicode kunjungi folder_name: "python-encoding"
# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan bin() kunjungi folder_name: "Fungsi-Bawaan/fungsi_bin.py"
# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan hex() kunjungi folder_name: "Fungsi-Bawaan/fungsi_hex.py"
# jika ingin mempelajari lebih lanjut tentang formatting-string f-string kunjungi folder_name: "python-formatting"
