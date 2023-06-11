# Magic method __truediv__ adalah method khusus dalam Python 
# yang digunakan untuk mendefinisikan perilaku operasi pembagian sejati (/) antara objek. 
# Ketika kita menggunakan operator / antara dua objek, 
# Python akan mencari dan menggunakan method __truediv__ untuk menentukan hasil pembagian tersebut.

# Ketika method __truediv__ didefinisikan dalam sebuah kelas, 
# kita dapat mengontrol bagaimana objek dari kelas tersebut berperilaku saat dibagi dengan objek lain.
# Kita dapat mengimplementasikan method __truediv__ untuk melakukan operasi pembagian sejati 
# sesuai dengan kebutuhan aplikasi atau kelas yang kita definisikan.

# Berikut adalah contoh sederhana untuk mendemonstrasikan penggunaan method __truediv__ dalam Python:

class TrueDiv:
    def __init__(self, nilai):
        self.nilai = nilai

    def __truediv__(self, other):
        return TrueDiv(self.nilai / other.nilai)

# membuat objek TrueDiv
obj1 = TrueDiv(10)
obj2 = TrueDiv(2)

# membagi antara dua objek obj1 dengan obj2
hasil = obj1 / obj2
print(hasil.nilai)
# Output:
# 5.0


        
