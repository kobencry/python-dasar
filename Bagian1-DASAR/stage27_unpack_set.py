# unpacking/membongkar Set
#----------------------------------------------------------------------------
# Peringatan:
# Jika kita menggunakan set dalam operasi unpacking, maka urutan akhir dari 
# tugas bisa sangat berbeda dariyang kita inginkan dan harapkan. 
# Jadi, sebaiknya hindari penggunaan set dalam operasi unpack/pembongkaran 
# kecuali urutan penetapan tidak penting untuk kode kita.
#----------------------------------------------------------------------------

# Saat membuat set, kami biasanya memberikan nilai padanya, ini disebut "packing/mengemas" set.
packing_set = {'alice', 'carl', 'eliot'}
# unpacking set
x, y, z = packing_set
print(x)
print(y)
print(z)
# jalankan kode diatas berulang-ulang maka hasilnya akan berubah-ubah
# x = eliot atau carl  atau alice ..dst/dan seterusnya
# y = alice atau alice atau eliot ..dst/dan seterusnya
# z = carl  atau eliot atau carl  ..dst/dan seterusnya 
# jadi di contoh ini tidak akan menampilkan hasil keluarannya karna nilainya berubah-ubah.

# Catatan: Jumlah variabel harus sesuai dengan jumlah nilai dalam set,
# jika tidak, Anda harus menggunakan tanda bintang (*) untuk mengumpulkan
# nilai yang tersisa sebagai list.

# unpacking menggunakan tanda bintang *
packing_set = {'alice', 'carl', 'eliot', 'geral'}
x, y, *z = packing_set
print(x)
print(y)
print(z)

# Jika tanda bintang ditambahkan ke nama variabel lain selain yang terakhir,
# Python akan memberikan nilai ke variabel sampai jumlah nilai yang tersisa 
# sesuai dengan jumlah variabel yang tersisa.

packing_set = {'alice', 'carl', 'eliot', 'geral'}
x, *y, z = packing_set
print(x)
print(y)
print(z)
