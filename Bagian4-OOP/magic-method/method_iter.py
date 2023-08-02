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
