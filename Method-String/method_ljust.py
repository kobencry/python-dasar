# -- Method String --

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi ljust() akan menyelaraskan/menyesuaikan string ke kiri, menggunakan karakter tertentu 
# (default/standarnya adalah spasi) sebagai karakter isian.

# Syntax
# string.ljust(panjang, karakter)

# Nilai Parameter
# Parameter             Deskripsi
# panjang               Dibutuhkan. Panjang string yang dikembalikan
# karakter              Opsional. Karakter untuk mengisi spasi yang hilang (di sebelah kanan string). 
#                       Standarnya adalah " " (spasi).

x = "hello"
y = "hello"
print(x.ljust(20), 'world')
print(y.ljust(20, '+'), 'world')

# contoh dengan struk belanjaan
print("apel".ljust(20,'.'), '3')
print("cheri".ljust(20,'.'), '5')
print("total item".ljust(20, '.'), '7')

# contoh dengan skor bola
nama_tim = {0:('ajax', 'itermilan'), 1:('real-madrid', 'barca'), 2:('juventus', 'dortmund')}
skor = ('2:3', '2:2', '2:1')
for i in nama_tim:
    x = nama_tim[i][0].ljust(15) + '-'.ljust(5) + nama_tim[i][1].ljust(15) + skor[i].ljust(4)
    print(x)
