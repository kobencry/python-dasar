# Angka python
# ada tiga tipe numerik dalam python
# * int
# * float
# * complex

# variabel tipe numerik dibuat saat anda menetapkan nilai
x = 10    # int
y = 10.8  # float
z = 10j   # complex
print(type(x), x)   # <class 'int'> 10
print(type(y), y)   # <class 'float'> 10.8
print(type(z), z)   # <class 'complex'> 10j

# int, atau bilangan bulat, adalah bilangan bulat positif atau negatif, dengan panjang tak terhingga.
x = 9
y = 9999999999999999999
z = -999999999999999999
print(type(x), x)   # <class 'int'> 9
print(type(y), y)   # <class 'int'> 9999999999999999
print(type(z), z)   # <class 'int'> -999999999999999

# float, atau "angka titik mengambang" adalah bilangan positif atau negatif, 
# yang mengandung satu atau lebih desimal.
x = 9.0
y = 9.999999999999999999
z = -99.9999999999999999
# float juga bisa berupa angka ilmiah/scientific dengan "e" untuk menunjukkan kekuatan 10.
sx = 99e9
sy = 19E4
sz = -96.6e100
print(type(x), x)       # <class 'float'> 9.0
print(type(y), y)       # <class 'float'> 10.0
print(type(z), z)       # <class 'float'> -100.0
print(type(sx), sx)     # <class 'float'> 9900000000.0
print(type(sy), sy)     # <class 'float'> 190000.0
print(type(sz), sz)     # <class 'float'> -9.66e+101

# complex adalah bilangan yang ditulis dengan huruf "j" sebagai bagian imajiner
x = 9j
y = 9+9j
z = -9j
print(type(x), x)   # <class 'complex'> 9j
print(type(y), y)   # <class 'complex'> (9+9j)
print(type(z), z)   # <class 'complex'> (-0-9j)
