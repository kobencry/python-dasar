# python set

# Set adalah salah satu dari 4 tipe data bawaan di Python yang digunakan untuk
# menyimpan kumpulan data, 3 lainnya adalah List, Tuple, dan Dictionary,
# semuanya dengan kualitas dan penggunaan yang berbeda.

# Set adalah kumpulan yang unordered/tidak teratur, unchangeable/tidak dapat berubah, unindexed/tidak terindex dan nilai tidak boleh duplikat/sama. 
# Set item dapat muncul dalam urutan yang berbeda setiap kali Anda menggunakannya, dan tidak dapat dirujuk dengan indeks atau kunci.

# Catatan: Set item tidak dapat diubah, tetapi Anda dapat menghapus item dan menambahkan item baru.

# membuat set dengan tanda kurung kurawal {}
x = {'alice', 'carl', 'eliot'}
print(x)
# jalankan kode diatas berulang-ulang maka hasilnya akan berubah-ubah
# {'alice', 'eliot', 'carl'}
# {'carl', 'alice', 'eliot'}
# {'alice', 'eliot', 'carl'}
# {'eliot', 'alice', 'carl'}
# jadi di contoh ini tidak akan menampilkan hasil keluarannya karna nilainya berubah-ubah.

# membuat set dengan konstuktor set()
set_kosong = set()
print(set_kosong)       # set()
print(type(set_kosong)) # <class 'set'>

# jika anda ingin membuat set kosong gunakan konstruktor set()
# jangan menggunakan tanda kurung kurawal {} = tipe data dict

x = set(('alice', 'carl', 'eliot'))
print(x)

y = set(['alice', 'carl', 'eliot'])
print(y)

# item set tidak boleh duplikat/sama maka item set yang sama akan diabaikan.
setku = {'alice', 'carl', 'alice', 'alice'}
print(setku)    # {'alice', 'carl'}

# item set dapat berisi tipe data yang berbeda.
setku = {'hello', True, 3, 'world', False, 2.5, ('b', None)}
print(setku)

# mendapatkan jumlah item set
setku = {'hello', True, 3, 'world', False}
print(len(setku))   # 5

# medapatkan jenis tipe data
setku = {'hello', True, 'world', False}
print(type(setku))  # <class 'set'>

# tambahkan item set menggunakan fungsi add()
setku = {'hello'}
setku.add('world')
print(setku)

# hapus item set menggunakan fungsi update()
setku = {'alice', 'carl', 'eliot'}
x = {23, 22, 20}
setku.update(x)
print(setku)

# Anda tidak dapat mengakses item dalam satu set dengan mengacu pada indeks atau kunci.
# Tapi Anda bisa mengulang item set menggunakan while/for loop, atau menanyakan apakah 
# ada nilai tertentu dalam set, dengan menggunakan keyword 'in'.
setku = {'alice', 'carl', 'eliot', True, False}
for i in setku:
    print(i)

if 'eliot' in setku:
    print("passed")

# jika anda ingin mengetahui tentang fungsi-bawaan len() kunjungi folder_name: "Fungsi-Bawaan/fungsi_len.py"
# jika anda ingin mengetahui tentang Method-Set kunjungi folder_name: "Method-Set"
