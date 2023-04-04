# Inheritance (pewarisan atau sifat pewarisan) pada Python adalah konsep di mana sebuah
# kelas baru dibuat dengan memperluas fungsionalitas kelas yang sudah ada. 
# Dalam pewarisan, kelas baru didefinisikan dengan menggunakan kelas 
# yang sudah ada sebagai landasan atau superclass, sehingga kelas baru dapat 
# mewarisi atribut dan method dari superclass.

# Dengan menggunakan inheritance, kita dapat membuat hierarki kelas
# yang lebih mudah dikelola dan memungkinkan kita untuk menghindari 
# duplikasi kode dan meningkatkan modularitas dan fleksibilitas kode. 
# Di Python, pewarisan dilakukan dengan menempatkan nama kelas induk 
# dalam kurung setelah nama kelas turunan.

# Berikut adalah contoh sederhana inheritance pada Python:
class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        return f"x: {self.x}, y: {self.y}"

class B(A):
    def __init__(self, x, y, z):
        #self.x = x
        #self.y = y
        A.__init__(self, x, y)
        self.z = z

    def display(self):
        return f"info: {self.x}, {self.y}, {self.z}"
a = A(100, 200)
print(a.display())
# Output:
# x: 100, y: 200

b = B(2, 4, 6)
print(b.display())
# Output:
# info: 2, 4, 6