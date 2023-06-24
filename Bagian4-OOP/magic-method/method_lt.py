# Magic method __lt__ (less than/kurang dari) adalah method khusus dalam Python 
# yang digunakan untuk mendefinisikan perilaku objek saat dibandingkan dengan operator < (less than/kurang dari).
# method ini memungkinkan kita untuk membandingkan dua objek dan menentukan apakah objek pertama lebih kecil daripada objek kedua.

# Syntax:
# __lt__(self, other)
# method __lt__ dijalankan ketika operator < digunakan pada objek.
# method ini menerima dua parameter: self (objek saat ini) dan other (objek yang digunakan sebagai less than/kurang dari).
# nama parameter "other" bisa diganti dengan nama apapun

# Ketika kita menggunakan operator < antara dua objek, 
# Python akan mencari dan menggunakan method __lt__ untuk melakukan perbandingan.
# method ini mengembalikan nilai True jika objek pertama kurang dari objek kedua dalam konteks perbandingan yang didefinisikan,
# dan mengembalikan nilai False jika tidak.

# Berikut adalah contoh penggunaan method __lt__ dalam sebuah kelas:

class Mahasiswa:
    def __init__(self, nilai):
        self.nilai = nilai

    def __lt__(self, other):
        # Jika objek other juga merupakan objek dari kelas Mahasiswa 
        if isinstance(other, Mahasiswa):
            return self.nilai < other.nilai

        # Jika objek other bukan merupakan objek Mahasiswa, 
        # kita asumsikan bahwa other adalah objek lain (tipe data apapun). 
        else:
            return self.nilai < other

# membuat objek Mahasiswa
mhs1 = Mahasiswa(22)
mhs2 = Mahasiswa(28)

# membandingkan antara dua objek mhs1 dengan mhs2 dari kelas Mahasiswa
hasil = mhs1 < mhs2
print(hasil)
# Output:
# True

hasil = mhs2 < mhs1
print(hasil)
# Output:
# False

# membandingkan antara objek mhs1 dengan bilangan bulat
hasil = mhs1 < 50
print(hasil)
# Output:
# True