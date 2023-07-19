# Dalam Python, Magic method __isub__ adalah method khusus dalam Python yang digunakan untuk mengimplementasikan 
# operasi pengurangan terhadap objek saat ini dengan objek lain. 
# Method ini dipanggil ketika operator -= digunakan untuk mengurangkan objek saat ini dengan objek lain.

# Deskripsi:
# Metode __isub__ memungkinkan kita untuk mendefinisikan perilaku pengurangan 
# in-place pada objek yang kita definisikan. 
# Ketika operator -= digunakan pada objek, metode ini akan dipanggil secara otomatis. 
# Kita dapat mengontrol bagaimana objek itu sendiri diubah setelah operasi pengurangan dilakukan.

# Syntax:
# def __isub__(self, other):
    # Implementasikan operasi pengurangan antara self dan other
    # Modifikasi objek saat ini dengan hasil pengurangan

# Parameter:
# self: Merujuk pada objek saat ini.
# other: Merujuk pada objek yang akan dikurangkan dengan objek saat ini.
# nama parameter "other" bisa diganti dengan nama apapun

# Berikut adalah contoh penggunaan magic method __isub__ dalam sebuah kelas:
class Menghitung:
    def __init__(self, nilai):
        self.nilai = nilai
    
    def __isub__(self, other):
        # Jika objek other juga merupakan objek dari kelas Menghitung
        if isinstance(other, Menghitung):
            self.nilai -= other.nilai
            return self.nilai
    
        # Jika objek other bukan merupakan objek Menghitung,
        # kita asumsikan bahwa other adalah objek lain (tipe data apapun)
        else:
            self.nilai -= other
            return self.nilai

# membuat objek Menghitung
x = Menghitung(10)
y = Menghitung(2)

# pengurangan dan penugasan antara dua objek x dengan y dari kelas Menghitung
x -= y # 10 - 2
print(x)
# Output:
# 8

# pengurangan dan penugasan antara objek x dengan bilangan bulat
x -= 3 # 8 - 3
print(x)
# Output:
# 5

# pengurangan dan penugasan dengan cara penggunaan magic method __isub__()
# Syntax:
# object.__isub__(object/value)

# membuat objek Menghitung
obj1 = Menghitung(50)
obj2 = Menghitung(20)

obj1.__isub__(obj2) # 50 - 20
print(obj1.nilai)
# Output:
# 30