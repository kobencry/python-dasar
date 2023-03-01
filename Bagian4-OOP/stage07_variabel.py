# Dalam OOP Python, variabel public, private, dan protected adalah 
# konsep aksesibilitas pada atribut class.

# Variabel public dapat diakses dan dimodifikasi dari mana saja, baik dari dalam maupun luar class,
# dengan cara memanggil nama atribut dari objek atau class tersebut.
class Mahasiswa:
    # variabel class
    # membuat variabel public
    x = "ini adalah variabel publik x"

    # menginisialisasi
    def __init__(self):
        # variabel instance
        # membuat variabel public
        self.y = "ini adalah variabel publik y"

# membuat object
mhs = Mahasiswa()
#print(Mahasiswa.x)

# untuk mengakses variabel class, Anda bisa juga menggunakan object ("mhs") dari kelas Mahasiswa
# Catatan: ini hanya berlaku untuk variabel public dan protected
print(mhs.x)    # mengakses variabel class
print(mhs.y)    # mengakses variabel instance
# Output:
# ini adalah variabel publik x
# ini adalah variabel publik y

# Variabel protected dimulai dengan satu garis bawah ( _ ) 
# dan dapat diakses dan dimodifikasi dari dalam class yang sama dan juga subclass 
# yang diwarisi dari class tersebut. 
# Namun, pada praktiknya variabel protected ini dapat diakses dan dimodifikasi dari luar class,
class Mahasiswa:
    # variabel class
    # membuat variabel protected
    _x = "ini adalah variabel protected x"

    # menginisialisasi
    def __init__(self):
        # variabel instance
        # membuat variabel protected
        self._y = "ini adalah variabel protected y"

# membuat object
mhs = Mahasiswa()
#print(Mahasiswa._x)
# untuk mengakses variabel class, Anda bisa juga menggunakan object ("mhs") dari kelas Mahasiswa
# Catatan: ini hanya berlaku untuk variabel public dan protected
print(mhs._x)   # mengakses variabel class
print(mhs._y)   # mengakses variabel instance
# Output:
# ini adalah variabel protected x
# ini adalah variabel protected y

# Variabel private dimulai dengan dua garis bawah ( __ ) 
# dan hanya dapat diakses dan dimodifikasi dari dalam class yang sama
# sehingga tidak bisa diakses dari luar class. 
# Namun, variabel private ini sebenarnya dapat diakses dan dimodifikasi 
# melalui metode public yang ada di dalam class tersebut.
class Mahasiswa:
    # variabel class
    # membuat variabel pritvate
    __x = "ini adalah variabel private x"

    # menginisialisasi
    def __init__(self):
        # variabel instance
        # membuat variabel private
        self.__y = "ini adalah variabel private y"

# membuat object
mhs = Mahasiswa()
# kode dibawah ini (yang dikomentarin #) akan memunculkan pesan error
# memaksa mengakses variabel private "__x" dan "__y"
# print(Mahasiswa.__x)
# print(mhs.__y)

# untuk mengakses variabel private, gunakan magic method __dict__ atau method didalam class.
print(mhs.__dict__)
print(Mahasiswa.__dict__)
# Output:
# {'_Mahasiswa__y': 'ini adalah variabel private y'}
# {'__module__': '__main__', '_Mahasiswa__x': 'ini adalah variabel private x', '__init__': <function Mahasiswa.__init__ at 0x000001E11D8EA700>, '__dict__': <attribute '__dict__' of 'Mahasiswa' objects>, '__weakref__': <attribute '__weakref__' of 'Mahasiswa' objects>, '__doc__': None}

# sehingga sebaiknya variabel ini tetap diperlakukan seperti variabel public.
# Namun, di Python sebenarnya tidak ada konsep aksesibilitas yang benar-benar private, 
# sehingga variabel private dan protected pada dasarnya dapat diakses dari luar class. 
# Penggunaan nama awalan garis bawah pada variabel ini sebenarnya hanya bersifat konvensi 
# atau aturan kesepakatan dalam komunitas Python.