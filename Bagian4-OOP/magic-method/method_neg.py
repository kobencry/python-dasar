# Magic method __neg__ adalah method khusus dalam Python 
# yang digunakan untuk mengimplementasikan operasi negasi (negatif) dari sebuah objek.
# method ini memungkinkan Anda untuk mendefinisikan perilaku objek ketika diaplikasikan operasi negasi menggunakan operator -.

# method __neg__ harus mengembalikan hasil negasi dari objek tersebut.
# method ini dipanggil ketika Anda menggunakan operator - pada instance objek yang Anda buat.

# Berikut adalah contoh penggunaan method __neg__:

class Negative:
    def __init__(self, nilai):
        self.nilai = nilai

    def __neg__(self):
        return -self.nilai

x = Negative(5)
print(-x)
# Output:
# -5

y = Negative(25.3333)
print(-y)
# Output:
# -25.3333

# Contoh menggunakan type data string
class Reverse:
    def __init__(self, nama):
        self.nama = nama

    def __neg__(self):
        return self.nama[::-1]

x = Reverse("alice")
print(-x)
# Output:
# ecila