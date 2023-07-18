# Magic method __eq__ (equal to/sama dengan) adalah method khusus dalam Python
# yang digunakan untuk mendefinisikan perilaku objek saat dibandingkan dengan operator == (sama dengan).
# method ini memungkinkan kita untuk membandingkan dua objek dan menentukan apakah objek tersebut sama atau tidak.

# Deskripsi:
# Method __eq__ mengembalikan nilai boolean, yaitu True jika objek saat ini sama dengan 
# objek lain(berdasarkan logika persamaan yang diimplementasikan), 
# dan False jika objek saat ini berbeda dari objek lain.

# Syntax:
# def __eq__(self, other):
    # Implementasikan logika persamaan antara self dan other
    # Mengembalikan True jika self sama dengan other, False jika tidak

# Parameter:
# self: Merujuk pada objek saat ini yang memanggil method __eq__.
# other: Merujuk pada objek yang dibandingkan dengan objek saat ini.
# nama parameter "other" bisa diganti dengan nama apapun

# Berikut adalah contoh penggunaan method __eq__ dalam sebuah kelas:
class Mahasiswa:
    def __init__(self, nilai):
        self.nilai = nilai

    def __eq__(self, other):
        # Jika objek other juga merupakan objek dari kelas Mahasiswa 
        if isinstance(other, Mahasiswa):
            return self.nilai == other.nilai
        
        # Jika objek other bukan merupakan objek Mahasiswa, 
        # kita asumsikan bahwa other adalah bilangan bulat atau bilangan desimal. 
        else:
            return self.nilai == other

# membuat objek Mahasiswa
mhs1 = Mahasiswa(20)
mhs2 = Mahasiswa(20)

# membandingkan antara dua objek mhs1 dengan mhs2 dari kelas Mahasiswa
hasil = mhs1 == mhs2
print(hasil)
# Output:
# True

hasil = mhs2 == mhs1
print(hasil)
# Output:
# True

# membandingkan antara mhs1 dengan bilangan bulat
hasil = mhs1 == 50
print(hasil)
# Output:
# False

# membandingkan dengan cara penggunaan magic Method __eq__()
# Syntax:
# object.__eq__(object/value)

# membandingkan antara dua objek mhs1 dan mhs2 dari kelas Mahasiswa
hasil = mhs1.__eq__(mhs2)
print(hasil)
# Output:
# True

# membandingkan antara dua objek mhs1 dengan bilangan bulat
hasil = mhs1.__eq__(50)
print(hasil)
# Output:
# False

# Berikut adalah contoh penggunaan magic method __eq__() dengan 2 atribut
class EqualTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        # Jika objek other juga merupakan objek dari kelas EqualTo
        if isinstance(other, EqualTo):
            return EqualTo(self.x == other.x, self.y == other.y)
        
        # Jika objek other bukan merupakan objek EqualTo, 
        # kita asumsikan bahwa other adalah bilangan bulat atau bilangan desimal. 
        else:
            return EqualTo(self.x == other, self.y == other)

# membuat objek EqualTo
obj1 = EqualTo(20, 50)
obj2 = EqualTo(20, 100)

# membandingkan antara dua objek obj1.x dengan obj2.y dari kelas EqualTo
hasil = obj1.x == obj2.y # 20 == 100
print(hasil)
# Output:
# False

# membandingkan antara dua objek obj1.x dengan obj2.x dari kelas EqualTo
hasil = obj1.x == obj2.x # 20 == 20
print(hasil)
# Output:
# True

# membandingkan dengan cara penggunaan magic method __eq__()
# Syntax:
# object.__eq__(object/value)

# membandingkan antara dua objek obj1 dan obj2 dari kelas Mahasiswa
hasil = obj1.__eq__(obj2)
print(hasil.x)
# Output:
# True

print(hasil.y)
# Output:
# False

# membandingkan antara objek obj1 dengan value "bilangan bulat"
hasil = obj1.__eq__(20)
print(hasil.x)  # 20 == 20
print(hasil.y)  # 50 == 20
# Output:
# True
# False