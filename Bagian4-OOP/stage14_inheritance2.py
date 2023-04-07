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
