# -- Method String --

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi join() mengambil semua item dalam iterable dan menggabungkannya menjadi satu string.
# Sebuah string harus ditentukan sebagai pemisah.

# Syntax
# string.join(iterable)

# Nilai Parameter
# Parameter         Deskripsi
# iterable          Dibutuhkan. Objek apa pun yang dapat diubah di mana semua nilai yang dikembalikan adalah string

# Catatan: 
# Saat menggunakan dict sebagai iterable, nilai yang dikembalikan adalah kuncinya/keys, bukan nilainya/values.

# menggunakan tipe data string
s = "hello world"
x = "#".join(s)
print(x)    # h#e#l#l#o# #w#o#r#l#d
print("-".join("12.030")) # 1-2-.-0-3-0

# menggunakan tipe data list
l = ['alice', 'carl', 'eliot']
x = " -> ".join(l)
print(x)    # alice -> carl -> eliot
print("-".join(['1', '2.0', '30'])) # 1-2.0-30
print(",".join(*['alice', 'carl', 'eliot']))

# menggunakan tipe data tuple
t = ('usr', 'bin', 'python')
x = "/".join(t)
print(x)    # usr/bin/python
print("-".join(('1', '2.0', '30'))) # 1-2.0-30

# menggunakan tipe data dict
# Catatan: 
# Saat menggunakan dict sebagai iterable, nilai yang dikembalikan adalah kuncinya/keys, bukan nilainya/values.
d = {'nama':'alice', 'usia':'23', 'email':'alice@gmail.com'}
x = ":".join(d)
print(x)    # nama:usia:email
print(":".join(d.values())) # alice:23:alice@gmail.com

# Berhati-hatilah jika anda memiliki iterabel yang memiliki ukuran/item 1
print("b".join('a'))    # a
print("b".join(['a']))  # a
print("b".join(('a')))  # a
# fungsi join() sangat cerdas karena menyisipkan item/data anda di antara string iterable yang ingin anda ikuti,
# ini berarti bahwa jika anda melewati iterable ukuran/item 1,
# anda tidak akan melihat fungsi join()
print("b".join('ac'))       # abc
print("b".join(['a', 'c'])) # abc
print("b".join(('a', 'c'))) # abc
