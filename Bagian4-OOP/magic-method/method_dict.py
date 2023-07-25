# Dalam Python, magic method __dict__ adalah salah satu dari banyak magic method di Python. 
# Magic method ini digunakan untuk mengakses atribut dari sebuah objek dalam bentuk kamus(dictionary). 
# Setiap objek dalam Python memiliki __dict__ yang berisi pasangan kunci-nilai(key-value),
# di mana kunci adalah nama atribut dan nilainya adalah nilai atribut tersebut.

# Deskripsi:
# Magic method __dict__ digunakan untuk mengakses atribut dari sebuah objek dalam bentuk kamus(dictionary).
# Kamus yang dihasilkan berisi semua atribut objek beserta nilainya.
 
# Syntax:
# object.__dict__

# Berikut adalah contoh penggunaan magic method __dict__ dalam sebuah kelas:
class Mahasiswa:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia
    
# membuat objek Mahasiswa
mhs = Mahasiswa("Alice", 20)

# Mengakses atribut objek dalam bentuk kamus(dictionary)
print(mhs.__dict__)
# Output:
# {'nama': 'Alice', 'usia': 20}

# Dalam contoh di atas, kita memiliki kelas Mahasiswa dengan dua atribut, nama dan usia.
# Ketika kita membuat objek mhs dari kelas tersebut, 
# kita dapat mengakses atribut objek dalam bentuk kamus(dictionary) menggunakan magic method __dict__. 
# Hasilnya adalah kamus yang berisi pasangan kunci-nilai dari atribut objek.