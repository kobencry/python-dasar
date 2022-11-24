# memodifikasi tuple python
# Ingat: Set  tidak dapat mengubah itemnya, tetapi Anda dapat menambahkan item baru.

# menambahkan item set menggunakan "Method-Set" fungsi add().
setku = {'hello', 'world'}
setku.add('alice')
print(setku)
# jalankan kode diatas berulang-ulang maka hasilnya akan berubah-ubah
# {'hello', 'world', 'alice'}
# {'hello', 'alice', 'world'}
# {'world', 'hello', 'alice'}
# {'world', 'alice', 'hello'}
# {'alice', 'hello', 'world'} 
# jadi di contoh ini tidak akan menampilkan hasil keluarannya karna nilainya berubah-ubah.

# menambahkan item dari item set lain ke set saat ini, gunakan fungsi update()
setku = {'alice', 'carl'}
x = {'eliot', 'geral'}
setku.update(x)
print(setku)

# menggunakan tipe data list
setku = {'alice', 'carl'}
listku = ['hello', 'world']
setku.update(listku)
print(setku)

# menggabung item set menggunakan "Method-Set" fungsi union()
set1 = {'alice', 'carl', 'eliot'}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# menghapus item set menggunakan fungsi remove()
setku = {'alice', 'carl', 'eliot'}
setku.remove('eliot')
print(setku)    # {'alice', 'carl'}

# jika anda ingin mengetahui tentang Method-Set kunjungi folder_name: "Method-Set"
