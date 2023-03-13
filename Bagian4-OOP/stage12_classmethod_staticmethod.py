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
# membuat class Matematika
class Matematika:
    def tambah(cls, x, y):
        return cls.x + cls.y

print(Matematika.tambah(5, 5))


class Mahasiswa:
    # variabel class
    jumlah = 0

    # menginisialisasi
    def __init__(self, nama):
        # variabel instance
        self.nama = nama

        # setiap object dibuat variabel class "jumlah" ditambahkan 1
        __class__.jumlah += 1

    # classmethod
    def total(cls):
        print(cls.jumlah)

Mahasiswa("alice").total()
Mahasiswa("carl").total()
Mahasiswa("eliot").total()



# classmethod adalah method dalam sebuah kelas yang menerima 
# kelas itu sendiri sebagai argumen pertama. 
# Dalam implementasinya, method ini sering digunakan untuk mengatur atau 
# memodifikasi variabel kelas atau untuk membuat instance baru dari kelas itu sendiri. 
# Salah satu kegunaan umum dari classmethod adalah untuk membuat alternatif konstruktor,
# yang memungkinkan pembuatan instance kelas dengan cara yang berbeda dari konstruktor utama.

# Berikut adalah contoh penggunaan staticmethod dan classmethod dalam Python:

# # membuat class
# class Mahasiswa:
#     # variabel class
#     class_variabel = "Harvard"
    
#     # menginisialisasi objek
#     def __init__(self, nama):
#         # variabel instance
#         self.instance_variabel = nama
    
#     # instance method
#     def instance_method(self):
#         print("Method instance dipanggil")

    
#     def static_method():
#         print("Method static dipanggil")
    
#     @staticmethod
#     def static_method2():
#         print("Method static dipanggil")

# mhs = Mahasiswa("alice")
# mhs.static_method()