# Encapsulation adalah salah satu konsep utama dalam pemrograman berorientasi objek 
# yang menunjukkan cara membatasi akses ke data dan method dalam sebuah objek. 
# Dalam encapsulasi, atribut dan method dalam sebuah kelas dapat dibuat private, protected, atau public.
# Private dan protected hanya dapat diakses secara internal oleh objek itu sendiri atau turunannya, 
# sedangkan public dapat diakses dari luar objek.
# untuk mengakses dan mengubah variabel private diluar kelas kita butuh "Getter dan Setter"

# Getter dan setter adalah metode dalam OOP yang digunakan untuk 
# mengakses dan mengubah nilai variabel private dalam sebuah class. 
# Getter digunakan untuk mengambil nilai variabel private, sedangkan 
# Setter digunakan untuk mengubah nilai variabel private tersebut.

# Dengan menggunakan encapsulasi, penggunaan data dan method dalam sebuah objek 
# dapat lebih terkendali dan terstruktur.

# membuat class Mahasiswa:
class Mahasiswa:
    # variabel class private
    __universitas = "Oxford"
    
    # menginisialisasi objek
    def __init__(self, nama, usia):
        # variabel instance private
        self.__nama = nama
        self.__usia = usia
    
    # method untuk menampilkan data mahasiswa
    def display_info(self):
        return f"nama:{self.__nama} usia:{self.__usia}"
    
    # method untuk mengakses nilai variabel private:
    # getter
    def getNama(self):
        return self.__nama
    # getter
    def getUsia(self):
        return self.__usia
    
    # method untuk mengubah nilai variabel private:
    # setter
    def setNama(self, nama_baru):
        self.__nama = nama_baru
    # setter
    def setUsia(self, usia_baru):
        self.__usia = usia_baru


# membuat object
mhs = Mahasiswa("alice", 22)
print(mhs.display_info())
# Output:
# nama:alice usia:22

# mengakses nama dan usia dengan encapsulasi "method getNama() dan getUsia()"
print(mhs.getNama())
# Output:
# alice
print(mhs.getUsia())
# Output:
# 22

# mengubah nama dan usia dengan encapsulasi "method setNama() dan setUsia()"
mhs.setNama("Alice stale")
mhs.setUsia(24)
print(mhs.display_info())
# Output:
# nama:Alice stale usia:24

# mengubah nama dan usia dengan cara biasa
mhs.__nama = "hello world"
mhs.__usia = 123
print(mhs.display_info())
# Output:
# nama:alice usia:22

# Ketika mencoba mengubah nilai "__nama" dan "__usia" secara langsung dari luar kelas 
# dengan "mhs.__nama" dan "mhs.__usia", itu sebenarnya tidak mengubah nilai variabel private
# yang sesungguhnya di dalam kelas. 
# Sebaliknya, Python akan membuat dua atribut publik baru pada objek, 
# yang tidak berpengaruh pada variabel private asli di dalam kelas. 
# Oleh karena itu, ketika kita memanggil metode display_info(), 
# kita masih mendapatkan nilai nama dan usia yang asli saat objek dibuat.

# Hal ini disebabkan karena variabel private hanya bisa diakses dan diubah nilainya
# melalui method yang sudah didefinisikan di dalam class, yaitu "Getter dan Setter". 
# Dalam contoh kode di atas, kita bisa mengakses dan mengubah nilai variabel private "nama" melalui method getNama() dan setNama().

print(mhs.__nama)
print(mhs.__usia)
# Output:
# hello world
# 123

# mengubah nilai attribute private "__nama" dan "__usia" di luar class menggunakan cara yang salah,
# sehingga akan membuat attribute baru di luar class dengan nama yang sama namun 
# tidak berhubungan dengan attribute private di dalam class.

# Getter sering juga disebut dengan accessor method.
# Setter sering juga disebut dengan mutator method. 
# Dalam Python, getter dan setter umumnya didefinisikan menggunakan property decorator.