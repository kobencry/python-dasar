# Polymorphism pada Python adalah kemampuan sebuah objek untuk memiliki banyak bentuk atau tampilan yang berbeda, 
# tergantung pada konteksnya. 
# Polymorphism memungkinkan objek untuk memiliki perilaku yang berbeda saat berinteraksi dengan objek yang berbeda pula.

# Di Python, polymorphism dapat dicapai dengan menggunakan teknik seperti operator overloading, 
# method overloading, dan method overriding. 
# Operator overloading memungkinkan operator standar seperti + dan - dapat digunakan pada objek-objek yang kita definisikan sendiri. 
# Method overloading memungkinkan sebuah kelas memiliki beberapa method dengan nama yang sama, 
# namun memiliki parameter yang berbeda. 
# Method overriding memungkinkan kelas turunan untuk menimpa method yang sama pada kelas induk dengan implementasi yang berbeda.

# Polymorphism sangat penting dalam OOP karena memungkinkan kode kita lebih fleksibel dan modular. 
# Dengan menggunakan polymorphism, kita dapat memanfaatkan abstraksi dan pewarisan(inheritance) pada kelas 
# untuk membuat kode yang lebih efisien dan mudah di-maintain. 
# Polymorphism juga dapat meningkatkan reusabilitas kode, 
# karena objek yang sama dapat memiliki perilaku yang berbeda dalam konteks yang berbeda.

# Berikut adalah contoh sederhana penggunaan polymorphism di Python pada kelas Hewan
class Hewan:
    def suara(self):
        pass

class Anjing(Hewan):
    def suara(self):
        print("guk guk")

class Kucing(Hewan):
    def suara(self):
        print("meow")

class Ayam(Hewan):
    def suara(self):
        print("kukuruyuk")

anjing = Anjing()
kucing = Kucing()
ayam = Ayam()

for x in (anjing, kucing, ayam):
    # memanggil metode suara dari masing-masing objek
    x.suara()
# Output:
# guk guk
# meow
# kukuruyuk