# Abstract class pada Python adalah sebuah kelas yang tidak dapat diinstansiasi (tidak dapat dibuatkan objeknya) 
# dan biasanya digunakan sebagai kelas dasar (parent class) 
# yang memiliki method yang belum diimplementasikan (berisi hanya deklarasi method tanpa implementasi). 
# Abstract class pada Python digunakan untuk mengimplementasikan konsep abstract method dan interface, 
# yang merupakan salah satu prinsip dasar dalam pemrograman berorientasi objek.

# Dalam Python, untuk membuat sebuah kelas menjadi abstract class, 
# kita dapat menggunakan modul abc dan mendefinisikan abstract method menggunakan decorator @abstractmethod. 
# Abstract method adalah sebuah method dalam kelas yang hanya dideklarasikan namun tidak diimplementasikan, 
# sehingga harus diimplementasikan di kelas turunannya.

# Berikut adalah contoh implementasi sebuah abstract class pada Python:
from abc import ABC, abstractmethod

class Kendaraan(ABC):
    @abstractmethod
    def jumlah_roda(self):
        pass

class Mobil(Kendaraan):
    def jumlah_roda(self):
        print("Mobil memiliki 4 roda")

class Motor(Kendaraan):
    def jumlah_roda(self):
        print("Motor memiliki 2 roda")

mobil = Mobil()
mobil.jumlah_roda()
# Output:
# Mobil memiliki 4 roda

motor = Motor()
motor.jumlah_roda()
# Output:
# Motor memiliki 2 roda

# Berikut adalah contoh implementasi sebuah abstract class pada Python:
class Product(ABC):
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    @abstractmethod
    def get_diskon(self):
        pass

class DigitalProduct(Product):
    def get_diskon(self):
        return self.harga * 0.9

class TshirtProduct(Product):
    def get_diskon(self):
        return self.harga * 0.8

laptop = DigitalProduct("Laptop", 2000_000)
print(f"Harga setelah diskon: Rp{int(laptop.get_diskon()):,}")
# Output:
# Harga setelah diskon: Rp1,800,000

shirt = TshirtProduct("Kaos Polos", 85_000)
print(f"Harga setelah diskon: Rp{int(shirt.get_diskon()):,}")
# Output:
# Harga setelah diskon: Rp68,000