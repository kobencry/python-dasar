# -- Fungsi bawaan python --

# fungsi int() mengubah nilai yang ditentukan menjadi bilangan bulat/int

# Syntax:
# int(value, base)

# Nilai Parameter:
# Parameter                     Deskripsi
# value                         Dibutuhkan. Angka atau string yang dapat diubah menjadi bilangan bulat
# base                          opsional. Angka yang mewakili format angka. Nilai default: 10

print(int("11")) # default
# 11
print(int("11", base=2)) # biner
# 3
print(int("11", base=8)) # octal
# 9
print(int("11", base=10)) # default
# 11
print(int("11", base=16)) # hexa 
# 17
print(int(11 - 9))
# 2
print(int.from_bytes(b"\x0f", "little"))
# 15
print(int.from_bytes(b"\xc0\xff\xee", "big"))
# 12648430
