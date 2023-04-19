class A:
    # method instance
    def display(self):
        return "hello"

class B(A):
    # method instance
    def display(self):
        return f"{super().display()} world"

# membuat object
b = B()
print(b.display())

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
