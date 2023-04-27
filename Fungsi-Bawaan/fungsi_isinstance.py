# -- Fungsi bawaan python --
# fungsi isinstance() adalah fungsi bawaan (built-in) pada Python 
# yang digunakan untuk memeriksa apakah sebuah objek termasuk dalam suatu tipe data tertentu atau tidak.

# fungsi isinstance() mengambil dua parameter, 
# yaitu objek yang akan diperiksa dan tipe data yang akan dibandingkan. 
# Fungsi ini akan mengembalikan nilai True jika objek tersebut merupakan instance dari tipe data yang diberikan, 
# dan mengembalikan nilai False jika sebaliknya

# Syntax
# isinstance(object, type)

# Nilai Parameter
# Parameter                    Deskripsi
# objek                        Dibutuhkan. Sebuah Objek.
# type                         Sebuah tipe atau kelas, atau kumpulan tipe dan/atau kelas

x = 5
print(isinstance(x, int))
# Output:
# True

y = "hello world"
print(isinstance(y, str))
# Output:
# True

z = ['hello', 'world']
print(isinstance(z, (tuple, dict, list, int, str, bool)))
# Output:
# True