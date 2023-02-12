# fungsi filter() setara dengan menulis ekspresi generator
def fungsi_filter(function, iterable):
    return (i for i in iterable if function(i))

# mencari nilai bilangan genap
listku = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = fungsi_filter(lambda n: n %2==0, listku)
print(x)
# Output:
# <generator object fungsi_filter.<locals>.<genexpr> at 0x0000025CD4641F20>

print(list(x))
# Output:
# [2, 4, 6, 8, 10]

# menggunakan fungsi filter()
y = list(filter(lambda n: n %2==0, listku))
print(y)
# Output:
# [2, 4, 6, 8, 10]

