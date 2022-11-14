# -- Method List --

# https://docs.python.org/3/tutorial/datastructures.html?highlight=sort#list.sort

# fungsi sort() mengurutkan list secara alfanumerik (0-9A-Za-z), default/standarnya ascending/menaik.

# Syntax
# list.sort(reverse=True|False, key=nama_fungsi)

# Nilai Parameter
# Parameter                 Deskripsi
# reverse                   Opsional. reverse=True akan mengurutkan elemen list secara turun. Default adalah reverse=False
# key                       Opsional. Fungsi untuk menentukan kriteria penyortiran


listku = ['hello', 'alice', '2.5', 'Eliot', '3', 'WORLD', 'CARL']
listku.sort()
print(listku)   # ['2.5', '3', 'CARL', 'Eliot', 'WORLD', 'alice', 'hello']

# menggunakan parameter reverse=True
listku = ['hello', 'alice', '2.5', 'Eliot', '3', 'WORLD', 'CARL']
listku.sort(reverse=True)
print(listku)   # ['hello', 'alice', 'WORLD', 'Eliot', 'CARL', '3', '2.5']

# menggunakan parameter key=nama_fungsi
def panjang_kata(e):
    return len(e)

# mengurutkan berdasarkan panjang nilai
x = ['hello', 'bert', '2.5', 'Eliot', '3', 'WORLD', 'CARL']
x.sort(key=panjang_kata)
print(x)   # ['3', '2.5', 'bert', 'CARL', 'hello', 'Eliot', 'WORLD']

# mengurutkan berdasarkan panjang nilai dan dibalik
y = ['hello', 'bert', '2.5', 'Eliot', '3', 'WORLD', 'CARL']
y.sort(reverse=True, key=panjang_kata)
print(y)   # ['hello', 'Eliot', 'WORLD', 'bert', 'CARL', '2.5', '3']

# urutkan elemen list bertipe dict berdasarkan nilai "tahun"
def fungsi_tahun(e):
    return e['tahun']

data_mahasiswa = [
        {'nama':'alice', 'tahun':1999},
        {'nama':'carli', 'tahun':1994},
        {'nama':'eliot', 'tahun':1990},
        {'nama':'geral', 'tahun':2002}
        ]
data_mahasiswa.sort(key=fungsi_tahun)
print(data_mahasiswa)
# [{'nama': 'eliot', 'tahun': 1990}, {'nama': 'carli', 'tahun': 1994}, {'nama': 'alice', 'tahun': 1999}, {'nama': 'geral', 'tahun': 2002}]

# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan len() kunjungi folder_name: "Fungsi-Bawaan/fungsi_len.py"
