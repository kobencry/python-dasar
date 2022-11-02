# Catatan:
# Jika anda belum mengetahui definisi fungsi di python maka lewati tutorial ini

# variabel global
# variabel yang dibuat di luar fungsi (seperti dalam semua contoh di atas) 
# dikenal sebagai variabel global.
# variabel global dapat digunakan oleh semua orang, baik di dalam fungsi maupun di luar.

x = "alice"

# gunakan nama variabel di dalam fungsi
def fungsi():
    print("nama saya", x)

fungsi()
print(x)

# Jika Anda membuat variabel 'x' dengan nama yang sama di dalam fungsi,
# variabel 'x' akan menjadi lokal, dan hanya dapat digunakan di dalam fungsi.
# variabel global dengan nama 'x' yang sama akan tetap seperti sebelumnya.

x = "alice"

def fungsi():
    # membuat variabel local/di dalam fungsi
    x = "eliot"
    print("local x:", x)

fungsi()
print("global x:", x)

# menggunakan keywords global python
# Biasanya, ketika Anda membuat variabel di dalam fungsi/variabel lokal, 
# hanya dapat digunakan di dalam fungsi itu.
# untuk membuat variabel global di dalam fungsi, Anda dapat menggunakan kata kunci global.
# jika Anda menggunakan kata kunci global, lingkup variabel local milik global.

def fungsi():
    global y
    y = "variabel local"
fungsi()
print(y)

def fungsi():
    global y
    y = "alice"
    print("di dalam fungsi:", y)
fungsi()
print("di luar fungsi:", y)

# contoh kesalahan runtime tidak menggunakan keywords global
#def fungsi():
#    var_x = "hello world"
#    print("hello world")
#fungsi()
#print(var_x)

# mengubah variabel global di dalam fungsi/local
nama = "alice"
def ubah_nama():
    global nama
    print("sebelum:", nama)
    nama = "eliot"
    print("sesudah:", nama)
ubah_nama()
# nama alice diubah menjadi eliot menggunakan keywords global
print("di luar fungsi:", nama)
