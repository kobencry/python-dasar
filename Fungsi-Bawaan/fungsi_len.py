# -- Fungsi bawaan python --
# fungsi len() mengembalikan jumlah item dalam suatu objek.
# ketika objek adalah string, fungsi len() mengembalikan jumlah karakter dalam string.

# Syntax
# len(objek)

# Nilai Parameter
# Parameter         Deskripsi
# objek             Dibutuhkan. Sebuah Objek. Harus berupa urutan atau kumpulan

# menggunakan string
print(len(""))  # 0
s = "hello world"
total = len(s)
print(total)    # 11

# menggunakan list
print(len([]))  # 0
l = ['alice', 10, 'carl', True, 'eliot', None]
total = len(l)
print(total)    # 6

# menggunakan tuple
print(len(()))  # 0
t = ('alice', 20, 'carl', False, 'eliot', None)
total = len(t)
print(total)    # 6

# menggunakan dict
d = {'a':'alice', 'b':5.10, 'c':'carl', 'd':None, 'e':'eliot'}
total = len(d)  # tipe dict yang di jumlahkan key
print(total)    # 5
# jika anda ingin menjumlahkan val 
print(len(d['a'])) # 5
print(len(['b']))  # 1

print(len("🤨"))   # 1
print(len(range(10)))   # 10
# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan range() kunjungi folder_name: "Fungsi-Bawaan/fungsi_range.py"
