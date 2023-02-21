# -- python exception --

# https://docs.python.org/3/library/exceptions.html#ImportError

# ImportError adalah sebuah exception dalam Python yang dihasilkan ketika sebuah modul 
# yang diimpor tidak ditemukan atau tidak dapat diimpor karena suatu alasan. 
# Ini dapat terjadi jika nama modul yang diimpor tidak benar, modul tidak ditemukan di sistem, 
# atau ada kesalahan dalam modul yang menghalangi import berhasil.

try:
    # mengimpor attribut hello_world yang tidak ada di modul bawaan python sys
    from sys import hello_world
except ImportError as err:
    print("Nama Class Error:", err.__class__)
    print("Pesan Error:", err)
# Output:
# Nama Class Error: <class 'ImportError'>
# Pesan Error: cannot import name 'hello_world' from 'sys' (unknown location)

# menggunakan pesan error sendiri
try:
    from sys import hello_world
# menangkap jenis Error
except ImportError:
    print("nama attribut tidak ada")
# Output:
# nama attribut tidak ada