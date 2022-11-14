# -- Method List --

# https://docs.python.org/3/tutorial/datastructures.html?highlight=reverse#list.reverse

# fungsi reverse() membalikkan urutan pengurutan elemen list.

# Syntax
# list.reverse()

# Nilai Parameter
# tidak ada nilai parameter

listku = ['alice', 'carl', 'eliot', 'geral']
print(listku)   # ['alice', 'carl', 'eliot', 'geral']

listku.reverse()
print(listku)   # ['geral', 'eliot', 'carl', 'alice']

listku = ['carl', 'alice', 'eliot', 'bert']
print(listku)   # ['carl', 'alice', 'eliot', 'bert']

listku.reverse()
print(listku)   # ['bert', 'eliot', 'alice', 'carl']
