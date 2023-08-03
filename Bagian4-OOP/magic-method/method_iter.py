# Dalam Python, magic method __iter__ digunakan untuk mengimplementasikan objek sebagai iterator di Python. 
# Iterator adalah objek yang dapat menghasilkan nilai-nilai dalam suatu iterasi atau perulangan. 
# Ketika suatu objek mendukung operasi iterasi (seperti penggunaan dalam loop for), 
# Python akan mencoba untuk memanggil magic method __iter__ pada objek tersebut.

# Deskripsi:
# Magic method __iter__ digunakan untuk mengimplementasikan objek sebagai iterator.
# Saat objek mendukung operasi iterasi (seperti dalam for loop), 
# Python akan mencoba untuk memanggil magic method __iter__ pada objek tersebut.
# Magic method ini harus mengembalikan iterator, yaitu objek yang mendefinisikan metode __next__ 
# untuk menghasilkan nilai-nilai dari objek selama iterasi.

# Syntax:
# def __iter__(self):
    # Implementasikan logika untuk mengembalikan iterator

# Parameter:
# self: Merujuk pada objek saat ini.

# Berikut adalah contoh penggunaan magic method __iter__ dalam sebuah kelas:
class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        # Periksa apakah iterasi sudah selesai
        if self.start >= self.end:
            raise StopIteration

        # Ambil nilai saat ini dan naikkan posisi start
        current_value = self.start
        self.start += 1

        return current_value

# Penggunaan objek iterasi dalam pernyataan for
my_range = Range(1, 5)
for num in my_range:
    print(num)
# Output:
# 