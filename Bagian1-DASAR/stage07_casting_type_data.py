# mungkin ada saatnya Anda ingin menentukan tipe pada variabel. 
# Ini bisa dilakukan dengan casting. 
# python adalah bahasa berorientasi objek, dan karena itu menggunakan kelas 
# untuk mendefinisikan tipe data, termasuk tipe primitifnya.
# casting tipe data python dilakukan dengan menggunakan fungsi konstruktor:

# int()
x = int(1.0)     # float
y = int("4")     # str
b1 = int(b'5')   # bytes
b2 = int(0b101)  # bytes
oc = int(0o101)  # octal
hx = int(0x101)  # hexa
t = int(True)    # boolean
f = int(False)   # boolean

print(type(x), x)   # 1
print(type(y), y)   # 4
print(type(b1), b1) # 5
print(type(b2), b2) # 5
print(type(oc), oc) # 65
print(type(hx), hx) # 257
print(type(t), t)   # 1
print(type(f), f)   # 0
# Jika anda ingin mengetahui tentang fungsi-bawaan type() kunjungi folder_name: "Fungsi-Bawaan/fungsi_type.py"


# float()
x = float(1)        # int
y = float("4")      # str
b1 = float(b'5')    # bytes
b2 = float(0b101)   # bytes
oc = float(0o101)   # octal
hx = float(0x101)   # hexa
t = float(True)     # boolean
f = float(False)    # boolean
# Jika anda ingin mengetahui tentang fungsi-bawaan float() kunjungi folder_name: "Fungsi-Bawaan/fungsi_float.py"

print(type(x), x)   # 1.0
print(type(y), y)   # 4.0
print(type(b1), b1) # 5.0
print(type(b2), b2) # 5.0
print(type(oc), oc) # 65.0
print(type(hx), hx) # 257.0
print(type(t), t)   # 1.0
print(type(f), f)   # 0.0

# str()
x = str(1)
y = str(4.0)
b1 = str(b'5')
b2 = str(0b101)
oc = str(0o101)
hx = str(0x101)
t = str(True)
f = str(False)
# Jika anda ingin mengetahui tentang fungsi-bawaan str() kunjungi folder_name: "Fungsi-Bawaan/fungsi_str.py"

print(type(x), x)   # 1
print(type(y), y)   # 4.0
print(type(b1), b1) # b'5'
print(type(b2), b2) # 5
print(type(oc), oc) # 65
print(type(hx), hx) # 257
print(type(t), t)   # True
print(type(f), f)   # False

# Catatan: 
# Anda tidak dapat mengonversi bilangan kompleks menjadi jenis bilangan lain.


# Jika anda ingin mengetahui tentang fungsi-bawaan int() kunjungi folder_name: "Fungsi-Bawaan/fungsi_int.py"
print(int('1010', 2))  # 10     biner
print(int('1010', 8))  # 520    octal
print(int('1010', 10)) # 1010   default
print(int('1010', 16)) # 4112   hexa
