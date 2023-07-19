# Magic method __abs__ adalah method khusus dalam Python 
# yang digunakan untuk mengimplementasikan fungsi bawaan abs() untuk sebuah objek dari sebuah kelas. 
# method ini memungkinkan Anda mendefinisikan perilaku dari fungsi abs() 
# ketika diterapkan pada instance kelas yang Anda buat.

# method __abs__ harus mengembalikan nilai absolut dari objek. 
# method ini dipanggil ketika Anda memanggil fungsi abs() pada sebuah instance dari kelas Anda 
# atau ketika Anda menggunakan fungsi abs() bawaan secara langsung pada sebuah objek.

# Berikut adalah contoh penggunaan method __abs__ dalam sebuah kelas:
class Nilai:
    def __init__(self, angka):
        self.angka = angka

    def __abs__(self):
        return abs(self.angka)

x = Nilai(-10)
print(x.__abs__())
# Output:
# 10

# menggunakan fungsi bawaan abs()
print(abs(x))
# Output:
# 10

y = Nilai(1+2j)
print(y.__abs__())
# Output:
# 2.23606797749979

# menggunakan fungsi abs()
print(abs(y))
# Output:
# 2.23606797749979