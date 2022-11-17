# -- Fungsi bawaan python --

# https://docs.python.org/3/library/stdtypes.html?highlight=class#str

# fungsi str() mengubah nilai yang ditentukan menjadi string.

# Syntax:
# str( object, encoding= encoding, errors= errors)

# Nilai Parameter:
# Parameter                 Deskripsi
# Objek                     Objek apa saja. Menentukan objek yang akan diubah menjadi string.
# encoding                  Pengkodean objek. Standarnya adalah UTF-8.
# errors                    Menentukan apa yang harus dilakukan jika decoding("menguraikan isi kode") gagal.

x = 2
y = 2.5
s1 = str(x)
s2 = str(y)
print(type(x))      # <class 'int'>
print(type(y))      # <class 'float'>
print(type(s1))     # <class 'str'>
print(type(s2))     # <class 'str'>
print(x + y)    # 4.5
print(s1 + s2)  # 22.5

x = str(b"\xc2\xbc sendok teh", encoding='utf-8')
print(x)    # ¼ sendok teh

x = "python 🐍"
y = str("python 🐍") # python 🐍
print(x)    # python 🐍
print(y)    # python 🐍

print(True + True)  # 2
print(str(True) + str(True))    # TrueTrue
