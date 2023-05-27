# operator bitwise hampir sama seperti Operator Logika, akan tetapi operator ini 
# melakukan operasi berdasarkan bilangan bit/biner.
# Bilangan biner sendiri merupakan jenis bilangan yang hanya terdiri dari dua
# jenis angka, yakni 0 dan 1. Jika nilai asal yang dipakai bukan bilangan biner,
# akan dikonversi secara otomatis oleh Python menjadi bilangan biner.
# Misalnya, angka 2 dalam bit ditulis 10 dalam notasi biner dan angka 7 ditulis 111.

# 128 64 32 16 8 4 2 1
#  0   0  0  0 0 0 1 0 = 10  = 2

# 128 64 32 16 8 4 2 1
#  0   0  0  0 0 1 1 1 = 111 = 1 + 2 + 4 = 7

#------------------------------------------------------
#  Nama         Simbol      Deskripsi
#------------------------------------------------------
#  AND            &         Mengembalikan bit 1 jika dua bit bernilai 1.
#  OR             |         Mengembalikan bit 1 jika salah satu bit bernilai 1.
#  XOR            ^         Mengembalikan bit 1 jika hanya satu bit saja yang bernilai 1.
#  NOT            ~         Membalikkan semua bit.
# Left Shift      <<        Menggeser bit ke kiri dengan mendorong digit 0 dan membiarkan bit paling kiri terlepas.
# Right Shift     >>        Menggeser bit ke kanan dengan mendorong salinan digit sebelah kiri dan membiarkan digit sebelah kanan terlepas.

# contoh menampilkan biner menggunakan formatting f-string
print(f"{0:08b}")   # 00000000
print(f"{1:08b}")   # 00000001
print(f"{2:08b}")   # 00000010
print(f"{7:08b}")   # 00000111

# menggunakan operator AND &
x = 5
y = 7
z = x & y
print(f"x = {x:08b}")   # x = 00000101
print(f"y = {y:08b}")   # y = 00000111
print('-'*12, 'AND')    # ------------ AND
print(f"z = {z:08b}")   # z = 00000101  
print(x & y)            # 5             
# 128 64 32 16 8 4 2 1
#  0  0  0  0  0 1 0 1 = 1 + 4 = 5 

#-------------------------------------------------------------------------------
# menggunakan operator OR |
x = 5
y = 7
z = x | y
print(f"x = {x:08b}")   # x = 00000101
print(f"y = {y:08b}")   # y = 00000111
print('-'*12, 'OR')     # ------------ OR
print(f"z = {z:08b}")   # z = 00000111
print(x | y)            # 7
# 128 64 32 16 8 4 2 1
#  0  0  0  0  0 1 1 1 = 1 + 2 + 4 = 7

#-------------------------------------------------------------------------------
# menggunakan operator XOR ^
x = 5
y = 7
z = x ^ y
print(f"x = {x:08b}")   # x = 00000101
print(f"y = {y:08b}")   # y = 00000111
print('-'*12, 'XOR')    # ------------ XOR
print(f"z = {z:08b}")   # z = 00000010
print(x ^ y)            # 2
# 128 64 32 16 8 4 2 1
#  0  0  0  0  0 0 1 0 = 2

#-------------------------------------------------------------------------------
# menggunakan operator NOT ~
x = 5
y = 7
print(f"x = {x:08b}")    # x = 00000101
print('-'*12, 'NOT')     # ------------ NOT
print(f"x = {~x:08b}")   # x = -0000110

print(f"y = {y:08b}")    # y = 00000111
print('-'*12, 'NOT')     # ------------ NOT
print(f"y = {~y:08b}")   # y = -0001000
print('x = ', int('-0000110', base=2))   # x = -6
print('y = ', int('-0001000', base=2))   # y = -8

#-------------------------------------------------------------------------------
# menggunakan operator  Left Shift <<
x = 1   # x adalah berapa banyak jumlah bit yang ingin digeser ke kiri
y = 7   # y adalah bit yang digeser 
z = y << x
print(f"geser {x} kali ke kiri") # geser 1 kali ke kiri
print(f"y = {y:08b}")            # y = 00000111
print('-'*12, 'Left Shift')      # ------------ Left Shift
print(f"z = {z:08b}")            # z = 00001110
print(y << x)                    # 14
# 128 64 32 16 8 4 2 1
#  0  0  0  0  1 1 1 0 = 2 + 4 + 8 = 14
print()

x = 2   # x adalah berapa banyak jumlah bit yang ingin digeser ke kiri
y = 7   # y adalah bit yang digeser 
z = y << x
print(f"geser {x} kali ke kiri") # geser 2 kali ke kiri 
print(f"y = {y:08b}")            # y = 00000111
print('-'*12, 'Left Shift')      # ------------ Left Shift
print(f"z = {z:08b}")            # z = 00011100
print(y << x)                    # 28
# 128 64 32 16 8 4 2 1
#  0  0  0  1  1 1 0 0 =  4 + 8 + 16 = 28

#-------------------------------------------------------------------------------
# menggunakan Right Shift >>
x = 1   # x adalah berapa banyak jumlah bit yang ingin digeser ke kanan
y = 7   # y adalah bit yang digeser 
z = y >> x
print(f"geser {x} kali ke kanan") # geser 1 kali ke kanan
print(f"y = {y:08b}")             # y = 00000111
print('-'*12, 'Right Shift')      # ------------ Right Shift
print(f"z = {z:08b}")             # z = 00000011
print(y >> x)                     # 3
# 128 64 32 16 8 4 2 1
#  0  0  0  0  0 0 1 1 = 1 + 2 = 3
print()

x = 2   # x adalah berapa banyak jumlah bit yang ingin digeser ke kanan
y = 7   # y adalah bit yang digeser 
z = y >> x
print(f"geser {x} kali ke kanan") # geser 2 kali ke kanan
print(f"y = {y:08b}")             # y = 00000111
print('-'*12, 'Right Shift')      # ------------ Right Shift
print(f"z = {z:08b}")             # z = 00000001
print(y >> x)                     # 1
# 128 64 32 16 8 4 2 1
#  0  0  0  0  0 0 0 1 = 1 

# jika ingin mempelajari lebih lanjut tentang python-formatting f-string kunjungi folder_name: "python-formatting/formatting_fstring.py"
