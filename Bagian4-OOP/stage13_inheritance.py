# Inheritance (pewarisan atau sifat pewarisan) pada Python adalah konsep di mana 
# sebuah kelas baru dibuat dengan memperluas fungsionalitas kelas yang sudah ada.
# Dalam pewarisan, kelas baru didefinisikan dengan menggunakan kelas yang sudah ada 
# sebagai landasan atau superclass, sehingga kelas baru dapat mewarisi atribut dan method dari superclass.

# Dengan menggunakan inheritance, kita dapat membuat hierarki kelas yang lebih 
# mudah dikelola dan memungkinkan kita untuk menghindari duplikasi kode dan 
# meningkatkan modularitas dan fleksibilitas kode. 

# Di Python, inheritance(pewarisan) dilakukan dengan menempatkan nama kelas induk(parent) 
# dalam kurung setelah nama kelas turunan.

# Berikut adalah contoh "tidak menggunakan" inheritance pada Python
class A:
    def __init__(self, nama, usia):
        # instance variabel
        self.__nama = nama
        self.__usia = usia
    
    # instance method
    def display(self):
        return f"{self.__nama}, {self.__usia}"

class B:
    def __init__(self, nama, usia, alamat):
        # instance variabel
        self.__nama = nama
        self.__usia = usia
        self.__alamat = alamat
    
    # instance method
    def display(self):
        return f"{self.__nama}, {self.__usia}, {self.__alamat}"
a = A('alice', 23)
print(a.display())
# Output:
# alice, 23


b = B('carl', 25, 'jakarta')
print(b.display())
# Output:
# carl, 25, jakarta

# Dalam hal ini kelas A dan B memiliki atribut dan method yang sama.
# atribut nama, usia, dan method display()
# lalu kita membuat instance variabel di class B yang sudah ada di class A, 
# artinya kita menulis ulang kode yang sudah ada.
# di Pemograman “Don't Repeat Yourself” 
# (atau lebih mudahnya disingkat DRY) 
# adalah satu kalimat istilah yang sering diperbincangkan di kalangan teknis pemrograman yaitu 
# untuk tidak mengulangi proses yang sama berulang kali,
# yang mana sebenarnya proses tersebut dapat dilakukan dengan suatu solusi hanya satu kali saja.

# Berikut adalah contoh sederhana inheritance pada Python
class A: # class parent(Induk) atau disebut superclass
    def __init__(self, nama, usia):
        self.__nama = nama
        self.__usia = usia
    
    def display(self):
        return f"{self.__nama}, {self.__usia}"

class B(A): # class child(anak) atau disebut subclass
    def __init__(self, nama, usia, alamat):
        # jika tidak menggunakan inheritance(pewarisan) dari kelas A
        #self.__nama = nama
        #self.__usia = usia

        # jika menggunakan inheritance(pewarisan) dari kelas A
        A.__init__(self, nama, usia)
        self.__alamat = alamat
    
    # method instance "jika tidak menggunakan inheritance(pewarisan) dari kelas A"
    # def display(self):
    #     return f"{self.__nama}, {self.usia}, {self.__alamat}"
    
    # method instance dari kelas A atau parent(induk) 
    def display(self):
        return f"{A.display(self)}, {self.__alamat}"
# membuat object
a = A("eliot", 24)
print(a.display())
# Output:
# eliot, 24

# membuat object
b = B("gerald", 22, "surabaya")
print(b.display())
# Output:
# gerald, 22, surabaya

# class "A" adalah superclass atau parent class, sedangkan 
# class "B" adalah subclass atau child class yang mewarisi atribut dan method dari class "A".
# class "A" memiliki atribut nama dan usia, serta method display() untuk menampilkan informasi nama dan usia.
# class "B" memiliki tambahan atribut alamat, serta meng-overwrite(menimpa) method display() dari class "A" 
# untuk menampilkan informasi alamat.

# Pada saat membuat objek dari class "B", kita memberikan parameter nama, usia, dan alamat. 
# Method __init__() di class "B" memanggil method __init__() di class "A" menggunakan nama_kelas.__init__(self, nama, usia) 
# untuk menginisialisasi atribut nama dan usia.

# Ketika method display() dipanggil pada objek b, terlebih dahulu method display() 
# dari superclass dipanggil dengan nama_kelas.display(self), kemudian informasi alamat ditambahkan.