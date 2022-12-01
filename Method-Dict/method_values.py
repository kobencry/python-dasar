# -- Method Dictionary --

# https://docs.python.org/3/library/stdtypes.html?#dict.values

# fungsi values() mengembalikan objek tampilan. 
# Objek tampilan berisi value/nilai dictionary, sebagai tipe data list.

# Objek tampilan akan mencerminkan setiap perubahan yang dilakukan pada dictionary.

# Syntax
# dictionary.values()

# Nilai Parameter
# tidak ada nilai parameter

# mengembalikan value/nilai dalam bentuk tipe data list
dictku = {'nama':'alice', 'usia':23}
x = dictku.values()
print(x)    # dict_values(['alice', 23)

# saat sebuah item dictionary ditambahkan atau diubah nilainya, objek tampilan juga diperbarui.
dictku['alamat'] = 'jakarta'
dictku['nama'] = 'carl'
print(x)        # dict_values(['carl', 23, 'jakarta'])
print(dictku)   # {'nama': 'carl', 'usia': 23, 'alamat': 'jakarta'}

# menampilkan objek dengan forloop
for val in dictku.values():
    print(val)
# carl
# 23
# jakarta
