# -- python exception --

# https://docs.python.org/3/library/exceptions.html#AssertionError
# https://docs.python.org/3/reference/simple_stmts.html#assert

# AssertionError adalah sebuah exception yang digunakan untuk menunjukkan bahwa sebuah assert gagal. 
# Assertion merupakan sebuah pernyataan yang digunakan untuk memastikan bahwa sebuah kondisi tertentu benar.
# Jika kondisi tersebut salah, maka assertion akan gagal dan akan melemparkan exception AssertionError.

def bagi(x, y):
    assert y != 0, "Tidak dapat membagi dengan nol"

    # menghasilkan angka float
    # return x / y
    # menghasilkan int
    return x // y

try:
    print(bagi(10, 2))
    print(bagi(10, 0))
except AssertionError as err:
    print(err)
# Output:
# 5
# Tidak dapat membagi dengan nol

# Ringkasan: 
# Pernyataan assert Python adalah bantuan untuk debugging, bukan mekanisme untuk menangani kesalahan run-time.
# Tujuan penggunaan assertion adalah agar pengembang/developers menemukan kemungkinan akar penyebab bug lebih cepat.
# Kesalahan assertion tidak boleh dimunculkan kecuali ada bug di program Anda.

import sys
try:
    assert ('linux' in sys.platform), 'program ini untuk linux'
    assert ('win32' in sys.platform), 'program ini untuk windows'
except AssertionError as err:
    print(err)
# jika anda menggunakan linux
# Output:
# program ini untuk windows

# jika anda menggunakan windows
# Output:
# program ini untuk linux