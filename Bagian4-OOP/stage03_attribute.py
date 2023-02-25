# Attribute adalah hal-hal individual yang membedakan satu objek dari yang lain. 
# Mereka menentukan penampilan, keadaan, atau kualitas lain dari object itu.
# Dalam kasus kami, class 'Mahasiswa' mungkin memiliki attribute berikut:
# nama: alice, carl, eliot
# usia: 23, 20, 25
# alamat: jakarta, bandung, surabaya

# Attribute didefinisikan dalam kelas oleh variabel, 
# dan setiap objek dapat memiliki nilainya sendiri untuk variabel tersebut.
# Ada dua jenis attribute: Instance Attribute dan Class Attribute.

# variabel "Class Attribute" dan variabel "Instance Attribute" merupakan jenis-jenis 
# atribut dalam pemrograman berorientasi objek.
# variabel Class Attribute" adalah atribut yang terkait dengan kelas itu sendiri,
# sedangkan variabel "Instance Attribute" adalah atribut yang terkait dengan suatu objek
# yang diciptakan dari kelas tersebut.

# variabel "Class Attribute" adalah variabel yang dibuat di dalam kelas dan bersifat statis.
# Artinya, nilai variabel "Class Attribute" sama untuk semua objek yang dibuat dari kelas tersebut. 
# variabel "Class Attribute" dapat diakses melalui nama kelas, baik dari dalam maupun luar kelas.

# membuat class Mahasiswa
class Mahasiswa:
    # variabel class attribute
    nama_universitas = "hello world"


# variabel "Instance attribute" adalah variabel yang dibuat di dalam suatu objek yang telah dibuat dari kelas tersebut.
# Setiap objek memiliki salinan variabel instance, yang dapat diubah tanpa memengaruhi objek lain.
# variabel "Instance attribute" hanya dapat diakses melalui objek yang bersangkutan.

# membuat class Mahasiswa
class Mahasiswa:
    # menginisialisasi objek yang dibuat dari class menggunakan constructor __init__()
    def __init__(self, nama, usia, alamat):
        # membuat variabel Instance Attribute
        self.var_nama = nama
        self.var_usia = usia
        self.var_alamat = alamat


# Mengakses Attribute dan Memodifikasi Attribute

# membuat class Mahasisa
class Mahasiswa:
    # variabel class attribute
    nama_universitas = "Oxford"

    # menginisialisasi objek yang dibuat dari class menggunakan constructor __init__()
    def __init__(self, nama, usia, alamat):
        # variabel Instance Attribute
        self.var_nama = nama
        self.var_usia = usia
        self.var_alamat = alamat

# Untuk mengakses variabel "Class Attribute", kita dapat menggunakan nama kelas dan tanda titik 
# contoh "NamaKelas.nama_variabel"

print(Mahasiswa.nama_universitas)
# Output:
# Oxford

# Untuk mengakses variabel "Instance Attribute", kita harus membuat objek dari kelas tersebut, 
# lalu gunakan nama objek dan tanda titik 
# contoh "nama_objek.nama_variabel"
# membuat object
objeku = Mahasiswa("alice", 23, "jakarta") # membuat objek class dengan memanggil nama class dan meneruskan argumen seolah-olah itu adalah fungsi.
print(objeku.var_nama)
print(objeku.var_usia)
print(objeku.var_alamat)
# Output:
# alice
# 23
# jakarta

# Anda bisa juga mengakses variabel "Class Attribute" menggunakan "objeku"
print(objeku.nama_universitas)
# Output:
# Oxford

# ketika Anda membuat objek baru dari kelas di Python, 
# Anda tidak perlu menetapkan argumen "self" secara eksplisit ke method __init__.
# Python secara otomatis mengatur "self" untuk merujuk ke objek yang baru dibuat.
# Dalam contoh yang diberikan, ketika objek "objeku" dibuat dari kelas Mahasiswa, 
# "self" tetap dibuat dan diatur untuk merujuk ke objek yang baru dibuat. 
# Method konstruktor(__init__) kemudian dapat menggunakan "self" untuk 
# mengakses dan mengatur atribut objek seperti nama, usia, dan alamat.

# Untuk memodifikasi variabel "Class Attribute", kita dapat menggunakan nama kelas dan tanda titik 
# lalu mengubah nilainya 
# contoh "NamaKelas.nama_variabel = nilai_baru"
print("-- sebelum --")
print(Mahasiswa.nama_universitas)

Mahasiswa.nama_universitas = "Harvard"
print("-- setelah --")
print(Mahasiswa.nama_universitas)
# Output:
# -- sebelum --
# Oxford
# -- setelah --
# Harvard

# Untuk memodifikasi variabel "Instance Attribute", kita harus membuat objek dari kelas tersebut,
# lalu gunakan nama objek dan tanda titik lalu mengubah nilainya 
# contoh "nama_objek.nama_variabel = nilai_baru"
print("-- sebelum --")
print(objeku.var_nama, objeku.var_usia, objeku.var_alamat)
# mengubah nama, usia, dan alamat
objeku.var_nama = "carl"
objeku.var_usia = 26
objeku.var_alamat = "bandung"
print("-- setelah --")
print(objeku.var_nama, objeku.var_usia, objeku.var_alamat)
# Output:
# -- sebelum --
# alice 23 jakarta
# -- setelah --
# carl 26 bandung

# Anda bisa juga memodifikasi variabel "Class Attribute" menggunakan "objeku"
print("-- sebelum --")
print(f"universitas: {objeku.nama_universitas}")
# mengubah nama universitas
objeku.nama_universitas = "Sydney"
print("-- setelah --")
print(f"universitas: {objeku.nama_universitas}")
# Output:
# -- sebelum --
# universitas: Harvard
# -- setelah --
# universitas: Sydney

# Dalam Python, kelas menggunakan kata kunci class,
# dan objek dibuat menggunakan method konstruktor __init__() yang dipanggil saat objek dibuat.
# Setelah objek dibuat, attribut dapat diakses dan dimodifikasi menggunakan notasi titik.