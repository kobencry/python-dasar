# -- Fungsi bawaan python --

# https://docs.python.org/3/library/functions.html#setattr

# fungsi setattr() adalah sebuah fungsi bawaan Python 
# yang digunakan untuk mengatur nilai atribut tertentu dari sebuah objek 
# dengan memberikan nilai baru ke sebuah atribut atau menambahkan atribut baru. 
# Fungsi ini menerima tiga argumen yaitu:
# objek yang akan diubah, 
# nama atribut yang akan diubah atau ditambahkan, dan 
# nilai baru yang akan diberikan. 
# Fungsi ini sangat berguna dalam mengubah atau menambahkan atribut pada objek secara dinamis.

# Syntax
# setattr(object, attribute, value)

# Nilai Parameter
# Parameter                     Deskripsi
# object                        Diperlukan. Sebuah Objek.
# attribute                     Diperlukan. Nama atribut yang ingin Anda atur.
# value                         Diperlukan. Nilai yang ingin Anda berikan pada atribut yang ditentukan.

# membuat class Mahasiswa
class Mahasiswa:
    # menginisialisasi
    def __init__(self, nama, usia):
        # variabel instance
        self.nama = nama
        self.usia = usia
# membuat object
mhs = Mahasiswa("alice", 23)

setattr(Mahasiswa, 'alamat', 'jakarta')
print(mhs.alamat)
# Output:
# jakarta

# menggunakan fungsi
def display_info(self):
    print("info mahasiswa")
    print(f"nama: {self.nama} usia: {self.usia}")

setattr(Mahasiswa, 'obj_fungsi', display_info)
mhs.obj_fungsi()
# Output:
# info mahasiswa
# nama: alice usia: 23