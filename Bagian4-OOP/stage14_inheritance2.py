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