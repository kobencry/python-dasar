# -- python exception --

# ZeroDivisionError adalah jenis exception yang terjadi ketika kita mencoba membagi angka dengan nol.
# Exception ini umumnya terjadi ketika kita melakukan operasi pembagian dan denominator atau pembagi yang digunakan adalah nol.

try:
    print(10 / 0)
except ZeroDivisionError as err:
    print("Nama Class Error:", err.__class__)
    print("Pesan Error:", err)
# Output:
# Nama Class Error: <class 'ZeroDivisionError'>
# Pesan Error: division by zero

# membuat fungsi bagi
def bagi(x, y):
    return x / y
# menggunakan pesan error sendiri
try:
    print(bagi(50, 0))
# menangkap jenis Error
except ZeroDivisionError:
    print("tidak bisa dibagi dengan angka nol.")
# Output:
# tidak bisa dibagi dengan angka nol.