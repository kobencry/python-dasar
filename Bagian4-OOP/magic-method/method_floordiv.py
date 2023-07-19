# Dalam Python, Magic method __floordiv__ adalah method khusus dalam Python 
# yang digunakan untuk mengimplementasikan operasi pembagian bulat (floor division) (//) pada objek.
# method ini memungkinkan objek untuk berperilaku seperti tipe data bawaan yang mendukung operasi pembagian bulat.

# Deskripsi:
# Method __floordiv__ digunakan untuk mengubah perilaku operasi floor
# division ketika operator // digunakan pada objek.

# Syntax:
# def __floordiv__(self, other):
    # implementasi floor division

# Parameter
# self: Merupakan objek yang menggunakan operator //.
# other: Merupakan objek yang menjadi operand kedua dalam operasi floor division.
# nama parameter "other" bisa diganti dengan nama apapun.

# Ketika Anda menggunakan operator pembagian bulat (//) antara dua objek,
# Python akan mencari dan memanggil magic method __floordiv__ pada objek pertama,
# dan meneruskan objek kedua sebagai argumen. 
# method ini harus mengembalikan hasil pembagian bulat objek tersebut.

# Berikut adalah contoh penggunaan magic method __floordiv__ dalam sebuah kelas:
class FloorDiv:
    def __init__(self, nilai):
        self.nilai = nilai
    
    def __floordiv__(self, other):
        # Jika objek other juga merupakan objek dari kelas FloorDiv 
        if isinstance(other, FloorDiv):
            return self.nilai // other.nilai
        
        # Jika objek other bukan merupakan objek FloorDiv,
        # kita asumsikan bahwa other adalah objek lain (tipe data apapun).
        else:
            return self.nilai // other

# membuat objek FloorDiv
obj1 = FloorDiv(10)
obj2 = FloorDiv(2)

# pembagian antara dua objek obj1 dengan obj2 dari kelas FloorDiv
hasil = obj1 // obj2
print(hasil)
# Output:
# 5

# pembagian dengan cara penggunaan magic method __floordiv__()
# Syntax:
# object.__floordiv__(object/value)

# pembagian antara dua objek obj1 dan obj2 dari kelas FloorDiv
hasil = obj1.__floordiv__(obj2)
print(hasil)
# Output:
# 5

# Contoh penggunaan magic method __floordiv__() dengan 2 atribut
class FloorDiv:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __floordiv__(self, other):
        # Jika objek other juga merupakan objek dari kelas FloorDiv 
        if isinstance(other, FloorDiv):
            return FloorDiv(self.x // other.y, self.y // other.y)
        
        # Jika objek other bukan merupakan objek FloorDiv,
        # kita asumsikan bahwa other adalah objek lain (tipe data apapun).
        else:
            return FloorDiv(self.x // other, self.y // other)
    
# membuat objek Floordiv
obj1 = FloorDiv(100, 200)
obj2 = FloorDiv(2, 5)

# pembagian antara dua objek obj1.x dengan obj2.y dari kelas FloorDiv
hasil = obj1.x // obj2.y # 100 // 5
print(hasil)
# Output:
# 20

# pembagian dengan cara penggunaan magic method __floordiv__()
# Syntax:
# object.__floordiv__(object/value)

hasil = obj1.__floordiv__(obj2)
print(hasil.x)  # 100 // 2
# Output:
# 20

print(hasil.y)  # 200 // 5
# Output:
# 40