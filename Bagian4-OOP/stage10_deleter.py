# Deleter pada konsep encapsulation pada Python adalah sebuah method atau fungsi 
# khusus yang digunakan untuk menghapus suatu atribut pada sebuah objek. 
# Deleter merupakan bagian dari konsep property dalam Python, 
# yang memungkinkan kita untuk mengimplementasikan getter, setter dan deleter pada sebuah atribut 
# agar dapat diakses dan dimodifikasi secara aman dan sesuai dengan prinsip encapsulation.

# Dalam konsep property pada Python, deleter dapat diimplementasikan dengan menggunakan
# decorator "@<nama_atribut>.deleter". 
# Fungsi deleter yang didekorasi dengan cara tersebut akan dijalankan ketika kita mencoba
# untuk menghapus sebuah atribut dari objek tersebut.
# Berikut adalah contoh implementasi deleter pada sebuah kelas dalam Python:
# membuat class Mahasiswa
class Mahasiswa:
    # menginisialisasi
    def __init__(self, input_nama):
        # variabel instance menjadi private "variabel tersebut tidak bisa diakses dari luar kelas"
        self.__nama = input_nama
    
    # Getter
    @property
    def nama(self):
        return self.__nama
    
    # Setter
    @nama.setter
    def nama(self, nama_baru):
        self.__nama = nama_baru
    
    # Deleter
    @nama.deleter
    def nama(self):
        del self.__nama

    # magic method __str__ digunakan untuk memberikan representasi string 
    # yang mudah dibaca oleh manusia dari objek.
    def __str__(self) -> str:
        return f"private: {self.__nama} \ngetter: {self.nama}"

# membuat object
mhs = Mahasiswa("alice")

# anda bisa menampilkan object "mhs" karna kelas Mahasiswa menggunakan magic method __str__
print(mhs)
# Output:
# private: alice
# getter: alice

# akses nilai variabel private __nama diluar kelas dengan method getter "mhs.nama"
# anda bisa mengakses method ini seperti atribut, tanpa perlu menggunakan tanda kurung.
print(mhs.nama)
# Output:
# alice

# ubah nilai variabel private __nama diluar kelas dengan method setter "mhs.nama"
# anda bisa mengubah method ini seperti atribut, tanpa perlu menggunakan tanda kurung.
mhs.nama = "hello world"
print(mhs.nama)
# Output:
# hello world

print(mhs)
# Output:
# private: hello world
# getter: hello world

# menghapus atribut "nama" pada object "mhs"
del mhs.nama

try:
    print(mhs)
except AttributeError as err:
    print(err)
# Output:
# 'Mahasiswa' object has no attribute '_Mahasiswa__nama'
# Hasilnya, ketika kita mencoba untuk mengakses atribut "nama" lagi pada objek "mhs", 
# maka Python akan menghasilkan error AttributeError karena atribut "nama" telah dihapus.

# membuat object
mhs2 = Mahasiswa('carl')
# akses dengan object "mhs2"
print(mhs2)
# Output:
# private: carl
# getter: carl

# akses atribut "nama" dari object "mhs2"
print(mhs2.nama)
# Output:
# carl