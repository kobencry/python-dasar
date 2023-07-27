# Dalam Python, Magic method __truediv__ merupakan salah satu Method khusus dalam Python 
# yang digunakan untuk mengimplementasikan perilaku pembagian menggunakan operator '/' pada objek
# yang dibuat dari kelas yang kita definisikan.

# Method ini disebut "true division" karena menghasilkan hasil pembagian sejati(hasil bilangan pecahan) 
# daripada pembagian floor (hasil bilangan bulat) yang diberikan oleh Method __floordiv__.

# Deskripsi:
# Method __truediv__ memungkinkan kita untuk mendefinisikan perilaku pembagian pada objek yang kita definisikan.
# Ketika operator '/' digunakan pada objek, Method ini akan dipanggil secara otomatis. 
# Kita dapat mengontrol hasil pembagian sesuai kebutuhan kita.

# Syntax:
# def __truediv__(self, other):
    # Implementasikan operasi pembagian antara self dan other
    # Return hasil pembagian

# self: Merujuk pada objek saat ini.
# other: Merujuk pada objek yang akan dibagi dengan objek saat ini.
# nama parameter "other" bisa diganti dengan nama apapun 

# Berikut adalah contoh penggunaan magic method __truediv__ dalam sebuah kelas:
class TrueDiv:
    def __init__(self, nilai):
        self.nilai = nilai

    def __truediv__(self, other):
        # Jika objek other juga merupakan objek dari kelas TrueDiv
        if isinstance(other, TrueDiv):
            return self.nilai / other.nilai

        # Jika objek other bukan merupakan objek TrueDiv, 
        # kita asumsikan bahwa other adalah objek lain (tipe data apapun).
        else:
            return self.nilai / other

# membuat objek TrueDiv
obj1 = TrueDiv(10)
obj2 = TrueDiv(2)

# pembagian antara dua objek obj1 dengan obj2 dari kelas TrueDiv
hasil = obj1 / obj2
print(hasil)
# Output:
# 5.0

# pembagian antara dua objek obj2 dengan obj1 dari kelas TrueDiv
hasil = obj2 / obj1
print(hasil)
# Output:
# 0.2

# pembagian antara objek obj1 dengan bilangan bulat
hasil = obj1 / 3
print(hasil)
# Output:
# 3.3333333333333335

# pembagian dengan cara penggunaan magic method __truediv__()
# Syntax:
# object.__truediv__(object/value)

# pembagian antara dua objek obj1 dan obj2 dari kelas TrueDiv
hasil = obj1.__truediv__(obj2)
print(hasil)
# Output:
# 5.0

# pembagian antara objek obj1 dengan bilangan bulat
hasil = obj1.__truediv__(3)
print(hasil)
# Output:
# 3.3333333333333335

# Berikut adalah contoh penggunaan magic method __truediv__ dengan 2 atribut
class Fraction:
    def __init__(self, pembilang, penyebut):
        self.pembilang = pembilang
        self.penyebut = penyebut
    
    # Membagi bilangan pecahan dengan bilangan bulat
    def __truediv__(self, other):
        # Jika objek other juga merupakan objek dari kelas Fraction
        if isinstance(other, Fraction):
            return Fraction(self.pembilang * other.penyebut, self.penyebut * other.pembilang)
        
        # Jika objek other bukan merupakan objek Fraction,
        # kita asumsikan bahwa other adalah objek lain (tipe data apapun)
        else:
            return Fraction(self.pembilang, self.penyebut * other)
    
    # Menampilkan hasil bilangan pecahan dan bilangan bulat
    def __str__(self):
        return f"{self.pembilang}/{self.penyebut}"

# membuat objek Fraction
obj1 = Fraction(3, 4)
obj2 = Fraction(2, 5)

# pembagian antara dua objek obj1 dan obj2 dari kelas Fraction
hasil = obj1 / obj2
print(hasil) 
# Output:
# 15/8

# pembagian antara objek obj1 dengan bilangan bulat
hasil = obj1 / 2
print(hasil)
# Output:
# 3/8

# pembagian dengan cara penggunaan magic method __truediv__()
# Syntax:
# object.__truediv__(object/value)

# pembagian antara dua objek obj1 dan obj2 dari kelas Fraction
hasil = obj1.__truediv__(obj2)
print(hasil)
# Output:
# 15/8