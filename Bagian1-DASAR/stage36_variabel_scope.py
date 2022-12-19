# Variabel scope adalah cakupan atau lingkup suatu variabel dalam sebuah program. 
# Variabel yang didefinisikan di dalam fungsi atau di dalam blok kode 
# tertentu hanya dapat digunakan di dalam blok kode tersebut. 
# Di luar blok kode tersebut, variabel tersebut tidak dapat diakses atau digunakan. 
# Ada dua jenis variabel scope di Python, yaitu global dan local.

# Variabel global adalah variabel yang didefinisikan di luar fungsi atau blok kode tertentu,
# sehingga dapat diakses dan digunakan di seluruh program.
# yang sudah dijelaskan di stage04_variabel_global.py

# Variabel local adalah variabel yang didefinisikan di dalam fungsi atau blok kode tertentu,
# sehingga hanya dapat diakses dan digunakan di dalam blok kode "fungsi" tersebut.

# Sebagai contoh, misalkan kita memiliki variabel 'x' yang didefinisikan di luar fungsi:
# Di sini, variabel 'x' merupakan variabel global karena didefinisikan di luar fungsi.
# Karena itu, variabel 'x' dapat diakses dan digunakan di dalam fungsi func_global().
# Variabel yang dibuat di luar fungsi bersifat global dan dapat digunakan di seluruh program
x = 10  #variabel global

def func_global():
    print(x, 'di dalam fungsi func_global()')
    print()
func_global()   # 10 di dalam fungsi func_global()
print(x)    # 10

# Sebaliknya variabel 'y' yang dibuat di dalam suatu fungsi.
def func_local():
    y = 20  #variabel local
    print(y)
func_local()    # 20
# akan menampilkan pesan kesalahan
# print(y)    # NameError: name 'y' is not define

#===============================================================================

# variabel scope local
# fungsi didalam fungsi
# Seperti yang dijelaskan pada contoh di atas, variabel 'y' tidak tersedia di luar
# fungsi, tetapi tersedia untuk fungsi apa pun di dalam fungsi:
# variabel local dapat diakses dari fungsi di dalam fungsi
def func_local():
    y = 30
    def inner_func_local():
        print(y, "di dalam fungsi inner_func_local()")
    inner_func_local()
func_local()    # 30 di dalam fungsi inner_func_local()

#===============================================================================

# penamaan variabel
# Jika Anda mengoperasikan dengan nama variabel yang sama di dalam dan di luar fungsi,
# Python akan memperlakukannya sebagai dua variabel terpisah, 
# satu tersedia di lingkup global (di luar fungsi) dan satu tersedia di lingkup lokal (di dalam fungsi):
x = "variabel global"
def fungsiku():
    x = "variabel local"
    print(x)
# akan mencetak local 'x' dan kemudian kode akan mencetak global 'x'
fungsiku()  # variabel local
print(x)    # variabel global

#===============================================================================

# keyword 'global'
# jika anda perlu membuat variabel global, didalam lingkup local (di dalam fungsi)
# anda dapat menggunakan keyword 'global'
def func_local():
    global x
    x = "alice"
    print(x, 'di dalam fungsi')
func_local()
print(x, 'di luar fungsi')
# alice di dalam fungsi
# alice di luar fungsi

# anda dapat mengubah isi dari variabel global di dalam fungsi (lingkup local)
y = "variabel global"
def func_local():
    global y
    print(y)    # variabel global
    # mengubah isi dari variabel global
    y = "variabel local"
func_local()
print(y)    # variabel local
