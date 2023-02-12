# fungsi map() setara dengan menulis ekspresi generator
def fungsi_map(function, iterable):
    return (function(i) for i in iterable)

# mengubah string huruf kecil menjadi huruf besar
listku = ['alice', 'carl', 'eliot']
x = fungsi_map(str.upper, listku)
print(x)
# Output:
# <generator object fungsi_map.<locals>.<genexpr> at 0x0000012974971E40>

# mengubah fungsi_map menjadi list, agar mudah dibaca
print(list(x))
# Output:
# ['ALICE', 'CARL', 'ELIOT']

# menggunakan fungsi map()
y = list(map(str.upper, listku))
print(y)
# Output:
# ['ALICE', 'CARL', 'ELIOT']

# menghitung panjang setiap kata dalam list
generator = list(fungsi_map(len, listku))
print(generator)
# Output:
# [5, 4, 5]

# kode ini setara dengan diatas karena fungsi map() setara dengan menulis ekspresi generator
generator = list(len(i) for i in listku)
print(generator)
# Output:
# [5, 4, 5]