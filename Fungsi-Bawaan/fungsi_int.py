# -- Fungsi bawaan python --

# fungsi int() mengubah nilai yang ditentukan menjadi bilangan bulat/int

# Syntax:
# int(value, base)

# Nilai Parameter:
# Parameter                     Deskripsi
# value                         Dibutuhkan. Angka atau string yang dapat diubah menjadi bilangan bulat
# base                          opsional. Angka yang mewakili format angka. Nilai default: 10

print(int("11")) # default

print(int("11", base=2)) # biner

print(int("11", base=8)) # octal

print(int("11", base=10)) # default

print(int("11", base=16)) # hexa 

print(int(11 - 9))

print(int.from_bytes(b"\x0f", "little"))
print(int.from_bytes(b"\xc0\xff\xee", "big"))
