# Magic method __pow__ dalam Python digunakan untuk mengimplementasikan perilaku operator pangkat (**) pada objek.

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
obj2 = pangkat(2)

# memangkatkan antara dua objek obj1 dengan obj2 dari kelas Pangkat
