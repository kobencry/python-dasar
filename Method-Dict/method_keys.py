# -- Method Dictionary --

# https://docs.python.org/3/library/stdtypes.html?#dict.keys

# fungsi keys() mengembalikan objek tampilan.
# Objek tampilan berisi keys/kunci dictionary, sebagai daftar.

# Objek tampilan akan mencerminkan setiap perubahan yang dilakukan pada dictionary.

# Syntax
# dictionary.keys()

# Nilai Parameter
# tidak ada nilai parameter

# mengembalikan keys/kunci dalam bentuk tipe data list
dictku = {'nama':'alice', 'usia':23}
x = dictku.keys()
print(x)    # dict_keys(['nama', 'usia'])

# saat sebuah item dictionary ditambahkan atau diubah nilainya, objek tampilan juga diperbarui.
dictku['alamat'] = 'jakarta'
dictku['nama'] = 'carl'
print(x)        # dict_keys(['nama', 'usia', 'alamat'])
print(dictku)   # {'nama': 'carl', 'usia': 23, 'alamat': 'jakarta'}

# menampilkan objek dengan forloop
for key in dictku.keys():
    print(key)
# nama
# usia
# alamat
