# Dalam Python, magic method __ge__() adalah method khusus yang digunakan untuk mengimplementasikan operator >= "lebih besar atau sama dengan" pada suatu objek. 
# method ini memungkinkan Anda untuk menentukan perilaku perbandingan antara dua objek, 
# di mana objek pertama lebih besar atau sama dengan objek kedua.

# Ketika operator >= digunakan untuk membandingkan dua objek,
# Python secara otomatis memanggil method __ge__() pada objek yang pertama,
# dan mengirimkan objek kedua sebagai argumen. 
# method ini harus mengembalikan nilai True jika objek tersebut lebih besar atau sama dengan objek kedua,
# dan False jika objek tersebut lebih kecil.

# Deskripsi:
# method __ge__() digunakan untuk mengimplementasikan operator >= "lebih besar atau sama dengan". 
# method ini harus mengembalikan nilai True jika objek saat ini lebih besar atau sama dengan objek kedua,
# dan False jika objek saat ini lebih kecil.

# Syntax:
# def __ge__(self, other)
#   Implementasi logika perbandingan

# Parameter:
# self: Merujuk pada objek saat ini.
# other: Merupakan objek kedua yang dibandingkan dengan objek saat ini.
# nama parameter "other" bisa diganti dengan nama apapun

# Contoh penggunaan magic method __ge__():
class Mahasiswa:
    def __init__(self, nilai):
        self.nilai = nilai

    def __ge__(self, other):
        # Jika objek other juga merupakan objek dari kelas Mahasiswa 
        if isinstance(other, Mahasiswa):
            return self.nilai >= other.nilai

        # Jika objek other bukan merupakan objek Mahasiswa, 
        # kita asumsikan bahwa other adalah bilangan bulat atau bilangan desimal.
        else:
            return self.nilai >= other

# membuat objek Mahasiswa
mhs1 = Mahasiswa(30)
mhs2 = Mahasiswa(20)

# membandingkan antara dua objek mhs1 dengan mhs2 dari kelas Mahasiswa
hasil = mhs1 >= mhs2
print(hasil)
# Output:
# True

hasil = mhs2 >= mhs1
print(hasil)
# Output:
# False

# membandingkan antara objek mhs1 dengan bilangan bulat 
hasil = mhs1 >= 30
print(hasil)
# Output:
# True

# membandingkan dengan cara penggunaan magic method __ge__()
# Syntax:
# object.__ge__(object/value)

hasil = mhs1.__ge__(mhs2)
print(hasil)
# Output:
# True

hasil = mhs2.__ge__(mhs1)
print(hasil)
# Output:
# False

# membandingkan antara objek mhs1 dengan value "bilangan bulat"
hasil = mhs1.__ge__(20)
print(hasil)
# Output:
# True