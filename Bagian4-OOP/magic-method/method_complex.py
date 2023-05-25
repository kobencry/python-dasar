# Magic method __complex__ adalah method khusus dalam Python 
# yang digunakan untuk mengimplementasikan konversi objek menjadi tipe data kompleks (complex).
# method ini memungkinkan Anda untuk mendefinisikan perilaku konversi objek menjadi bilangan kompleks saat menggunakan fungsi bawaan complex().

# magic method __complex__ harus mengembalikan representasi kompleks dari objek dalam bentuk bilangan kompleks.
# method ini dipanggil ketika Anda menggunakan fungsi complex() pada instance objek yang Anda buat.

# Berikut adalah contoh penggunaan method __complex__:
class Nilai:
    def __init__(self, bilangan_real, bilangan_imajiner):
        self.bilangan_real = bilangan_real
        self.bilangan_imajiner = bilangan_imajiner

    def __complex__(self):
        return complex(self.bilangan_real, self.bilangan_imajiner)

x = Nilai(2, 3)
print(x.__complex__())
# Output:
# (2+3j)

# menggunakan fungsi complex()
print(complex(x))
# Output:
# (2+3j)

y = Nilai(-5, 2+3j)
print(y.__complex__())
# Output:
# (-8+2j)

# menggunakan fungsi complex()
print(complex(y))
# Output:
# (-8+2j)
