# Magic method __invert__ digunakan dalam Python untuk melakukan operasi bitwise negasi pada objek.
# Operasi bitwise negasi mengubah setiap bit dalam representasi biner objek menjadi kebalikannya.

# Contoh penggunaan __invert__ pada objek yang mendukung operasi bitwise adalah sebagai berikut:

class Invert:
    def __init__(self, nilai):
        self.nilai = nilai

    def __invert__(self):
        return ~self.nilai

x = Invert(5)
print(~x)
# Output:
# -6
