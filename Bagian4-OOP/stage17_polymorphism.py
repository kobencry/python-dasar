# Polymorphism pada Python adalah kemampuan sebuah objek untuk memiliki banyak bentuk atau tampilan yang berbeda, 
# tergantung pada konteksnya. 
# Polymorphism memungkinkan objek untuk memiliki perilaku yang berbeda saat berinteraksi dengan objek yang berbeda pula.

# Di Python, polymorphism dapat dicapai dengan menggunakan teknik seperti operator overloading, 
# method overloading, dan method overriding. 
# Operator overloading memungkinkan operator standar seperti + dan - dapat digunakan pada objek-objek yang kita definisikan sendiri. 
# Method overloading memungkinkan sebuah kelas memiliki beberapa method dengan nama yang sama, 
# namun memiliki parameter yang berbeda. 
# Method overriding memungkinkan kelas turunan untuk menimpa method yang sama pada kelas induk dengan implementasi yang berbeda.

# Polymorphism sangat penting dalam OOP karena memungkinkan kode kita lebih fleksibel dan modular. 
# Dengan menggunakan polymorphism, kita dapat memanfaatkan abstraksi dan pewarisan(inheritance) pada kelas 
# untuk membuat kode yang lebih efisien dan mudah di-maintain. 
# Polymorphism juga dapat meningkatkan reusabilitas kode, 
# karena objek yang sama dapat memiliki perilaku yang berbeda dalam konteks yang berbeda.

# Berikut adalah contoh sederhana penggunaan polymorphism di Python pada kelas Hewan:
class Hewan:
    def suara(self):
        pass

class Anjing(Hewan):
    def suara(self):
        print("guk guk")

class Kucing(Hewan):
    def suara(self):
        print("meow")

class Ayam(Hewan):
    def suara(self):
        print("kukuruyuk")

anjing = Anjing()
kucing = Kucing()
ayam = Ayam()

for x in (anjing, kucing, ayam):
    # memanggil metode suara dari masing-masing objek
    x.suara()
# Output:
# guk guk
# meow
# kukuruyuk

# Berikut adalah contoh sederhana penggunaan polymorphism di Python pada kelas Mahasiswa:
class Mahasiswa: #superclass
    # inisalisasi
    def __init__(self, nama, nim):
        # variabel instance
        self.nama = nama
        self.nim = nim
    
    # method instance
    def keterangan(self):
        print(f"Nama:{self.nama}, Nim:{self.nim}")
    
class MahasiswaS1(Mahasiswa): #subclass
    # inisialisasi
    def __init__(self, nama, nim, jurusan):
        # variabel instance
        super().__init__(nama, nim)
        self.jurusan = jurusan
    
    # method instance
    def keterangan(self):
        print(f"Mahasiswa S1 {self.nama} dengan Nim {self.nim} jurusan {self.jurusan}")

class MahasiswaS2(Mahasiswa): #subclass
    # inisialisasi
    def __init__(self, nama, nim, program_studi):
        # variabel instance
        super().__init__(nama, nim)
        self.program_studi = program_studi
    
    # method instance
    def keterangan(self):
        print(f"Mahasiswa S2 {self.nama} dengan Nim {self.nim} program studi {self.program_studi}")

# membuat objek dari masing2  kelas
mhs1 = MahasiswaS1("Alice", "112233", "Informatika")
mhs2 = MahasiswaS2("Carl", "445566", "Sistem Informasi")

mhs1.keterangan()
# Output:
# Mahasiswa S1 Alice dengan Nim 112233 jurusan Informatika

mhs2.keterangan()
# Output:
# Mahasiswa S2 Carl dengan Nim 445566 program studi Sistem Informasi

# Berikut adalah contoh sederhana penggunaan Polymorphism di Python pada kelas Product:
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_discount(self, discount):
        pass

class DigitalProduct(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def calculate_discount(self, discount):
        self.price -= (self.price * discount/100)

class PhysicalProduct(Product):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight

    def calculate_discount(self, discount):
        self.price -= (self.price * discount/100) + (self.weight * 0.1)

# objek dari masing-masing kelas
digital_product = DigitalProduct("Ebook", 100, 20)
physical_product = PhysicalProduct("Buku", 50, 0.5)

# memanggil metode calculate_discount dari masing-masing objek
digital_product.calculate_discount(10)
physical_product.calculate_discount(10) 