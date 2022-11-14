# -- Method List --

# https://docs.python.org/3/tutorial/datastructures.html?highlight=index#list.index

# fungsi index() mengembalikan posisi pada kemunculan pertama dari nilai yang ditentukan.

# Syntax
# list.index(elemen)

# Nilai Parameter
# Parameter             Deskripsi
# elemen                Dibutuhkan. Jenis apa pun (string, angka, list, dll.). Elemen yang harus dicari

listku = ['alice', 'carl', 'eliot', 'geral']
i = listku.index('geral')
print(i)    # 3

# Catatan: fungsi index() ini hanya mengembalikan kemunculan nilai pertama .

listku = [10, 'x', False, 'x', True, 'x']
print(listku.index('x'))    # 1
i = listku.index('x')
print(i)    # 1 
print(listku[i])    # x

# menggunakan list didalam list atau disebut list bersarang
listku = [2.5, False, ['python', 'x'], True, 3.5, 'x']
print(listku.index('x'))    # 5
print(listku[2].index('x')) # 1
