# Abstract class pada Python adalah sebuah kelas yang tidak dapat diinstansiasi (tidak dapat dibuatkan objeknya) 
# dan biasanya digunakan sebagai kelas dasar (parent class) 
# yang memiliki method yang belum diimplementasikan (berisi hanya deklarasi method tanpa implementasi). 
# Abstract class pada Python digunakan untuk mengimplementasikan konsep abstract method dan interface, 
# yang merupakan salah satu prinsip dasar dalam pemrograman berorientasi objek.

# Dalam Python, untuk membuat sebuah kelas menjadi abstract class, 
# kita dapat menggunakan modul abc dan mendefinisikan abstract method menggunakan decorator @abstractmethod. 
# Abstract method adalah sebuah method dalam kelas yang hanya dideklarasikan namun tidak diimplementasikan, 
# sehingga harus diimplementasikan di kelas turunannya.