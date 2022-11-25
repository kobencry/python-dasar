# -- Method Set --

# https://docs.python.org/3/library/stdtypes.html?#frozenset.copy

# fungsi copy() menyalin set.

# Syntax
# set.copy()

# Nilai Parameter
# tidak ada nilai parameter

setku = {'alice', 'carl', 'eliot'}
set_copy = setku.copy()
print(setku)
print(set_copy)

print(setku == set_copy)    # True
