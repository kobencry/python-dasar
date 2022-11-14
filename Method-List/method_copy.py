# -- Method List --

# https://docs.python.org/3/tutorial/datastructures.html?highlight=copy#list.copy

# fungsi copy() mengembalikan salinan list yang ditentukan.

# Syntax
# list.copy()

# Nilai Parameter
# tidak ada nilai parameter

listku = ['hello', 2.5, True, 'world', None, 1, False]
x = listku.copy()
print(listku)   # ['hello', 2.5, True, 'world', None, 1, False]
print(x)        # ['hello', 2.5, True, 'world', None, 1, False]

listku = ['hello',[1.5, 2.5], ['world', [True, False]], None]
print(listku)   # ['hello', [1.5, 2.5], ['world', [True, False]], None]
y = listku.copy()
print(y)        # ['hello', [1.5, 2.5], ['world', [True, False]], None]

print(listku == y)  # True
print(listku is y)  # False

listku[0] = 'war'
print(listku)
print(y)

# jika ingin mempelajari lebih lanjut tentang jenis-jenis operator kunjungi folder_name: "python-operator"
