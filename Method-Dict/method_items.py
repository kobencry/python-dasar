# -- Method Dictionary --

# https://docs.python.org/3/library/stdtypes.html?#dict.items

# fungsi items() mengembalikan objek tampilan. 
# Objek tampilan berisi pasangan kunci-nilai dictionary, 
# sebagai tipe data list yang berisi tipe data tupel.
# Objek tampilan akan mencerminkan setiap perubahan yang dilakukan pada dictionary.

# Syntax
# dictionary.items()

# Nilai Parameter
# tidak ada nilai parameter

# mengembalikan keys/kunci dan value/nilai 
dictku = {'nama':'alice', 'usia':23}
x = dictku.items()
print(x)    # dict_items([('nama', 'alice'), ('usia', 23)])

# saat sebuah item dictionary ditambahkan atau diubah nilainya, objek tampilan juga diperbarui.
dictku['alamat'] = 'jakarta'    # menambahkan
dictku['nama'] = 'carl'         # mengubah
print(x)        # dict_items([('nama', 'alice'), ('usia', 23), ('alamat', 'jakarta')])
print(dictku)   # {'nama': 'carl', 'usia': 23, 'alamat': 'jakarta'}

# menampilkan objek dengan forloop
for key, val in dictku.items():
    print(key, val)
# nama alice
# usia 23
# alamat jakarta
