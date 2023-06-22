# Magic method __le__ (less than or equal to/kurang dari sama dengan) adalah method khusus dalam Python
# yang digunakan untuk mendefinisikan perilaku objek saat dibandingkan dengan operator <= (kurang dari atau sama dengan).
# method ini memungkinkan kita untuk membandingkan dua objek dan menentukan apakah objek pertama kurang dari atau sama dengan objek kedua.

# Syntax:
# __le__(self, other)
# method __le__ dijalankan ketika operator <= digunakan pada objek.
# method ini menerima dua parameter: self (objek saat ini) dan other (objek yang digunakan sebagai kurang dari sama dengan).
# nama parameter "other" bisa diganti dengan nama apapun

# Ketika kita menggunakan operator <= antara dua objek, Python akan mencari dan menggunakan method __le__ untuk melakukan perbandingan.
# method ini mengembalikan nilai True jika objek pertama kurang dari atau sama dengan objek kedua dalam konteks perbandingan yang didefinisikan, 
# dan mengembalikan nilai False jika tidak.

# Berikut adalah contoh penggunaan method __le__ dalam sebuah kelas:

class Mahasiswa:
    def __init__(self, nilai):
        self.nilai = nilai

    def __le__(self, other):
        # Jika objek other juga merupakan objek dari kelas Mahasiswa 
        if isinstance(other, Mahasiswa):
            return self.nilai <= other.nilai

        # Jika objek other bukan merupakan objek Mahasiswa, 
        # kita asumsikan bahwa other adalah bilangan bulat atau bilangan desimal. 
        else:
            return self.nilai <= other
