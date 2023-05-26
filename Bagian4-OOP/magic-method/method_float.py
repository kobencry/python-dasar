# Magic method __float__ adalah method khusus dalam Python 
# yang digunakan untuk mengimplementasikan konversi objek menjadi tipe data float.
# method ini memungkinkan Anda untuk mendefinisikan perilaku konversi objek menjadi
# bilangan desimal saat menggunakan fungsi bawaan float().

# method __float__ harus mengembalikan representasi float dari objek.
# method ini dipanggil ketika Anda menggunakan fungsi float() pada instance objek yang Anda buat.

# Berikut adalah contoh penggunaan method __float__:

class NilaiFloat:
    def __init__(self, nilai):
        self.nilai = nilai

    def __float__(self):
        return float(self.nilai)

x = NilaiFloat(5)
print(x.__float__())
# Output:
# 5.0

# menggunakan fungsi bawaan float()
print(float(5))
# Output:
# 5.0

y = NilaiFloat("25.333")
print(y.__float__())
# Output:
# 25.333

# menggunakan fungsi bawaan float()
print(float("25.333"))
# Output:
# 25.333
