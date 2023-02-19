# -- python exception --

# https://docs.python.org/3/library/exceptions.html#FileNotFoundError

# FileNotFoundError adalah sebuah exception yang terjadi ketika sebuah file atau direktori 
# tidak dapat ditemukan di lokasi yang ditentukan. 
# Biasanya exception ini muncul ketika kita mencoba membuka atau membaca sebuah file
# yang tidak ada di sistem atau lokasi yang salah.

# Contoh penggunaan FileNotFoundError adalah ketika kita mencoba membuka sebuah file
# dengan modus baca tetapi file tersebut tidak ditemukan di direktori yang ditentukan.

try:
    with open("file_tidak_ada.txt", mode='r') as f:
        print(f.read())
except FileNotFoundError as err:
    print("Nama Class Error:", err.__class__)
    print("Pesan Error:", err)
# Output:
# Nama Class Error: <class 'FileNotFoundError'>
# Pesan Error: [Errno 2] No such file or directory: 'file_tidak_ada.txt'

# menggunakan pesan error sendiri
try:
    with open("file_tidak_ada.txt", mode='r') as f:
        print(f.read())
# menangkap jenis Error
except FileNotFoundError:
    print("file tidak ada")
# Output:
# file tidak ada