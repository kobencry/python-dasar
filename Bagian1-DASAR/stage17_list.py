# python list
# list adalah salah satu dari 4 tipe data bawaan dalam Python yang digunakan 
# untuk menyimpan koleksi data, 3 lainnya adalah Tuple, Set, dan Dictionary, 
# semuanya dengan kualitas dan penggunaan yang berbeda.

# list digunakan untuk menyimpan beberapa item dalam satu variabel.
# list dibuat menggunakan tanda kurung siku [].
# list dapat berisi tipe data yang berbeda
# list dapat diubah, artinya kita dapat mengubah, menambah, dan menghapus item dalam list setelah dibuat.
# list item diurutkan, dapat diubah, dan memungkinkan nilai duplikat
# list item diindeks, item pertama memiliki index [0], item kedua memiliki indeks [1] dll.
# Jika Anda menambahkan item baru ke list, item baru akan ditempatkan di akhir list.
# list serupa dengan tipe data array, tapi list bukan array hanya serupa.

# Catatan: Python tidak memiliki dukungan bawaan untuk Array, tetapi list Python dapat digunakan sebagai gantinya

# Dari perspektif Python, list didefinisikan sebagai objek dengan tipe data 'list'.
print(type(['x']))  # <class 'list'>

# membuat list
x = ['alice', 'carl', 'eliot', 'geral']
print(x)    # ['alice', 'carl', 'eliot', 'geral']

# membuat list dengan item duplikat
x = ['alice', 'carl', 'alice', 'carl']
print(x)    # ['alice', 'carl', 'alice', 'carl']

# membuat list dengan tipe data apapun
x = ['alice', 'carl', 'eliot']
y = [1, 2.5, 0xff, 0b11111111]
z = [True, False, None]
print(x)    # ['alice', 'carl', 'eliot']
print(y)    # [1, 2.5, 255, 255]
print(z)    # [True, False, None]
print(['alice', 2.5, True, 0xff, 'carl', False, 0b111, None])
# ['alice', 2.5, True, 255, 'carl', False, 7, None]

# menggunakan konstruktor list() saat membuat list
x = list(('alice', 2.5, True, 0xff, 0b11))
print(x)    # ['alice', 2.5, True, 255, 3]

# akses item list 
# item list diindeks dan anda dapat mengaksesnya dengan mengacu pada nomor indeks.
# catatan: item list pertama memiliki indeks 0
listku = ['alice', 'carl', 'eliot']
print(listku[0])    # alice
print(listku[1])    # carl
print(listku[2])    # eliot

# menggunakan indeks negatif
# pengindeksan negatif berarti mulai dari akhir
print(listku[-1])   # eliot
print(listku[-2])   # carl
print(listku[-3])   # alice

# unpacking/membongkar list
packing_list = ['alice', 'carl', 'eliot']
x, y, z = packing_list
print(x)    # alice
print(y)    # carl
print(z)    # eliot

# urutkan list Secara Alfanumerik (0-9A-Za-z)
# menggunakan "Method-List" dengan fungsi sort(), mengurutkan list secara alfanumerik, secara default ascending/menaik. 
listku = ['eliot', '2.5', 'carl', 'Alice', '1']
listku.sort()
print(listku) # ['1', '2.5', 'Alice', 'carl', 'eliot']

# urutan terbalik 
# menggunakan "Method-List" dengan fungsi reverse(), membalikan urutan pengurutan item list.
listku = ['alice', 'carl', 'eliot']
listku.reverse()
print(listku)   # ['eliot', 'carl', 'alice']

# gabungkan item list
list1 = ['alice', 'carl', 'eliot']
list2 = [1, 2.5, False, None]
hasil = list1 + list2
print(hasil)    # ['alice', 'carl', 'eliot', 1, 2.5, False, None]

# copy list menggunakan konstruktor list()
x = ['alice', 'carl', 'eliot']
copy_x = list(x)
print(copy_x)   # ['alice', 'carl', 'eliot']

# looping list
for i in ['alice', 2.5, False]:
    print(i)
# alice
# 2.5
# False

# menghitung jumlah item list
listku = ['alice', 2.5, False, 'carl', None]
print(len(listku))  # 5

# periksa apakah 'carl' ada dalam list
listku = ['alice', 'carl', 'eliot']
if 'carl' in listku:
    print('passed')

# jika ingin mempelajari lebih lanjut tentang slice list kunjungi folder_name: "Bagian1-DASAR/stage17_slice_list.py"
# jika ingin mempelajari lebih lanjut tentang modify list kunjungi folder_name: "Bagian1-DASAR/stage18_modify_list.py"
# jika ingin mempelajari lebih lanjut tentang Method-List sort() kunjungi folder_name: "Method-List/method_sort.py"
# jika ingin mempelajari lebih lanjut tentang Method-List reverse() kunjungi folder_name: "Method-List/method_reverse.py"
# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan list() kunjungi folder_name: "Fungsi-Bawaan/fungsi_list.py"
# jika anda ingin mengetahui tentang fungsi-bawaan len() kunjungi folder_name: "Fungsi-Bawaan/fungsi_len.py"
