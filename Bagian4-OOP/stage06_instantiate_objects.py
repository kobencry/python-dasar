# Selain membuat variabel "Instance attribute", block constructor __init__ 
# juga dapat digunakan untuk melakukan inisialisasi data, 
# melakukan pengaturan awal nilai-nilai default, 
# mengambil nilai dari parameter dan melakukan validasi data. 
# Selain itu, block __init__ juga dapat digunakan untuk menginstansiasi
# objek tambahan atau memanggil metode tambahan yang dibutuhkan saat pembuatan objek.

# Berikut adalah beberapa contoh kode block constructor __init__ 
# yang selain membuat variabel "Instance attribute" juga melakukan operasi lain:

# Berikut ini beberapa contoh kode yang dapat dituliskan di dalam block constructor __init__ 
# selain membuat variabel "Instance attribute":

# Memanggil method instance lainnya
# membuta class Mahasiswa
class Mahasiswa:
    # menginisialisasi objek yang dibuat dari class 'Mahasiswa' menggunakan constructor __init__()
    def __init__(self, nama, usia):
        # variabel instance
        self.var_nama = nama
        self.var_usia = usia
        # memanggil method display_info()
        self.display_info()
    
    # method ini menampilkan info mahasiswa
    def display_info(self):
        print("Contoh memanggil method instance:")
        print(f"nama:{self.var_nama} usia:{self.var_usia}")

# membuat object
mhs = Mahasiswa("alice", 23)
# Output:
# Contoh memanggil method instance
# nama:alice usia:23

# Membuat variabel "Class attribute":
# membuat class mahasiswa
class Mahasiswa:
    # variabel class
    jumlah = 0

    # menginisialisasi objek yang dibuat dari class 'Mahasiswa' menggunakan constructor __init__()
    def __init__(self, nama, usia):
        # variabel instance
        self.nama = nama
        self.usia = usia

        # menginkrementasi variabel class "jumlah" setiap kali objek Mahasiswa dibuat.
        Mahasiswa.jumlah += 1
    
    # manampilkan jumlah mahasiswa
    def total_info(self):
        return f"Jumlah Mahasiswa: {Mahasiswa.jumlah}"

print("Contoh menjumlahkan variabel class:")
# membuat object
alice = Mahasiswa("alice", 22)
print(alice.total_info())
# Output:
# Jumlah Mahasiswa: 1

carl = Mahasiswa("carl", 20)
print(carl.total_info())
# Output:
# Jumlah Mahasiswa: 2

eliot = Mahasiswa("eliot", 25)
print(eliot.total_info())
# Output:
# Jumlah Mahasiswa: 3

# Menginisialisasi variabel "Instance attribute" dengan nilai default:
class Mahasiswa:
    # menginisialisasi
    def __init__(self, nama, usia, alamat=None):
        # variabel instance
        self.var_nama = nama
        self.var_usia = usia
        
        # jika parameter alamat diisi dengan nilai selain None, 
        # maka nilai alamat akan di-set sesuai dengan nilai yang diberikan. 
        if alamat is not None:
            self.var_alamat = alamat
        # Jika parameter alamat tidak diisi atau diisi dengan nilai None,
        # maka nilai alamat akan di-set menjadi "tidak ada"
        else: 
            self.var_alamat = "tidak ada"

    # method ini menampilkan info mahasiswa
    def display_info(self):
        return f"nama:{self.var_nama} usia:{self.var_usia} alamat:{self.var_alamat}"

print("Contoh variabel instance dengan nilai default:")
# membuat object
alice = Mahasiswa("alice", 22, "jakarta")
print(alice.display_info())
# Output:
# nama:alice usia:22 alamat:jakarta

# membuat object
carl = Mahasiswa("carl", 24)
print(carl.display_info())
# Output:
# nama:carl usia:24 alamat:tidak ada

# Melakukan pengecekan atau validasi input:
# membuat class Lingkaran
class Lingkaran:
    # menginisialisasi 
    def __init__(self, jari_jari):
        # Jika nilai jari_jari yang diberikan kurang dari 0, 
        # maka akan muncul ValueError yang menyatakan bahwa jari-jari tidak boleh negatif.
        if jari_jari < 0:
            raise ValueError("Jari-jari tidak boleh negatif")
        # Selain itu, atribut luas akan dihitung berdasarkan rumus luas lingkaran
        # dengan menggunakan nilai jari-jari tersebut.
        # variabel instance
        self.jari_jari = jari_jari
        self.luas = 3.14 * jari_jari ** 2
    
    # method ini menampilkan hasil luas lingkaran 
    def hasil(self):
        return f"Luas lingkaran adalah: {self.luas}"

print("Contoh pengecekan atau validasi input")
# membuat object
x = Lingkaran(5)
print(x.hasil())
# Output:
# Luas lingkaran adalah: 78.5

y = Lingkaran(10)
print(y.hasil())
# Output:
# Luas lingkaran adalah: 314.0

# Kode program yang ditulis di dalam block constructor __init__ 
# selain membuat variabel instance attribute disebut sebagai inisialisasi objek. 
# Pada dasarnya, ini adalah proses untuk mengatur nilai awal dari objek,
# ketika objek dibuat dengan menggunakan class. 
# Inisialisasi objek dapat dilakukan dengan menetapkan nilai awal untuk variabel instance attribute,
# atau dengan melakukan operasi lain pada objek seperti memanggil method atau mengakses variabel class.