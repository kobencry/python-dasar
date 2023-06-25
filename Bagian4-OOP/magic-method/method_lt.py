# Dalam Python, magic method __lt__() adalah method khusus yang digunakan untuk mengimplementasikan operator kurang dari < pada suatu objek. 
# method ini memungkinkan Anda untuk menentukan hubungan kurang dari antara dua objek.

# Ketika operator < digunakan untuk membandingkan dua objek, 
# Python secara otomatis memanggil method __lt__() pada objek yang pertama, 
# dan mengirimkan objek kedua sebagai argumen. 
# method ini harus mengembalikan True jika objek pertama kurang dari objek kedua,
# dan False jika tidak.

# Deskripsi:
# method __lt__() digunakan untuk mengimplementasikan operator < kurang dari.
# method ini harus mengembalikan True jika objek saat ini kurang dari objek kedua, 
# dan False jika tidak.

# Syntax:
# def __lt__(self, other):
#   Implementasi logika perbandingan kurang dari

# Parameter:
# self: Merujuk pada objek saat ini.
# other: Merupakan objek kedua yang akan dibandingkan dengan objek saat ini.
# nama parameter "other" bisa diganti dengan nama apapun

# Contoh penggunaan magic method __lt__():
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

# membandingkan dengan cara penggunaan magic method __lt__()
# Syntax:
# object.__lt__(object/value)

hasil = mhs1.__lt__(mhs2)
print(hasil)
# Output:
# True

hasil = mhs2.__lt__(mhs1)
print(hasil)
# Output
# False

# membandingkan antara objek mhs1 dengan value "bilangan bulat"
hasil = mhs1.__lt__(50)
print(hasil)
# Output:
# True