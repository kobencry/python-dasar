# constructor __init__() dan parameter "self"
# __init__() adalah sebuah method constructor bawaan pada Python 
# yang secara otomatis dipanggil saat sebuah objek dibuat dari suatu class.
# Method ini digunakan untuk menginisialisasi data awal dari objek yang akan dibuat.
# Pada method ini biasanya didefinisikan argument/parameter yang akan diisi oleh nilai-nilai awal ketika objek dibuat.
# "yang ada garis bawa __ 2 kali (underscore underscore) disebut magic method."

# membuat class Mahasiswa
class Mahasiswa:
    # menginisialisasi
    def __init__(self): # pertama kali yang selalu dieksekusi
        print("__init__ dieksekusi duluan")

# membuat object 1
objek = Mahasiswa()
print(objek)
# Output:
# __init__ dieksekusi duluan
# <__main__.Mahasiswa object at 0x000002BD46448D00>

# membuat object 2
x = Mahasiswa()
print(x)
# __init__ dieksekusi duluan
# <__main__.Mahasiswa object at 0x000002B71EE08BE0>

# Metode __init__() umumnya digunakan untuk melakukan operasi yang diperlukan sebelum objek dibuat.
# Ketika Anda mendefinisikan method __init__() di dalam definisi class,
# parameter pertamanya harus selalu diisi dengan "self".

# Parameter "self" merujuk pada objek individu itu sendiri. 
# Ini digunakan untuk mengambil atau mengatur atribut dari instance tertentu.
# Parameter ini tidak harus disebut self, Anda bisa menamainya apa saja yang Anda inginkan,
# tetapi praktek yang umum dan sebaiknya Anda tetap memakainya. 
# Dalam method yang didefinisikan dalam sebuah class, self merujuk pada instance atau objek itu sendiri, 
# dan Anda harus memasukkannya sebagai parameter pertama pada setiap method.
# Dengan cara ini, Anda bisa mengakses atribut dan method dari instance di dalam method yang Anda buat.

# membuat class Mahasiswa
class Mahasiswa:
    # menginisialisasi
    def __init__(bebas):
        print("__init__ dieksekusi duluan")
# membuat object
y = Mahasiswa()
print(x)
# Output:
# __init__ dieksekusi duluan
# <__main__.Mahasiswa object at 0x0000019B506E8BE0>