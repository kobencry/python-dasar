# -- python exception --

# Exception Classes adalah kelas yang digunakan untuk membuat jenis-jenis 
# pengecualian atau exception yang spesifik dan dapat dipersonalisasi. 
# Dalam Python, setiap jenis exception memiliki kelas yang berbeda, 
# dan pengguna dapat membuat jenis exception sendiri dengan mewarisi kelas dasar Exception
# dan menambahkan fungsionalitas tambahan sesuai kebutuhan.
# Pengguna juga dapat menentukan pesan kesalahan atau informasi tambahan 
# yang akan ditampilkan saat exception terjadi.

# membuat kelas PesanError sendiri dengan mewarisi semua sifat kelas dasar ValueError
class PesanError(ValueError):
    pass

# fungsi ini memvalidasi panjang password
def protec_password(password):
    if len(str(password)) <= 8:
        raise PesanError(f"(!) password '{password}' kurang panjang coba lagi.")

try:
    protec_password('abc123')
except PesanError as err:
    print(f"Error: {err}")
# Output:
# Error: (!) password 'abc123' kurang panjang coba lagi.

# membuat kelas PesanError sendiri dengan mewarisi semua sifat kelas dasar Exception
# bahwa class Exception memiliki banyak subclass kunjungi file: "Exception_Hierarchy.txt"
class PesanError(Exception):
    # kode program biasa
    # def __init__(self, pesan):
    #     super().__init__(pesan)

    # kode program menggunakan annotation
    def __init__(self, pesan: object) -> None:
        super().__init__(pesan)

def bagi(x, y):
    if y == 0:
        raise PesanError(f"nilai {y} tidak bisa dibagi")
    return x / y

try:
    print(bagi(10, 2))
    print(bagi(10, -2))
    print(bagi(50, 0))
except PesanError as err:
    print(err)
# Output:
# 5.0
# -5.0
# nilai 0 tidak bisa dibagi