# Keyword-only arguments adalah sebuah fitur di Python yang memungkinkan Anda untuk
# menentukan argumen hanya dapat diterima jika ditentukan menggunakan keyword (yaitu, nama argumennya). 
# Ini berguna ketika Anda ingin memastikan bahwa argumen yang ditentukan tidak tertukar dengan argumen lainnya.

# Untuk menentukan argumen sebagai keyword-only, Anda dapat menggunakan tanda asterisk/bintang (*) di depan nama argumen.
def fungsiku(x, *, y, z):
    print(x, y, z)
# Dengan menggunakan tanda asterisk/bintang * ini, argumen y dan z hanya dapat diterima jika ditentukan menggunakan keyword.
# Jadi, jika Anda mencoba menggunakan fungsi di atas seperti ini:
# fungsiku(10, 20, 30)
# TypeError: fungsiku() takes 1 positional argument but 3 were given
# Maka Anda akan mendapatkan error "TypeError" karena argumen y dan z harus ditentukan menggunakan keyword.

# Jadi, cara yang benar untuk menggunakan fungsi di atas adalah seperti ini:
fungsiku(10, y=20, z=30)
# 10 20 30

fungsiku(10, y='hello', z='world')
# 10 hello world


# menggunakan default argument 
def tambah_mahasiswa(nama, *, usia=0, alamat='xxx'):
    print(f"{nama} {usia} {alamat}")

tambah_mahasiswa('alice')
# alice 0 xxx

tambah_mahasiswa('carl', usia=22, alamat='bandung')
# carl 22 bandung

# memanggil fungsi dengan argumen posisi sewenang-wenang
tambah_mahasiswa('eliot', alamat='surabaya', usia=20)
# eliot 20 surabaya
