# operator identitas adalah untuk mengetahui apakah dua buah variabel merupakan
# objek yang sama atau memiliki nilai yang sama atau tidak. 
# Jika sama akan menghasilkan nilai TRUE dan sebaliknya, 
# jika salah akan menghasilkan nilai FALSE.


#-------------------------------------------
#  Simbol           Deskripsi
#-------------------------------------------
#   is          Menghasilkan nilai TRUE jika kedua nilai operand memiliki identitas yang sama.
#  is not       Menghasilkan nilai FALSE jika kedua nilai operand memiliki identitas yang sama.

x = ['alice']
y = x
print(x is y)   # True
print(x is not y) # False

x = 5
y = 5
print(x is y)   # True

x = ['alice']
y = ['carl']
print(x is y)   # False
print(type(x) is type(y))   # True

print(x is not y)   # True
print(type(x) is not type(y)) # False

# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan type() kunjungi folder_name: "Fungsi-Bawaan/fungsi_type.py"
