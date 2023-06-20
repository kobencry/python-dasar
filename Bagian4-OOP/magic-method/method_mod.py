# Magic method __mod__ adalah method khusus dalam Python 
# yang digunakan untuk mengatur perilaku operasi modulo (%) antara dua objek.
# method ini memungkinkan kita untuk mendefinisikan cara objek dari kelas yang kita buat berperilaku saat dioperasikan dengan operator modulo.

# Ketika operator % digunakan antara dua objek,
# Python akan mencari dan menggunakan method __mod__ untuk menentukan hasil modulo tersebut.
# method ini memungkinkan kita mengendalikan bagaimana objek dari kelas yang kita definisikan akan dikenai operasi modulo.

# Syntax:
# __mod__(self, other)
# method __mod__ dijalankan ketika operator % digunakan pada objek.
# method ini menerima dua parameter: self (objek saat ini) dan other (objek yang digunakan sebagai modulator).
# nama parameter "other" bisa diganti dengan nama apapun

# Berikut adalah contoh sederhana untuk mendemonstrasikan penggunaan method __mod__ dalam Python:

class Modulus:
    def __init__(self, nilai):
        self.nilai = nilai

    def __mod__(self, other):
        if isinstance(other, Modulus):
            return self.nilai % other.nilai
        else:
            return self.nilai % other

# membuat objek Modulus
obj1 = Modulus(10)
obj2 = Modulus(20)

# modulus antara dua objek obj1 dengan obj2
hasil = obj1 % obj2
print(hasil)
# Output:
# 10

# modulus antara obj1 dengan angka
hasil = obj1 % 3
print(hasil)
# Output:
# 1

# modulus antara obj2 dengan angka
hasil = obj2 % 3
print(hasil)
# Output:
# 2