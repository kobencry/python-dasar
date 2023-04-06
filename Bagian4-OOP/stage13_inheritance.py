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
        # variabel instance
        self.__nama = nama
        self.__usia = usia
    
    # method instance
    def display(self):
        return f"{self.__nama}, {self.__usia}"

class B:
    def __init__(self, nama, usia, alamat):
        # variabel instance
        self.__nama = nama
        self.__usia = usia
        self.__alamat = alamat
    
    # method instance
    def info(self):
        return f"{self.__nama}, {self.__usia}, {self.__alamat}"
a = A('alice', 23)
print(a.display())
# Output:
# alice, 23


b = B('carl', 25, 'jakarta')
print(b.info())
# Output:
# carl, 25, jakarta

# Dalam hal ini kelas A dan B memiliki atribut dan method yang sama.
# atribut nama, usia, dan memiliki method "display(), info()" yang fungsinya sama-sama menampilkan data
# lalu kita membuat instance variabel di class B yang sudah ada di class A, 
# artinya kita menulis ulang kode yang sudah ada.
# di Pemrograman “Don't Repeat Yourself” 
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
    # def info(self):
    #     return f"{self.__nama}, {self.usia}, {self.__alamat}"
    
    # method instance dari kelas A atau parent(induk) 
    def info(self):
        return f"{A.display(self)}, {self.__alamat}"
# membuat object
a = A("eliot", 24)
print(a.display())
# Output:
# eliot, 24

# membuat object
b = B("gerald", 22, "surabaya")
print(b.info())
# Output:
# gerald, 22, surabaya

# class "A" adalah superclass atau parent class, sedangkan 
# class "B" adalah subclass atau child class yang mewarisi atribut dan method dari class "A".
# class "A" memiliki atribut nama dan usia, serta method display() untuk menampilkan informasi nama dan usia.
# class "B" memiliki sebuah method "info()" yang menggunakan method "display()" dari, 
# class "A" untuk menampilkan nilai "nama" dan "usia", dan menambahkan nilai "alamat", untuk menampilkan informasi alamat.

# Pada saat membuat objek dari class "B", kita memberikan parameter nama, usia, dan alamat. 
# Method __init__() di class "B" memanggil method __init__() di class "A" menggunakan nama_kelas.__init__(self, nama, usia) 
# untuk menginisialisasi atribut nama dan usia.

# Ketika method info() dipanggil pada objek b, terlebih dahulu method display() 
# dari superclass dipanggil dengan nama_kelas.display(self), kemudian informasi alamat ditambahkan.

#---------------------------------------------------
# Inheritance dengan Magic method super()

# Magic method super() adalah sebuah built-in function di Python yang memungkinkan kita untuk
# memanggil method atau atribut dari parent class atau superclass saat kita membuat subclass. 
# method super() biasanya digunakan dalam method __init__() dari subclass untuk mengakses 
# constructor atau method parent class.

# Dalam penggunaannya, method super() menerima dua argumen, 
# yaitu nama class saat ini (dalam hal ini subclass) dan instance objek saat ini.
# Dengan menggunakan method super(), kita bisa memanggil method dari parent class dan 
# menggunakan variabel atau atribut dari parent class.

# Contoh penggunaan method super() pada subclass yang meng-inheritance(mewarisi) dari parent class:
class A: # parent class atau disebut superclass
    def __init__(self, nama, usia):
        self.__nama = nama
        self.__usia = usia

    # method instance
    def display(self):
        return f"{self.__nama}, {self.__usia}"

class B(A): # child class atau disebut subclass
    def __init__(self, nama, usia, alamat):
        # contoh dengan memanggil nama classnya
        #A.__init__(self, nama, usia)

        # contoh dengan magic method super()
        super().__init__(nama, usia)
        self.__alamat = alamat

    # method instance
    def info(self):
        # contoh dengan memanggil nama classnya
        #return f"{A.display()}, {self.__alamat}"

        # contoh dengan magic method super()
        return f"{super().display()}, {self.__alamat}"

a = A("alice", 23)
print(a.display())
# Output:
# alice, 23

b = B("carl", 22, "jakarta")
print(b.info())
# Output:
# carl, 22, jakarta