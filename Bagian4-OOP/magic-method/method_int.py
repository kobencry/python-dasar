# Magic method __int__ adalah method khusus dalam Python 
# yang digunakan untuk mengimplementasikan konversi objek menjadi tipe data integer.
# method ini memungkinkan Anda untuk mendefinisikan perilaku konversi objek menjadi
# bilangan bulat saat menggunakan fungsi bawaan int().

# method __int__ harus mengembalikan representasi integer dari objek.
# method ini dipanggil ketika Anda menggunakan fungsi int() pada instance objek yang Anda buat.

# Berikut adalah contoh penggunaan method __int__:

class NilaiInteger:
    def __init__(self, nilai):
        self.nilai = nilai

    def __int__(self):
        return int(self.nilai)

x = NilaiInteger(25.9999999)
print(x.__int__())
# Output:
# 25

# menggunakan fungsi bawaan int()
print(int(x))
# Output:
# 25

y = NilaiInteger(0xff)
print(y.__int__())
# Output:
# 255

# menggunakan fungsi bawaan int()
print(int(0b0101010))
# Output:
# 42
