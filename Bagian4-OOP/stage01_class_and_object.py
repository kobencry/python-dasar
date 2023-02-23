# class dan object Python adalah konsep dasar pemrograman berorientasi objek di Python.

# Class adalah blueprint/cetak biru atau templat yang mendefinisikan data dan metode yang akan dimiliki objek kelas itu. 
# Ini adalah tipe data yang ditentukan pengguna yang merangkum data dan fungsi untuk beroperasi pada data tersebut.
# membuat class
class Mahasiswa:
    pass
print(Mahasiswa)
# Output:
# <class '__main__.Mahasiswa'>
# Di sini pernyataan 'pass' digunakan untuk menunjukkan bahwa class ini kosong.

# Object adalah turunan dari class, yang berarti bahwa itu adalah representasi konkret dari class,
# dengan kumpulan data dan metodenya sendiri yang beroperasi pada data tersebut.
# Object dibuat dari blueprint/cetak biru atau template yang disediakan oleh class, 
# dan dapat dimanipulasi dan berinteraksi untuk melakukan tugas tertentu.
# membuat object
objek = Mahasiswa()
print(objek)
# Output:
# <__main__.Mahasiswa object at 0x000001DEA2538D00>

# membuat class Mahasiswa
class Mahasiswa:
    print("hello world")

# membuat object
objek = Mahasiswa()
print(objek)
# Output:
# hello world







# Dalam Python, class didefinisikan menggunakan kata kunci class,
# dan objek dibuat menggunakan metode konstruktor __init__() yang dipanggil saat objek dibuat.
# Setelah objek dibuat, atribut dan metodenya dapat diakses menggunakan notasi titik.

# constructor __init__() dan parameter "self"
# __init__() adalah sebuah method constructor bawaan pada Python 
# yang secara otomatis dipanggil saat sebuah objek dibuat dari suatu class.
# Method ini digunakan untuk menginisialisasi data awal dari objek yang akan dibuat.
# Pada method ini biasanya didefinisikan argument/parameter yang akan diisi 
# oleh nilai-nilai awal ketika objek dibuat.

# membuat class Mahasiswa
class Mahasiswa:
    # menginisialisasi
    def __init__(self):
        pass

# Metode __init__() umumnya digunakan untuk melakukan operasi yang diperlukan sebelum objek dibuat.
# Ketika Anda mendefinisikan method __init__() di dalam definisi class,
# parameter pertamanya harus selalu diisi dengan "self".

# Parameter self merujuk pada objek individu itu sendiri. 
# Ini digunakan untuk mengambil atau mengatur atribut dari instance tertentu.
# Parameter ini tidak harus disebut self, Anda bisa menamainya apa saja yang Anda inginkan,
# tetapi praktek yang umum dan sebaiknya Anda tetap memakainya. 
# Dalam method yang didefinisikan dalam sebuah class, self merujuk pada instance atau objek itu sendiri, 
# dan Anda harus memasukkannya sebagai parameter pertama pada setiap method.
# Dengan cara ini, Anda bisa mengakses atribut dan method dari instance di dalam method yang Anda buat.

# attribute dan method
# Setiap class yang Anda tulis dengan Python memiliki dua fitur dasar: attribute dan method.

# Attribute adalah hal-hal individual yang membedakan satu objek dari yang lain. 
# Mereka menentukan penampilan, keadaan, atau kualitas lain dari object itu.

# Dalam kasus kami, class 'Mahasiswa' mungkin memiliki attribute berikut:
# nama: alice, carl, eliot
# usia: 23, 20, 25
# alamat: jakarta, bandung, surabaya

# Atribut didefinisikan dalam kelas oleh variabel, 
# dan setiap objek dapat memiliki nilainya sendiri untuk variabel tersebut.
# Ada dua jenis atribut: Instance Attribute dan Class Attribute.

# Instance Attribute
# Atribut instance adalah variabel yang unik untuk setiap objek (instance).
# Setiap objek dari class itu memiliki salinannya sendiri dari variabel itu.
# Setiap perubahan yang dilakukan pada variabel tidak mencerminkan objek lain dari class itu.
# Dalam kasus ini class Mahasiswa(), setiap mahasiswa memiliki nama, usia dan alamat tertentu.

# membuat class Mahasiswa
class Mahasiswa:
    # menginisialisasi menggunakan constructor __init__()
    # dengan Instance Attribute
    def __init__(self, nama, usia, alamat):
        self.var_nama = nama
        self.var_usia = usia
        self.var_alamat = alamat

# Class Attribute
# Class attribute adalah variabel yang dimiliki oleh kelas itu sendiri,
# bukan oleh setiap objek yang dihasilkan dari kelas tersebut.
# Variabel ini dapat diakses oleh semua objek yang dihasilkan dari kelas tersebut,
# dan jika nilai dari variabel tersebut diubah, nilai dari variabel tersebut akan berubah untuk semua
# objek yang dihasilkan dari kelas tersebut.
# Dalam kasus kelas Mahasiswa, contoh class attribute yang dapat diberikan adalah jumlah maksimal
# mahasiswa yang dapat diterima oleh universitas tempat mahasiswa tersebut belajar.

# membuat class Mahasiswa
class Mahasiswa:
    # membuat variabel Class Attribute
    maksimal_mahasiswa = 5
    
    # menginisialisasi menggunakan constructor __init__()
    # dengan Instance Attribute
    def __init__(self, nama, usia, alamat):
        self.nama = nama
        self.usia = usia
        self.alamat = alamat