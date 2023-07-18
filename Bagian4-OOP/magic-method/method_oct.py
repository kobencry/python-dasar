# Magic method __oct__ adalah method khusus dalam Python 
# yang digunakan untuk mengimplementasikan representasi oktal (basis 8) dari sebuah objek.
# method ini memungkinkan Anda untuk mendefinisikan perilaku objek ketika diubah menjadi 
# representasi oktal menggunakan fungsi bawaan oct().

# method __oct__ harus mengembalikan representasi oktal dari objek dalam bentuk string dengan awalan "0o".
# method ini dipanggil ketika Anda menggunakan fungsi oct() pada instance objek yang Anda buat.

# Berikut adalah contoh penggunaan method __oct__ dalam sebuah kelas:
class NilaiOctal:
    def __init__(self, nilai):
        self.nilai = nilai

    def __oct__(self):
        return oct(self.nilai)

x = NilaiOctal(4)
print(x.__oct__())
# Output:
# 0o4

# menggunakan fungsi bawaan oct()
print(oct(4))
# Output:
# 0o4

y = NilaiOctal(255)
print(y.__oct__())
# Output:
# 0o377

# menggunakan fungsi bawaan oct()
print(oct(255))
# Output:
# 0o377