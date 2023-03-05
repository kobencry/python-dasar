# Contoh latihan sederhana tentang encapsulasi

# membuat class Mahasiswa
class Mahasiswa:
    # variabel class private
    __jumlah = 0
    
    # menginisialisasi
    def __init__(self, input_nama, input_usia, input_alamat):
        # variabel instance private
        self.__nama = input_nama
        self.__usia = input_usia
        self.__alamat = input_alamat

        # menambahkan jumlah mahasiswa setiap kali object dibuat
        Mahasiswa.__jumlah += 1
    
    # menampilkan data mahasiswa
    def display(self):
        return f"nama: {self.__nama}, usia: {self.__usia}, alamat: {self.__alamat} \nJumlah mahasiswa: {Mahasiswa.__jumlah}"
    
    # Decorator "@property" untuk menandai bahwa method tersebut adalah sebuah property,
    # untuk bisa mengakses fungsi ini seperti atribut, tanpa perlu menggunakan tanda kurung.
    # "property akan dianggap sebagai atribut, dan dapat diakses dan diubah dengan 
    # cara yang sama seperti variabel."
    
    # Getter
    # digunakan untuk mengakses atau mengambil nilai dari atribut
    @property
    def nama(self):
        return self.__nama
    
    @property
    def usia(self):
        return self.__usia
    
    @property
    def alamat(self):
        return self.__alamat
    
    # Setter
    # digunakan untuk mengubah nilai dari atribut
    @nama.setter
    def nama(self, nama_baru):
        self.__nama = nama_baru
    
    @usia.setter
    def usia(self, usia_baru):
        self.__usia = usia_baru
    
    @alamat.setter
    def alamat(self, alamat_baru):
        self.__alamat = alamat_baru
    
# membuat object
alice = Mahasiswa("alice", 22, "jakarta")
print(alice.display())
# Output:
# nama: alice, usia: 22, alamat: jakarta
# Jumlah mahasiswa: 1

# membuat object
carl = Mahasiswa("carl", 25, "bandung")
print(carl.display())
# Output:
# nama: carl, usia: 25, alamat: bandung
# Jumlah mahasiswa: 2

# ubah semua nilai atribut nama, usia, dan alamat
alice.nama = "none"
alice.usia = 0
alice.alamat = "xxx"
print(alice.display())
# Output:
# nama: none, usia: 0, alamat: xxx
# Jumlah mahasiswa: 2

carl.nama = "none"
carl.usia = 0
carl.alamat = "xxx"
print(carl.display())
# Output:
# nama: none, usia: 0, alamat: xxx
# Jumlah mahasiswa: 2