# Getter dan setter adalah method yang digunakan dalam konsep encapsulation di OOP untuk 
# mengakses dan memodifikasi nilai dari atribut kelas. 
# Getter digunakan untuk mengambil nilai dari atribut.
# Setter digunakan untuk memperbarui nilai atribut.

# Getter dan Setter sering digunakan untuk memastikan bahwa nilai atribut kelas tetap terjaga dan 
# terkontrol, sehingga dapat memperbaiki masalah yang muncul ketika nilai atribut 
# diubah secara langsung oleh pengguna program.

# Dalam bahasa Python, getter dan setter biasanya diimplementasikan dengan menggunakan "@property" decorator.
# "@property" decorator digunakan untuk mengubah method biasa menjadi sebuah atribut, 
# sehingga dapat diakses dan dimodifikasi seperti atribut biasa, 
# namun di balik layar sebenarnya terdapat method getter dan setter yang dijalankan.

# Berikut contoh implementasi Getter pada sebuah kelas:
# membuat class Mahasiswa
class Mahasiswa:
    # menginisialisasi objek yang dibuat dari class 'Mahasiswa' menggunakan constructor __init__()
    def __init__(self, input_nama):
        # variabel instance menjadi private "variabel tersebut tidak bisa diakses dari luar kelas"
        self.__nama = input_nama
    
    # Decorator "@property" untuk menandai bahwa method tersebut adalah sebuah property,
    # untuk bisa mengakses fungsi ini seperti atribut, tanpa perlu menggunakan tanda kurung. 
    @property
    def nama(self):
        pass
    # statement "pass", yang artinya method tersebut tidak melakukan apa-apa.

    # Decorator "@<nama_atribut>.getter" untuk menandai bahwa method tersebut 
    # sebagai getter untuk atribut nama.
    # method getter nama() mengembalikan nilai dari atribut __nama.
    @nama.getter
    def nama(self):
        return self.__nama
    
    # magic method __str__ digunakan untuk memberikan representasi string 
    # yang mudah dibaca oleh manusia dari objek.
    def __str__(self):
        # akses variabel private __nama di dalam kelas dengan method getter "self.nama"
        return f"akses dengan variabel private: {self.__nama} \nakses dengan method getter: {self.nama}"
    
# membuat object
mhs = Mahasiswa("alice")
print(mhs)
# Output:
# akses dengan variabel private: alice
# akses dengan method getter: alice

# akses variabel private __nama diluar kelas dengan method getter "mhs.nama"
# anda bisa mengakses method ini seperti atribut, tanpa perlu menggunakan tanda kurung.
print(mhs.nama)
# Output:
# alice

# Berikut contoh implementasi Setter pada sebuah kelas:
# membuat class Mahasiswa
class Mahasiswa:
    # menginisialisasi objek yang dibuat dari class 'Mahasiswa' menggunakan constructor __init__()
    def __init__(self, input_nama):
        # variabel instance menjadi private "variabel tersebut tidak bisa diakses dari luar kelas"
        self.__nama = input_nama
    
    # Decorator "@property" untuk menandai bahwa method tersebut adalah sebuah property,
    # untuk bisa mengakses fungsi ini seperti atribut, tanpa perlu menggunakan tanda kurung. 
    @property
    def nama(self):
        pass
    # statement "pass", yang artinya method tersebut tidak melakukan apa-apa.

    # Decorator "@<nama_atribut>.setter" untuk menandai bahwa method tersebut 
    # sebagai setter untuk atribut nama.
    # method setter nama() menerima nilai nama_baru dan mengubah nilai 
    # dari atribut __nama menjadi nama_baru.
    @nama.setter
    def nama(self, nama_baru):
        self.__nama = nama_baru
    
    # magic method __str__ digunakan untuk memberikan representasi string 
    # yang mudah dibaca oleh manusia dari objek.
    def __str__(self):
        return f"nama: {self.__nama}"

# membuat object
mhs = Mahasiswa("alice")
print("-- sebelum --")
print(mhs)
print("-- setelah --")
# mengubah nama "Mahasiswa" diluar kelas dengan method setter "mhs.nama"
# anda bisa mengakses method ini seperti atribut, tanpa perlu menggunakan tanda kurung.
mhs.nama = "carl"
print(mhs)
# Output:
# -- sebelum --
# nama: alice
# -- setelah --
# nama: carl

#=============================================================================

# anda bisa membuat Getter dengan menggunakan decorator "@property" 
# tanpa harus menggunakan "@nama.getter". 
# Cara ini sering digunakan ketika anda hanya membutuhkan Getter 
# saja dan tidak perlu menetapkan nilai atribut.
class Mahasiswa:
    def __init__(self, input_nama, input_usia):
        self.__nama = input_nama
        self.__usia = input_usia
    
    # getter nama
    @property
    def nama(self):
        return self.__nama
    
    # getter usia
    @property
    def usia(self):
        return self.__usia

mhs = Mahasiswa("eliot", 20)
# akses variabel private __nama diluar kelas dengan method getter "mhs.nama"
# anda bisa mengakses method ini seperti atribut, tanpa perlu menggunakan tanda kurung.
print(mhs.nama)
print(mhs.usia)
# Output:
# eliot
# 20

#===================================================================================

# Menggunakan fungsi property()
# fungsi property() adalah sebuah fungsi bawaan Python yang digunakan untuk membuat 
# dan mengelola atribut objek. 
# Fungsi ini memungkinkan pengguna untuk mendefinisikan 
# method getter, setter, dan deleter pada atribut yang terkait. 
# Hal ini memungkinkan akses ke atribut yang diatur secara otomatis, 
# tanpa harus memanggil method getter atau setter secara langsung. 
# property() akan dianggap sebagai atribut, dan dapat diakses dan diubah dengan 
# cara yang sama seperti variabel.

class Mahasiswa:
    def __init__(self, input_nama):
        self.__nama = input_nama
    
    # Instance method "getter"
    def getNama(self):
        return self.__nama
    
    # Instance method "setter"
    def setNama(self, nama_baru):
        self.__nama = nama_baru
    
    # magic method __str__ digunakan untuk memberikan representasi string
    # yang mudah dibaca oleh manusia dari objek.
    def __str__(self):
        return f"akses dengan variabel private: {self.__nama} \nakses dengan method getter: {self.nama}"

    # Atribut ini bisa digunakan untuk mengakses dan memodifikasi nilai atribut __nama 
    nama = property(getNama, setNama)

# membuat object
mhs = Mahasiswa("alice")
# anda bisa menampilkan object "mhs" karna kelas Mahasiswa menggunakan magic method __str__
print(mhs)
# Output:
# akses dengan variabel private: alice
# akses dengan method getter: alice

# akses nilai variabel private __nama diluar kelas dengan method getter "mhs.nama"
# anda bisa mengakses method ini seperti atribut, tanpa perlu menggunakan tanda kurung.
print(mhs.nama)
# Output:
# alice

# ubah nilai variabel private __nama diluar kelas dengan method setter "mhs.nama"
# anda bisa mengubah method ini seperti atribut, tanpa perlu menggunakan tanda kurung.
mhs.nama = "hello world"
print(mhs.nama)
# Output:
# hello world

# property() akan dianggap sebagai atribut, dan dapat diakses dan diubah dengan 
# cara yang sama seperti variabel.

print(mhs)
# Output:
# akses dengan variabel private: hello world
# akses dengan method getter: hello world