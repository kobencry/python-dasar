# Dalam Python, magic method __hex__ adalah method khusus dalam Python 
# yang digunakan untuk mengimplementasikan representasi heksadesimal dari sebuah objek.
# method ini memungkinkan Anda untuk mendefinisikan perilaku objek ketika 
# diubah menjadi representasi heksadesimal menggunakan fungsi bawaan hex().

# method __hex__ harus mengembalikan representasi heksadesimal dari objek dalam bentuk string dengan awalan "0x".
# method ini dipanggil ketika Anda menggunakan fungsi hex() pada instance objek yang Anda buat.

# Berikut adalah contoh penggunaan magic method __hex__ dalam sebuah kelas:
class NilaiHexa:
    def __init__(self, nilai):
        self.nilai = nilai
    
    def __hex__(self):
        return hex(self.nilai)

# membuat objek NilaiHexa
x = NilaiHexa(255)
print(x.__hex__())
# Output:
# 0xff

# menggunakan fungsi bawaan hex()
print(hex(255))
# Output:
# 0xff

# membuat objek NilaiHexa
y = NilaiHexa(192)
print(y.__hex__())
# Output:
# 0xc0

# menggunakan fungsi bawaan hex()
print(hex(168))
# Output:
# 0xa8