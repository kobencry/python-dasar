# Dalam Python, magic method __mod__() adalah method khusus yang digunakan untuk mengimplementasikan operator modulus (%) pada suatu objek. 
# method ini memungkinkan Anda untuk menghitung sisa hasil pembagian antara dua objek.

# Ketika operator % digunakan untuk membagi dua objek,
# Python secara otomatis memanggil method __mod__() pada objek yang pertama, 
# dan mengirimkan objek kedua sebagai argumen. 
# method ini harus mengembalikan hasil modulus dari objek pertama terhadap objek kedua.

# Deskripsi:
# method __mod__() digunakan untuk mengimplementasikan operator modulus (%). 
# method ini harus mengembalikan sisa hasil pembagian objek saat ini terhadap objek kedua.

# Syntax:
# def __mod__(self, other):
#   Implementasi logika perhitungan modulus

# Parameter:
# self: Merujuk pada objek saat ini.
# other: Merupakan objek kedua yang akan digunakan dalam perhitungan modulus.
# nama parameter "other" bisa diganti dengan nama apapun

# Contoh penggunaan magic method __mod__():
class Modulus:
    def __init__(self, nilai):
        self.nilai = nilai

    def __mod__(self, other):
        # Jika objek other juga merupakan objek dari kelas Modulus
        if isinstance(other, Modulus):
            return self.nilai % other.nilai
        # Jika objek other bukan merupakan objek Modulus, 
        # kita asumsikan bahwa other adalah objek lain (tide data apapun). 
        else:
            return self.nilai % other

# membuat objek Modulus
obj1 = Modulus(10)
obj2 = Modulus(20)

# modulus antara dua objek obj1 dengan obj2 dari kelas Modulus
hasil = obj1 % obj2
print(hasil)
# Output:
# 10

# modulus antara obj1 dengan bilangan bulat
hasil = obj1 % 3
print(hasil)
# Output:
# 1

# modulus antara obj2 dengan bilangan bulat
hasil = obj2 % 3
print(hasil)
# Output:
# 2

# modulus dengan cara penggunaan magic method __mod__()
# Syntax:
# object.__mod__(object/value)

hasil = obj1.__mod__(obj2)
print(hasil)
# Output:
# 10

# modulus antara dua objek obj1 dengan value "bilangan bulat"
hasil = obj1.__mod__(3)
print(hasil)
# Output:
# 1