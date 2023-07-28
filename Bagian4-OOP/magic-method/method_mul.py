# Dalam Python, magic method __mul__ adalah method khusus dalam Python
# yang digunakan untuk mengimplementasikan operasi perkalian (*) pada objek.
# method ini memungkinkan objek untuk berperilaku seperti tipe data bawaan yang mendukung operasi perkalian.

# Deskripsi:
# Method __mul__() digunakan untuk mengimplementasikan operator perkalian *. 
# Method ini harus mengembalikan hasil perkalian objek saat ini dengan objek kedua.

# Syntax:
# def __mul__(self, other):
    # Implementasi logika perkalian

# Parameter:
# self: Merujuk pada objek saat ini.
# other: Merupakan objek kedua yang akan dikalikan dengan objek saat ini.
# nama parameter "other" bisa diganti dengan nama apapun 

# Berikut adalah contoh penggunaan magic method __mul__ dalam sebuah kelas:
class Kali:
    def __init__(self, nilai):
        self.nilai = nilai

    def __mul__(self, other):
        # Jika objek other juga merupakan objek dari kelas Kali
        if isinstance(other, Kali):
            return self.nilai * other.nilai
        
        # Jika objek other bukan merupakan objek Mahasiswa, 
        # kita asumsikan bahwa other adalah objek lain (tipe data apapun).
        else:
            return self.nilai * other

# membuat objek Kali
obj1 = Kali(2)
obj2 = Kali(3)

# mengalikan antara dua objek obj1 dengan obj2 dari kelas Kali
hasil = obj1 * obj2
print(hasil)
# Output:
# 6

# manglaikan antara dua objek obj1 dengan bilangan bulat
hasil = obj1 * 10
print(hasil)
# Output:
# 20

# Contoh menggunakan  2 atribut
class Kali:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, other):
        return Kali(self.x * other.x, self.y * other.y)

# membuat objek Kali
obj1 = Kali(2, 3)
obj2 = Kali(5, 6)

# mengalikan  objek dari obj1.x dengan obj1.y
hasil = obj1.x * obj1.y
print(hasil)
# Output:
# 6

# mengalikan objek dari obj1 dengan obj2
hasil = obj1 * obj2
print(hasil.x)
# Output:
# 10

print(hasil.y)
# Output:
# 18