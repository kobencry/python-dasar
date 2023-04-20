# Overriding adalah suatu konsep dalam pemrograman berorientasi objek (OOP) 
# di mana sebuah subclass memiliki fungsi/method dengan nama yang sama seperti method yang didefinisikan di superclassnya.
# Saat method yang di-override dipanggil pada objek dari subclass, 
# maka method yang ada di subclass akan dipanggil bukan "method yang ada di superclass".

# Di Python, overriding dapat dilakukan dengan mendefinisikan ulang method di subclass 
# dengan nama yang sama dengan method yang ada di superclass. 
# Ketika sebuah objek dari subclass dipanggil dengan method yang di-override, 
# Python akan mencari method yang sesuai di subclass dan menjalankannya. 
# Jika method tidak ditemukan di subclass, Python akan mencari di superclassnya.

# Berikut adalah contoh pertama sederhana overriding di Python:
class A: #superclass
    # method instance
    def display(self):
        return "hello alice"

class B(A): #subclass
    # method instance
    def display(self):
        return "hello carl"
# membuat object
a = A()
print(a.display())
# Output:
# hello alice

# membuat object
b = B()
print(b.display())
# Output
# hello carl 

# penjelasan:
# Pada contoh di atas, "class B" mewarisi(inheritance) "class A". 
# Kemudian, "class B" mendefinisikan ulang method display() dengan implementasi yang berbeda.
# Ketika method display() dipanggil pada objek a, 
# Python akan menemukan method yang ada di "class A" dan menjalankannya.
# Sedangkan ketika method display() dipanggil pada objek b, 
# Python akan menemukan method yang ada di "class B" dan menjalankannya, sehingga outputnya berbeda.

# Berikut adalah contoh kedua sederhana overriding di Python:
class A: #superclass
    # method instance
    def display(self):
        return "hello"

class B(A): #subclass
    # method instance
    def display(self):
        return f"{super().display()} world"

# membuat object
a = A()
print(a.display())
# Output
# hello

b = B()
print(b.display())
# Output
# hello world

# Berikut adalah contoh sederhana overriding di Python:
class A: #superclass
    def __init__(self, nama, usia):
        # variabel instance
        self.__nama = nama
        self.__usia = usia

    # method instance
    def display(self):
        return f"{self.__nama}, {self.__usia}"

class B(A): #subclass
    def __init__(self, nama, usia, alamat):
        # variabel instance
        super().__init__(nama, usia)
        self.__alamat = alamat

    # method instance
    def display(self):
        return f"{super().display()}, {self.__alamat}"

a = A('alice', 20)
print(a.display())
# Output:
# alice, 20

# membuat object
b = B('carl', 25, 'bandung')
print(b.display())
# Output:
# carl, 25, bandung
