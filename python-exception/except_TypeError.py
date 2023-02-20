# -- python exception --

# https://docs.python.org/3/library/exceptions.html#TypeError

# TypeError adalah salah satu jenis exception (atau kesalahan) yang muncul ketika 
# operasi tidak dapat dilakukan atau tidak valid untuk jenis objek yang diberikan.
# Contoh umum dari TypeError adalah ketika kita mencoba menggabungkan objek dengan jenis yang tidak cocok, 
# seperti menggabungkan string dan angka.

try:
    hasil = 5 + "1"
except TypeError as err:
    print("Nama Class Error:", err.__class__)
    print("Pesan Error:", err)
# Output:
# Nama Class Error: <class 'TypeError'>
# Pesan Error: unsupported operand type(s) for +: 'int' and 'str

try:
    hasil = "1" + 5
except TypeError as err:
    print("Nama Class Error:", err.__class__)
    print("Pesan Error:", err)
# Output:
# Nama Class Error: <class 'TypeError'>
# Pesan Error: can only concatenate str (not "int") to str

# menggunakan pesan error sendiri
try:
    panjang = len(100)
# menangkap jenis Error
except TypeError as err:
    print("objek yang diberikan tidak valid")
# Output:
# objek yang diberikan tidak valid