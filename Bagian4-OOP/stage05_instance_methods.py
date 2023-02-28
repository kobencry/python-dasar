# Instance method adalah metode yang didefinisikan dalam kelas dan 
# dioperasikan pada instance atau objek dari kelas tersebut. 
# Instance method biasanya memiliki satu parameter "self", yang merujuk pada instance saat ini. 
# Instance method dapat mengakses atribut dan method dari instance tersebut dan 
# dapat digunakan untuk memodifikasi nilai atribut instance atau melakukan operasi lain pada instance tersebut. 
# Instance Method pada dasarnya adalah perilaku atau tindakan yang dapat dilakukan oleh objek dari sebuah kelas.

# Contoh instance method pada kelas "Mahasiswa" adalah sebagai berikut:
# display_info: Method ini dapat digunakan untuk menampilkan informasi mahasiswa 
# seperti nama, usia, dan alamat.
# total_info: Method ini dapat digunakan untuk menghitung jumlah mahasiswa.

# membuat class Mahasiswa
class Mahasiswa:
    # variabel Class Attribute
    jumlah = 0
    
    # menginisialisasi objek yang dibuat dari class 'Mahasiswa' menggunakan constructor __init__()
    def __init__(self, nama, usia, alamat):
        # variabel Instance Attribute
        self.var_nama = nama
        self.var_usia = usia
        self.var_alamat = alamat

        # setiap kali objek Mahasiswa dibuat, tambahkan nilai 1 ke variabel Class Attribute: "jumlah"
        Mahasiswa.jumlah += 1
    
    # instance methods
    # Method untuk menampilkan informasi mahasiswa
    def display_info(self):
        return f"nama: {self.var_nama} \nusia: {self.var_usia} \nalamat: {self.var_alamat}"
    
    # instance methods
    # Method untuk menghitung jumlah mahasiswa
    def total_info(self):
        return f"jumlah mahasiswa: {Mahasiswa.jumlah}"

# membuat object 1
alice = Mahasiswa("alice tale", 22, "jakarta")
# menggunakan instance method display_info()
print(alice.display_info())
# Output:
# nama: alice tale
# usia: 22
# alamat: jakarta

# menggunakan instance methods total_info()
print(alice.total_info())
# Output:
# jumlah mahasiswa: 1

# membuat object 2
carl = Mahasiswa("carl liez", 24, "bandung")
print(carl.display_info())
print(carl.total_info())
# Output:
# nama: carl liez
# usia: 24
# alamat: bandung
# jumlah mahasiswa: 2

# mengubah nama menggunakan variabel "Instance attribute"
carl.var_nama = "eliot steal"
print(carl.display_info())
# Output:
# nama: eliot steal
# usia: 24
# alamat: bandung

# Di python ada yang namanya Magic method
# Magic method (metode ajaib) adalah metode bawaan yang disediakan oleh Python 
# dan dimulai dan diakhiri dengan dua garis bawah (__). 
# Metode ini digunakan untuk menentukan perilaku khusus dari objek ketika digunakan dalam operasi khusus,
# seperti pemanggilan fungsi built-in(bawaan), operator, dan built-in konstruktor. 
# Magic method dapat digunakan untuk mengubah perilaku bawaan dari operasi built-in Python 
# atau untuk menambahkan fitur khusus ke objek.
# Jenis-jenis magic method kunjungi folder_name: "magic-method"

# menggunakan Magic method __str__ dan __repr__
# Method __str__ digunakan untuk memberikan representasi string yang mudah dibaca oleh manusia dari objek.
# membuat class Mahasiswa
class Mahasiswa:
    # menginisialisasi objek yang dibuat dari class 'Mahasiswa' menggunakan constructor __init__()
    def __init__(self, nama, usia):
        # variabel instance
        self.var_nama = nama
        self.var_usia = usia
    
    # menggunakan magic method __str__
    def __str__(self):
        return f"nama: {self.var_nama} usia: {self.var_usia}"

# membuat objek
obj_alice = Mahasiswa("alice", 23)
print(obj_alice)
# Output:
# nama: alice usia: 23

# Method __repr__  digunakan untuk memberikan representasi string yang lebih lengkap dan formal dari objek,
# yang juga dapat digunakan untuk merekonstruksi objek.
# Representasi ini ditujukan untuk programmer dan biasanya menampilkan semua detail tentang objek tersebut,
# seperti atribut dan nilai mereka.
# membuat class Mahasiswa
class Mahasiswa:
    # menginisialisasi objek yang dibuat dari class 'Mahasiswa' menggunakan constructor __init__()
    def __init__(self, nama, usia):
        self.var_nama = nama
        self.var_usia = usia
    
    # menggunakan magic method __repr__
    def __repr__(self):
        return f"nama: {self.var_nama} usia: {self.var_usia}"

obj_carl = Mahasiswa("carl", 20)
print(obj_carl)
# Output:
# nama: carl usia: 20

# Anda bisa juga seperti ini
class Mahasiswa:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia
    def __repr__(self):
        return f"nama: {self.nama} usia: {self.usia}"
    def __str__(self):
        return self.__repr__()
x = Mahasiswa('eliot', 23)
print(x)
# Output:
# nama: eliot usia: 23