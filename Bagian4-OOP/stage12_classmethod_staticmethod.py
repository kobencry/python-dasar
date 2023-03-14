# staticmethod dan classmethod adalah dua jenis dekorator dalam Python 
# yang dapat digunakan untuk mengubah perilaku method dalam sebuah kelas.

# staticmethod pada Python adalah method yang digunakan untuk mendeklarasikan 
# method statis dalam sebuah kelas.
# Method statis adalah method yang tidak memerlukan instance dari kelas 
# untuk dipanggil dan dapat diakses melalui nama kelas itu sendiri.
# Dalam method static, tidak ada parameter khusus seperti "self" atau "cls". 
# Method static pada umumnya berdiri sendiri dan tidak bergantung pada objek kelas atau objek turunannya.

# Berikut adalah contoh penggunaan staticmethod pada Python:
# membuat class Matematika
class Matematika:
    # static method
    def tambah(x, y):
        return x + y

print(Matematika.tambah(2, 3))
# Output:
# 5

print(Matematika.tambah(5, 5))
# Output:
# 10

# pada contoh di atas, kita membuat kelas "Matematika" yang memiliki method static "tambah"
# untuk melakukan operasi penjumlahan dua angka. 
# method "tambah" dapat dipanggil langsung melalui nama kelas "Matematika" 
# tanpa harus membuat instance kelas terlebih dahulu.

# Menggunakan Decorator @staticmethod
# Decorator "@staticmethod" adalah salah satu jenis decorator di Python 
# yang digunakan untuk menandai sebuah method sebagai static method. 
# Sebuah method static adalah method yang terikat dengan class bukan instance objek,
# sehingga tidak membutuhkan akses ke instance objek untuk dijalankan.

# Penggunaan decorator "@staticmethod" biasanya digunakan ketika method 
# yang dibuat terkait dengan class tersebut secara umum, 
# namun tidak memerlukan penggunaan instance objek dalam penggunaannya.

# Contoh penggunaan decorator @staticmethod:
# membuat class Matematika
class Matematika:
    # static method tanpa decorator
    def tambah(x, y):
        return x + y
    
    # static method menggunakan decorator
    @staticmethod
    def kali(x, y):
        return x * y
    
print(Matematika.tambah(2, 3))
# Output:
# 5

print(Matematika.kali(3, 3))
# Output:
# 9

#=============================================================================

# classmethod adalah sebuah fungsi yang digunakan dalam bahasa pemrograman Python
# dan beroperasi pada level kelas atau "class" bukan pada level "instance" seperti halnya fungsi biasa.

# Secara khusus, classmethod adalah method kelas yang mengoperasikan nilai-nilai 
# dan fungsi pada level kelas dan bukan pada level instance. 
# Dalam method kelas, "cls" digunakan sebagai parameter pertama alih-alih "self"
# yang digunakan dalam method instance.

# Dalam classmethod, parameter pertama "cls" mewakili kelas itu sendiri dan dapat digunakan 
# untuk mengakses atribut kelas dan juga method kelas lainnya. 
# classmethod berguna ketika Anda ingin menggunakan method yang diinginkan oleh kelas itu sendiri,
# bukan oleh instance dari kelas tersebut.

# Berikut adalah contoh penggunaan staticmethod pada Python:
# membuat class Mahasiswa
class Mahasiswa:
    # variabel class
    jumlah = 0

    # menginisialisasi
    def __init__(self, nama):
        # variabel instance
        self.nama = nama

        # setiap object dibuat variabel class "jumlah" ditambahkan 1
        Mahasiswa.jumlah += 1

    # classmethod
    def total(cls):
        print(cls.jumlah)

Mahasiswa("alice").total()
# Output:
# 1

x = Mahasiswa('carl')
x.total()
# Output:
# 2


# Menggunakan Dekorator @classmethod
# Dekorator @classmethod adalah sebuah (penanda) dalam bahasa pemrograman Python 
# yang digunakan untuk mendefinisikan sebuah method kelas (class method).

# Sebuah classmethod adalah method yang terikat dengan kelas dan 
# bukan dengan objek yang dihasilkan dari kelas tersebut. 
# Oleh karena itu, classmethod dapat diakses dan dipanggil langsung dari kelas 
# tanpa perlu membuat instance dari kelas tersebut terlebih dahulu.

# Untuk mendefinisikan sebuah classmethod dalam Python, 
# kita menggunakan @classmethod sebelum mendefinisikan method tersebut.

# Contoh penggunaan decorator @staticmethod:
# membuat class Matematika
class Matematika:
    
    # class method menggunakan decorator
    @classmethod
    def tambah(cls, x, y):
        hasil = x + y
        return hasil

print(Matematika.tambah(5, 5))
# Output:
# 10

print(Matematika.tambah(100, 200))
# Output:
# 300

# Berikut adalah contoh penggunaan staticmethod dan classmethod dalam Python:

# membuat class
class Mahasiswa:
    # variabel class
    class_variabel = "Harvard"
    
    # menginisialisasi objek
    def __init__(self, nama):
        # variabel instance
        self.instance_variabel = nama
    
    # instance method
    def instance_method(self):
        print("Method instance dipanggil")
    
    # static method tanpa decorator
    def static_method():
        print("Method static dipanggil")
    
    # static method dengan decorator
    @staticmethod
    def static_method2():
        print("Method static 2 dipanggil")
    
    # class method dengan decorator
    @classmethod
    def class_method(cls, nama, usia):
        return f"{nama}, {usia}"

# method "static_method" dapat dipanggil langsung melalui nama kelas "Mahasiswa" 
# tanpa harus membuat instance kelas terlebih dahulu.
Mahasiswa.static_method()
# Output:
# Method static dipanggil

# menggunakan staticmethod
x = Mahasiswa("alice")
x.static_method2()
# Output:
# Method static 2 dipanggil

# menggunakan classmethod
y = Mahasiswa.class_method("carl", 23)
print(y)
# Output:
# carl, 23

# method "class_method" dapat dipanggil dengan instance kelas
print(x.class_method('eliot', 20))
# Output:
# eliot, 20