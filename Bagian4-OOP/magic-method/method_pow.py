# Dalam Python, Magic method __pow__() adalah method khusus dalam Python 
# yang digunakan untuk mengimplementasikan operasi pangkat (**) pada suatu objek. 
# method ini memungkinkan Anda untuk menentukan perilaku pangkat kustom pada objek Anda.

# Definisi:
# method __pow__() digunakan untuk mengimplementasikan operasi pangkat (**) pada objek. 
# method ini harus mengembalikan hasil perpangkatan objek saat ini dengan objek yang diberikan.

# Syntax:
# def __pow__(self, other):
#   Implementasi logika pangkat

# Parameter:
# self: Merujuk pada objek saat ini.
# other: Objek yang akan digunakan sebagai pangkat.
# nama parameter "other" bisa diganti dengan nama apapun 

# Contoh penggunaan magic method __pow__():
class Pangkat:
    def __init__(self, nilai):
        self.nilai = nilai

    def __pow__(self, other):
        # Jika objek other juga merupakan objek dari kelas Pangkat
        if isinstance(other, Pangkat):
            return self.nilai ** other.nilai

        # Jika objek other bukan merupakan objek Pangkat, 
        # kita asumsikan bahwa other adalah objek lain (tipe data apapun).
        else:
            return self.nilai ** other

# membuat objek Pangkat
obj1 = Pangkat(5)
obj2 = Pangkat(2)

# memangkatkan antara dua objek obj1 dengan obj2 dari kelas Pangkat
hasil = obj1 ** obj2
print(hasil)
# Output:
# 25

# memangkatkan antara objek obj1 dengan bilangan bulat
hasil = obj1 ** 3
print(hasil)
# Output:
# 125

# memangkatkan antara objek obj2 dengan bilangan bulat
hasil = obj2 ** 3
print(hasil)
# Output:
# 8

# memangkatkan dengan cara penggunaan magic method __pow__()
# Syntax:
# object.__pow__(object/value)

# memangkatkan antara dua objek obj1 dengan obj2 dari kelas Pangkat
hasil = obj1.__pow__(obj2)
print(hasil)
# Output:
# 25

# memangkatkan antara objek obj1 dengan value "bilangan bulat".
hasil = obj1.__pow__(3)
print(hasil)
# Output:
# 125