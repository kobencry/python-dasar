# Dalam Python, Magic method __sub__() adalah method khusus dalam Python 
# yang digunakan untuk mengimplementasikan operasi pengurangan (-) pada suatu objek.
# method ini memungkinkan Anda untuk menentukan perilaku pengurangan kustom pada objek Anda.

# Definisi:
# method __sub__() digunakan untuk mengimplementasikan operasi pengurangan (-) pada objek. method ini mengembalikan hasil pengurangan antara objek saat ini dengan objek yang diberikan.

# Syntax:
# def __sub__(self, other):
#   Implementasi logika pengurangan

# Parameter:
# self: Merujuk pada objek saat ini.
# other: Objek yang akan dikurangkan dari objek saat ini.
# nama parameter "other" bisa diganti dengan nama apapun 

# Contoh penggunaan magic method __sub__ dalam sebuah kelas:
class Kurang:
    def __init__(self, nilai):
        self.nilai = nilai

    def __sub__(self, other):
        # Jika objek other juga merupakan objek dari kelas Kurang
        if isinstance(other, Kurang):
            return self.nilai - other.nilai
        
        # Jika objek other bukan merupakan objek Kurang, 
        # kita asumsikan bahwa other adalah objek lain (tipe data apapun).
        else:
            return self.nilai - other

# membuat objek Kurang
obj1 = Kurang(50)
obj2 = Kurang(30)

# mengurangkan antara dua objek obj1 dengan obj2 dari kelas Kurang
hasil = obj1 - obj2
print(hasil)
# Output:
# 20

# mengurangkan antara dua objek obj1 dengan bilangan bulat
hasil = obj1 - 10
print(hasil)
# Output:
# 40

# membuat objek Kurang menggunakan tipe data string dan set
obj1 = Kurang({'alice', 'carl', 'eliot'})
obj2 = Kurang({'carl'})

# mengurangkan antara dua objek obj1 dengan obj2 dari kelas Kurang
hasil = obj1 - obj2
print(hasil)
# Output:
# {'eliot', 'alice'}

# pengurangan dengan cara penggunaan magic method __sub__()
# Syntax:
# object.__sub__(object/value)

x = Kurang(10)
y = Kurang(2)

# mengurangkan antara dua objek x dengan y dari kelas Kurang 
hasil = x.__sub__(y)
print(hasil)
# Output:
# 8

# mengurangkan antara dua objek x dengan value "bilangan bulat"
hasil = x.__sub__(3)
print(hasil)
# Output:
# 7

# Contoh penggunaan magic method __sub__() dengan 2 atribut:
class Kurang:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        # Jika objek other juga merupakan objek dari kelas Kurang
        if isinstance(other, Kurang):
            return self.x - other.x, self.y - other.y
        
        # Jika objek other bukan merupakan objek Kurang, 
        # kita asumsikan bahwa other adalah objek lain (tipe data apapun).
        else:
            return self.x - other, self.y - other
        

# membuat objek Kurang
obj1 = Kurang(50, 20)
obj2 = Kurang(5, 2)

# mengurangkan antara dua objek obj1.x dengan obj2.y dari kelas Kurang
hasil = obj1.x - obj1.y
print(hasil)
# Output:
# 30

# mengurangkan antara dua objek obj1 dengan obj2 dari kelas Kurang
hasil = obj1 - obj2
print(hasil)
# Output:
# (45, 18)

# mengurangkan antara dua objek obj1.x dengan bilangan bulat
hasil = obj1.x - 30
print(hasil)
# Output:
# 20