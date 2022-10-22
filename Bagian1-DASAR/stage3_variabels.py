# variabel adalah wadah untuk menyimpan nilai data.
# membuat variabel
# python tidak memiliki perintah untuk mendeklarasikan variabel.
# variabel dibuat saat Anda pertama kali menetapkan nilai padanya.

x = 5
y = "hello world"
print(x)
print(y)
#output
# 5
# alice

# variabel tidak perlu dideklarasikan dengan tipe tertentu , 
# dan bahkan dapat mengubah tipe setelah ditetapkan.
x = 4 # type int
x = "hello world" # type str
print(x)
# output
# hello world

# dapatkan jenisnya
# fungsi type() menampilkan tipe data
x = 5
y = "hello world"
print(type(x))
print(type(y))
# output
# <class 'int'>
# <class 'str'>

# tanda kutip tunggal('') atau ganda ("")
x = "hello"
y = 'world'
print(x)
print(y)
# output
# hello
# world

# nama variabel peka huruf besar/kecil
x = 4
X = "hello world"
print(x)
print(X)
# output
# 4
# hello world

#===============================================================================
# nama Variabel
# Sebuah variabel dapat memiliki nama pendek (seperti x dan y) atau 
# nama yang lebih deskriptif (nama, usia, jumlah_mahasiswa). 
# Aturan untuk variabel Python:
# nama variabel harus dimulai dengan huruf atau karakter garis bawah
# nama variabel tidak boleh diawali dengan angka
# nama variabel hanya boleh berisi karakter alfanumerik dan garis bawah (Az, 0-9, dan _ )
# nama variabel peka huruf besar/kecil (usia, Usia, dan AGE adalah tiga variabel berbeda)

# jenis-jenis nama variabel yang boleh diterapkan
#------------------------------------------------
# ingat variabel peka huruf besar/kecil
# varnama   = "hello world"
# var_nama  = "hello world"
# _var_nama = "hello world"
# varNama   = "hello world"
# VARNAMA   = "hello world"
# var2      = "hello world"
# var_nama_saya = "hello world"



# jenis-jenis nama variabel yang tidak boleh diterapkan
#-------------------------------------------------------
# 2var  = "hello world"
# var-x = "hello world"
# var x = "hello world"


#===============================================================================

# nama variabel multi kata
# nama variabel dengan lebih dari satu kata bisa jadi sulit dibaca.
# ada beberapa teknik yang dapat Anda gunakan untuk membuatnya lebih mudah dibaca:

# camel case
# setiap kata, kecuali yang pertama, dimulai dengan huruf besar kecil
# varNamaSaya = "alice"

# pascal case
# setiap kata dimulai dengan huruf kapital
# VarNamaSaya = "bob"

# snake case
# setiap kata dipisahkan oleh karakter garis bawah
# var_nama_saya  = "carl"

#===============================================================================

# menetapkan beberapa nilai/'assign multiple values'
# banyak nilai ke beberapa variabel
# Python memungkinkan Anda untuk menetapkan nilai ke beberapa variabel dalam satu baris:
# Catatan: 
# Pastikan jumlah variabel sesuai dengan jumlah nilai, atau Anda akan mendapatkan kesalahan.
x, y, z = "alice", "bob", "carl"
print(x)
print(y)
print(z)
# print(x, y, z)
# output
# alice
# bob
# carl

# contoh kesalahan
# x, y, z = "alice", "carl"
# x, y = "alice", "bob", "carl"

# satu nilai ke beberapa variabel
x = y = z = "hello world"
print(x)
print(y)
print(z)
# output
# hello world
# hello world
# hello world
