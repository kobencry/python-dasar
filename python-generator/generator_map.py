# fungsi map() setara dengan menulis ekspresi generator
def fungsi_map(function, iterable):
    return (function(i) for i in iterable)

listku = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
generator = fungsi_map(lambda x: x %2==0, listku)
print(generator)
# Output:
# <generator object fungsi_map.<locals>.<genexpr> at 0x0000022254081EB0>

print(list(generator))