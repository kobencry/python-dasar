# -- python exception --

# https://docs.python.org/3/library/exceptions.html#ArithmeticError

# ArithmeticError adalah kelas dasar yang menggambarkan kesalahan yang terkait dengan operasi aritmatika,
# seperti pembagian dengan nol atau operasi matematika lainnya yang tidak valid.

# Kelas turunan ArithmeticError meliputi:

# ZeroDivisionError: Ketika mencoba membagi bilangan dengan nol.
# FloatingPointError: Ketika operasi aritmatika floating-point tidak valid dilakukan.
# OverflowError: Ketika hasil operasi aritmatika terlalu besar untuk direpresentasikan dalam tipe data yang diberikan.
# UnderflowError: Ketika hasil operasi aritmatika terlalu kecil untuk direpresentasikan dalam tipe data yang diberikan.
# Semua kelas ini merupakan subclass dari ArithmeticError.

# Berikut ini adalah contoh kode yang menimbulkan ArithmeticError
# dengan pesan kesalahan "division by zero" ketika mencoba melakukan pembagian dengan nol:
try:
    x = 1 / 0
except ArithmeticError as err:
    print("Nama Class Error:", err.__class__)
    print("Pesan Error:", err)
# Output:
# Nama Class Error: <class 'ZeroDivisionError'>
# Pesan Error: division by zero

try:
    x = 100 / 0.0
except ArithmeticError as err:
    print("Nama Class Error:", err.__class__)
    print("Pesan Error:", err)
# Output:
# Nama Class Error: <class 'ZeroDivisionError'>
# Pesan Error: float division by zero