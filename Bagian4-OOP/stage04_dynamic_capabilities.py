# Dynamic capabilities adalah kemampuan dari suatu bahasa pemrograman
# atau lingkungan komputasi untuk memungkinkan pengguna menambah, mengubah, atau menghapus objek,
# fungsi, atau variabel pada waktu runtime. 
# Dalam hal ini, Python memungkinkan pemrogram untuk menambahkan variabel Instance 
# secara dinamis ke objek individu, yang merupakan salah satu contoh dari 
# dynamic capabilities dalam Python. 
# Dynamic capabilities memungkinkan fleksibilitas dan dinamisme dalam pengembangan perangkat lunak,
# dan memungkinkan pengguna untuk membuat kode yang lebih efisien dan mudah digunakan.

# Berikut ini adalah contoh kode yang menambahkan variabel Instance secara dinamis ke sebuah objek:
# membuat class Mahasiswa
class Mahasiswa:
    # menginisialisasi objek yang dibuat dari class menggunakan constructor __init__()
    def __init__(self, nama):
        # membuat variabel Instance
        self.var_nama = nama

# membuat object
mhs = Mahasiswa("alice")
print(mhs.var_nama)
# Output:
# alice

# menambahkan variabel Instance usia dan alamat secara dinamis
mhs.var_usia = 23
mhs.var_alamat = "jakarta"
print(mhs.var_usia)
print(mhs.var_alamat)
# Output:
# 23
# jakarta

# Pada contoh di atas, variabel Instance usia dan alamat ditambahkan secara dinamis ke objek "mhs"
# setelah objek tersebut dibuat. 
# variabel Instance tersebut tidak didefinisikan pada kelas "Mahasiswa",
# namun bisa ditambahkan pada objek secara langsung. 
# variabel Instance tersebut kemudian bisa diakses dan digunakan seperti variabel Instance lainnya 
# pada objek tersebut.

# Berikut ini adalah contoh kode Python untuk menambahkan fungsi secara dinamis ke sebuah kelas:
def display_info(self):
    print("Info Mahasiswa")
    print(f"nama: {self.var_nama} usia: {self.var_usia} alamat: {self.var_alamat}")

# menambahkan method Instance secara dinamis ke class Mahasiswa
Mahasiswa.obj_fungsi = display_info

# bisa menggunakan fungsi setattr()
# setattr(Mahasiswa, 'obj_fungsi', display_info)

# memanggil method Instance baru
mhs.obj_fungsi()

# Pada contoh di atas, kita menambahkan method instance baru "display_info()" secara dinamis ke kelas "Mahasiswa". 
# Kemudian kita memanggil method instance baru tersebut menggunakan "mhs.display_info()". 
# Dengan dynamic capabilities ini, kita bisa menambahkan fungsi baru ke objek individu sesuai kebutuhan.