# -- python exception --

# https://docs.python.org/3/library/exceptions.html#AttributeError

# AttributeError adalah ketika sebuah objek tidak memiliki atribut yang diminta. 
# Ini terjadi ketika kita mencoba mengakses atribut yang tidak tersedia pada sebuah objek.

class Kelasku:
    pass

try:
    kls = Kelasku()
    print(kls.y)
except AttributeError as err:
    print("Nama Class Error:", err.__class__)
    print("Pesan Error:", err)
# Output:
# Nama Class Error: <class 'AttributeError'>
# Pesan Error: 'Kelasku' object has no attribute 'y'

# menggunakan pesan error sendiri
class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama

try:
    mhs = Mahasiswa('alice')
    print(mhs.nama)
    print(mhs.usia)
# menangkap jenis Error
except AttributeError:
    print("attribut tidak ada")
# Output:
# alice
# attribut tidak ada