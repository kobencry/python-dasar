# Positional-only arguments adalah sebuah fitur baru di Python 3.8 yang memungkinkan
# Anda untuk menentukan argumen hanya dapat diterima berdasarkan posisinya, bukan namanya.
# Ini berguna ketika Anda ingin memodifikasi sebuah fungsi yang 
# sudah ada dan tidak ingin merubah cara argumennya dituliskan.

# Untuk menentukan argumen sebagai positional-only, 
# Anda dapat menggunakan tanda slash (/) di depan nama argumen.
def fungsiku(x, y, /):
    print(x, y)
# Dengan menggunakan tanda slash (/) ini, argumen x dan y hanya dapat 
# diterima berdasarkan posisinya, tidak dapat diterima menggunakan keyword. 
# Jadi, jika Anda mencoba menggunakan fungsi di atas seperti ini:

# memanggil fungsiku dengan argumen keyword
# fungsiku(x='alice', y=20)
# TypeError: fungsiku() got some positional-only arguments passed as keyword arguments: 'x, y'
# Maka Anda akan mendapatkan error "TypeError" karena argumen x dan y harus ditentukan berdasarkan posisinya.

# Jadi, cara yang benar untuk menggunakan fungsi di atas adalah seperti ini:
fungsiku('alice', 20)
# alice 20

fungsiku(100, 200)
# 100 200

# fungsi ini menambah data mahasiswa
def tambah_data(nama, usia, /, alamat='jakarta'):
    print("data ditambahkan")
    print(f"nama: {nama} usia: {usia} alamat: {alamat}")

tambah_data('alice', 23)
# data ditambahkan
# nama: alice usia: 23 alamat: jakarta

tambah_data('carl', 20, 'bandung')
# data ditambahkan
# nama: carl usia: 20 alamat: bandung

tambah_data('eliot', 28, alamat='surabaya')
# data ditambahkan
# nama: eliot usia: 28 alamat: surabaya
