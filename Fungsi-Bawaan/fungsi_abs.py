# -- Fungsi bawaan python --

# https://docs.python.org/3/library/functions.html?highlight=built-function-abs#abs

# fungsi abs() mengembalikan nilai absolut dari angka yang ditentukan.

# pengertian nilai absolut
# Dalam matematika, nilai absolut dari suatu bilangan real x, 
# ditulis sebagai |x|, adalah nilai dari x tanpa disertai oleh tanda.
# Dengan kata lain, |x| = x jika x adalah bilangan positif dan |x| = −x jika x adalah bilangan negatif.
# Sebagai contoh, nilai mutlak dari 3 adalah 3, dan nilai mutlak dari –3 juga 3.

# Syntax
# abs(n)

# Nilai Parameter
# Parameter             Deskripsi
# n                     Dibutuhkan. sebuah angka

x = abs(-3.25)  # float minus
print(x)
# Output:
# 3.25

x = abs(3+5j)   # imajiner
print(x)    # 5.830951894845301

x = abs(-3+5j)  # imajiner minus
print(x)    
# Output:
# 5.830951894845301

x = abs(0xff)   # hexadecimal
print(x)        
# Output:
# 255

x = abs(0b11111111) # biner
print(x)        
# Output:
# 255

x = abs(0o400)  # octal
print(x)        
# Output:
# 256
