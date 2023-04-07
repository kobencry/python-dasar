# contoh kasus inheritance pada parameter superclass dan subclass

#------------------------------------------
# contoh superclass memiliki tiga parameter dan subclass memiliki 2 parameter
# parameter superclass: nama, usia, email
# parameter subclass: nama, usia
#------------------------------------------

# menggunakan parameter default "nilainya bisa (string, int, boolean, list, tuple, dictionary, dll.)"
class A: # superclass
    def __init__(self, nama, usia, email=None):
        self.__nama = nama
        self.__usia = usia
        self.__email = email
    
    def display(self):
        return f"{self.__nama}, {self.__usia}, {self.__email}"

class B(A):
    def __init__(self, nama, usia):
        super().__init__(nama, usia)
    
    def info(self):
        return f"{super().display()}"

a = A("alice", 20, "alice@gmail.com")
print(a.display())
# Output:
# alice, 20, alice@gmail.com

b = B("carl", 25)
print(b.info())
# Output:
# carl, 25, None
# Karena tidak ada nilai email yang diberikan pada constructor "class B", 
# maka nilai email pada objek b diisi dengan None saat constructor "class A" dipanggil menggunakan super().__init__(nama, usia).

# jika anda tidak ingin menggunakan parameter default
class A: # superclass
    def __init__(self, nama, usia, email):
        self.__nama = nama
        self.__usia = usia
        self.__email = email
    
    def display(self):
        return f"{self.__nama}, {self.__usia}, {self.__email}"

# Dalam "class B", pada saat memanggil method __init__() menggunakan fungsi super(),
# yang berarti variabel nama dan usia diwariskan dari "class A" ke "class B" dan 
# variabel email diisi dengan nilai None atau "apapun" bisa (string, int, boolean, list, tuple, dictionary, dll.)
class B(A): # subclass
    def __init__(self, nama, usia):
        # variabel instance
        #super().__init__(nama, usia, 2)  #int
        #super().__init__(nama, usia, False) #boolean
        #super().__init__(nama, usia, ['a', 'b', 'c']) #list
        super().__init__(nama, usia, None)

    def info(self):
        return f"{super().display()}"
a = A("alice", 20, "alice@gmail.com")
print(a.display())
# Output:
# alice, 20, alice@gmail.com

b = B("carl", 25)
print(b.info())
# Output:
# carl, 25, None

# jika parameter emailnya berada di awal:
class A: # superclass
    def __init__(self, email, nama, usia):
        self.__email = email
        self.__nama = nama
        self.__usia = usia
    def display(self):
        return f"{self.__email}, {self.__nama}, {self.__usia}"
class B(A): # subclass
    def __init__(self, nama, usia):
        super().__init__(None, nama, usia)
    
    def info(self):
        return f"{super().display()}"

a = A("alice@gmail.com", "alice", 20)
print(a.display())
# Output:
# alice@gmail.com, alice, 20

b = B("carl", 25)
print(b.info())
# Output:
# None, carl, 25
# Anda bisa menyesuaikan posisi parameter dari superclass yang tidak ada di subclass.

#------------------------------------------
# contoh superclass memiliki 3 parameter dan subclass memiliki 3 parameter
# dengan nama parameter yang berbeda
# parameter superclass: nama, usia, email
# parameter subclass: nama, usia, alamat
#------------------------------------------
# sebenarnya contoh ini sama dengan diatas

# menggunakan parameter default "nilainya bisa (string, int, boolean, list, tuple, dictionary, dll.)"
class A: # superclass
    def __init__(self, nama, usia, email=None):
        # variabel instance
        self.__nama = nama
        self.__usia = usia
        self.__email = email
    
    # method instance
    def display(self):
        return f"{self.__nama}, {self.__usia}, {self.__email}"

class B(A): # subclass
    def __init__(self, nama, usia, alamat):
        # variabel instance
        super().__init__(nama, usia)
        self.__alamat = alamat
    
    # method instance
    def info(self):
        return f"{super().display()}, {self.__alamat}"

a = A("alice", 20, "alice@gmail.com")
print(a.display())
# Output:
# alice, 20, alice@gmail.com

b = B("carl", 25, "jakarta")
print(b.info())
# Output:
# carl, 25, None, jakarta

#------------------------------------------
# Contoh tambahan:
# Junior: Saya tidak ingin outputnya ada None bagaimana caranya?
# Senior: Karna outputnya bertipe "string" ada 4 metode cara menghapus string: strip(), translate(), regex, forloop

# menggunakan method string strip() kunjungi folder: "Method-String/method_strip.py"
# yang 3 metode diatas "PR" buat anda

class A: # superclass
    def __init__(self, nama, usia, email):
        # variabel instance
        self.__nama = nama
        self.__usia = usia
        self.__email = email
    
    # method instance
    def display(self):
        return f"{self.__nama}, {self.__usia}, {self.__email}"

class B(A): # subclass
    def __init__(self, nama, usia, alamat):
        # variabel instance
        super().__init__(nama, usia, None)
        self.__alamat = alamat
    
    # method instance
    def info(self):
        # print(type(super().display()))  #output: <class 'str'>
        # Perlu diingat bahwa string di Python bersifat immutable, 
        # sehingga ketika melakukan penghapusan karakter pada string 
        # akan menghasilkan string baru yang harus disimpan ke dalam variabel baru 
        # atau mengganti variabel lama dengan variabel yang baru.
        hasil = super().display().strip("None, ")
        return f"{hasil}, {self.__alamat}"
a = A("alice", 20, "alice@gmail.com")
print(a.display())
# Output:
# alice, 20, alice@gmail.com

b = B("carl", 25, "jakarta")
print(b.info())
# Output:
# carl, 25, jakarta

# menggunakan regex kunjungi folde_name: "modul-re"
import re # library bawaan python

class A:
    def __init__(self, nama, usia, email):
        # variabel instance
        self.__nama = nama
        self.__usia = usia
        self.__email = email
    
    # method instance
    def display(self):
        return f"{self.__nama}, {self.__usia}, {self.__email}"

class B(A): # subclass
    def __init__(self, nama, usia, alamat):
        # variabel instance
        super().__init__(nama, usia, None)
        self.__alamat = alamat
    
    # method instance
    def info(self):
        stringku = f"{super().display()}, {self.__alamat}"
        regex = "None, "
        hasil = re.sub(regex, "", stringku)
        return hasil

b = B("eliot", 30, "bandung")
print(b.info())
# Output:
# eliot, 30, bandung