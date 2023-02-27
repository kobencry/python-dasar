# -- python exception --

# https://docs.python.org/3/library/exceptions.html#ValueError

# ValueError merupakan salah satu jenis exception/error pada Python yang terjadi 
# ketika suatu fungsi atau operasi menerima argumen dengan tipe data yang benar, 
# tetapi nilainya tidak valid atau tidak dapat diinterpretasikan. 
# Contohnya, jika sebuah fungsi mengharapkan sebuah bilangan bulat (integer), 
# tetapi menerima sebuah string sebagai argumen.

try:
    angka = int("hello world")
except ValueError as err:
    print("Nama Class Error:", err.__class__)
    print("Pesan Error:", err)
# Output:
# Nama Class Error: <class 'ValueError'>
# Pesan Error: invalid literal for int() with base 10: 'hello world'

# menggunakan pesan error sendiri
try:
    angka = int("hello world")
# menangkap jenis Error
except ValueError:
    print("bukan bilangan bulat (integer)")
# Output:
# bukan bilangan bulat (integer)