# fungsi map() setara dengan menulis ekspresi generator
def fungsi_map(function, iterable):
    return (function(i) for i in iterable)

# mengubah string huruf kecil menjadi huruf besar
listku = ['alice', 'carl', 'eliot']
generator = fungsi_map(str.upper, listku)
print(generator)
# Output:
# <generator object fungsi_map.<locals>.<genexpr> at 0x0000012974971E40>

print(list(generator))
# Output:
# ['ALICE', 'CARL', 'ELIOT']

# mengubah string huruf kecil menjadi huruf besar menggunakan fungsi map()
generator = list(map(str.upper, listku))
print(generator)
# Output:
# ['ALICE', 'CARL', 'ELIOT']

# menghitung panjang setiap kata dalam list
generator = list(fungsi_map(len, listku))
print(generator)
# Output:
# [5, 4, 5]