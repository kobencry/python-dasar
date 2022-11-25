# -- Method Set --

# https://docs.python.org/3/library/stdtypes.html?#frozenset.add

# fungsi add() menambahkan elemen ke set.
# jika elemen sudah ada, fungsi add() tidak menambahkan elemen.

# Syntax
# set.add(elemen)

# Nilai Parameter
# Parameter                 Deskripsi
# elemen                    Dibutuhkan. Elemen untuk ditambahkan ke set.

setku = {'alice', 'carl'}
setku.add('eliot')
print(setku)

setku.add(False)
print(setku)
