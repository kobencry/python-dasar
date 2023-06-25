# Dalam Python, magic method __le__() adalah method khusus yang digunakan untuk mengimplementasikan operator kurang dari sama dengan <= pada suatu objek. 
# method ini memungkinkan Anda untuk menentukan hubungan kurang dari sama dengan antara dua objek.

# Ketika operator <= digunakan untuk membandingkan dua objek, 
# Python secara otomatis memanggil method __le__() pada objek yang pertama, 
# dan mengirimkan objek kedua sebagai argumen. 
# method ini harus mengembalikan True jika objek pertama kurang dari atau sama dengan objek kedua,
# dan False jika tidak.

# Deskripsi:
# method __le__() digunakan untuk mengimplementasikan operator <= "kurang dari sama dengan". 
# method ini harus mengembalikan True jika objek saat ini kurang dari atau sama dengan objek kedua, 
# dan False jika tidak.

# Syntax:
# def __le__(self, other):
#   Implementasi logika perbandingan kurang dari sama dengan

# Parameter:
# self: Merujuk pada objek saat ini.
# other: Merupakan objek kedua yang akan dibandingkan dengan objek saat ini.
# nama parameter "other" bisa diganti dengan nama apapun

# Contoh penggunaan magic method __le__():
class Mahasiswa:
    def __init__(self, nilai):
        self.nilai = nilai

    def __le__(self, other):
        # Jika objek other juga merupakan objek dari kelas Mahasiswa 
        if isinstance(other, Mahasiswa):
            return self.nilai <= other.nilai

        # Jika objek other bukan merupakan objek Mahasiswa, 
        # kita asumsikan bahwa other adalah objek lain (tipe data apapun). 
        else:
            return self.nilai <= other

# membuat objek Mahasiswa
mhs1 = Mahasiswa(20)
mhs2 = Mahasiswa(30)

# membandingkan antara dua objek mhs1 dengan mhs2 dari kelas Mahasiswa
hasil = mhs1 <= mhs2
print(hasil)
# Output:
# True

hasil = mhs2 <= mhs1
print(hasil)
# Output:
# False

# membandingkan antara objek mhs1 dengan bilangan bulat 
hasil = mhs1 <= 50
print(hasil)
# Output:
# True

# membandingkan dengan cara penggunaan magic method __le__()
# Syntax:
# object.__le__(object/value)

hasil = mhs1.__le__(mhs2)
print(hasil)
# Output:
# True

hasil = mhs2.__le__(mhs1)
print(hasil)
# Output:
# False

# membandingkan antara objek mhs1 dengan value "bilangan bulat"
hasil = mhs1.__le__(50)
print(hasil)
# Output:
# True