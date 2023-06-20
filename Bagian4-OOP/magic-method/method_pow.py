# Magic method __pow__ dalam Python digunakan untuk mengimplementasikan perilaku operator pangkat (**) pada objek.

# Syntax:
# __pow__(self, other)
# method __pow__ dijalankan ketika operator ** digunakan pada objek.
# method ini menerima dua parameter: self (objek saat ini) dan other (objek yang digunakan sebagai pangkat).
# nama parameter "other" bisa diganti dengan nama apapun

# Ketika kita menggunakan operator pangkat pada dua objek atau objek dengan bilangan lainnya, 
# Python akan mencari dan menggunakan magic method __pow__ untuk menghitung hasil pangkat.

# Berikut adalah contoh penggunaan magic method __pow__ dalam sebuah kelas:

class Pangkat:
    def __init__(self, nilai):
        self.nilai = nilai

    def __pow__(self, other):
        # Jika objek other juga merupakan objek dari kelas Pangkat
        if isinstance(other, Pangkat):
            return self.nilai ** other.nilai

        # Jika objek other bukan merupakan objek Pangkat, 
        # kita asumsikan bahwa other adalah bilangan bulat atau bilangan desimal.
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

# memangkatkan antara obj1 dengan bilangan bulat
hasil = obj1 ** 3
print(hasil)
# Output:
# 125

# memangkatkan antara obj2 dengan bilangan bulat
hasil = obj2 ** 3
print(hasil)
# Output:
# 8
