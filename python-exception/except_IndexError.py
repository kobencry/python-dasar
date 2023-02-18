# -- python exception --

# https://docs.python.org/3/library/exceptions.html#IndexError

# IndexError adalah sebuah exception yang terjadi saat mencoba mengakses sebuah index 
# pada sebuah objek seperti list atau tuple yang tidak valid atau diluar range yang ada.
#  Contohnya, mencoba mengakses indeks ke-4 pada list yang hanya memiliki 3 elemen akan menghasilkan IndexError.

try:
    x = ['alice', 'carl', 'eliot']
    print(x[4])
except IndexError as err:
    print("Nama Class Error:", err.__class__)
    print("Pesan Error:", err)
# Output:
# Nama Class Error: <class 'IndexError'>
# Pesan Error: list index out of range

# menggunakan pesan error sendiri
try:
    listku = ['alice', 'carl', 'eliot']
    print(listku[3])
# menangkap jenis Error
except IndexError:
    print("index list tidak ada")
# Output:
# index list tidak ada