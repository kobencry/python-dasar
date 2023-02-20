# -- python exception --

# https://docs.python.org/3/library/exceptions.html#KeyError

# KeyError adalah sebuah jenis exception atau pengecualian pada Python 
# yang terjadi ketika kita mencoba untuk mengakses sebuah kunci (key) pada sebuah dictionary
# yang tidak ada atau tidak valid.
# Misalnya, jika kita memiliki sebuah dictionary dengan kunci (key) 'foo',
# dan kita mencoba untuk mengakses nilai (value) yang terkait dengan kunci (key) 'bar',
# maka akan terjadi KeyError.

try:
    dictku = {'foo':10, 'baz':20}
    print(dictku['bar'])
except KeyError as err:
    print("Nama Class Error:", err.__class__)
    print("Pesan Error:", err)
# Output:
# Nama Class Error: <class 'KeyError'>
# Pesan Error: 'bar'

# menggunakan pesan error sendiri
try:
    dictku = {'foo':10, 'baz':20}
    print(dictku['bar'])
# menangkap jenis Error
except KeyError:
    print("key tidak ada")
# Output:
# key tidak ada