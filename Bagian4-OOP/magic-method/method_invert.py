# Magic method __invert__ digunakan dalam Python untuk melakukan operasi bitwise negasi pada objek.
# Operasi bitwise negasi mengubah setiap bit dalam representasi biner objek menjadi kebalikannya.

# Berikut adalah contoh penggunaan magic method __invert__ dalam sebuah kelas:
class Invert:
    def __init__(self, nilai):
        self.nilai = nilai

    def __invert__(self):
        return ~self.nilai

# membuat objek Invert
x = Invert(5)
print(~x)
# Output:
# -6

# contoh ilustrasi tentang operator bitwise NOT atau ~ (Negasi/Kebalikan)
# sebelum 
print(f"{5:08b}") # 00000101
# sesudah
print(f"{~5:08b}") # -0000110
print(int('-0000110', base=2)) # -6

# Perlu dicatat bahwa penggunaan magic method __invert__ tergantung pada tipe objek yang Anda definisikan.
# Tidak semua objek mendukung operasi bitwise dan tidak semua objek memiliki magic method __invert__.