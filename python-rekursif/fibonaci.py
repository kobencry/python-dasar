# Menentukan Bilangan Fibonaci dengan Fungsi Rekursif
def fibonaci(n):
    if n == 0 or n == 1:
        return n
    
    else:
        return (fibonaci(n - 1) + fibonaci(n - 2))

for i in range(10):
    print(fibonaci(i), end=' ')
# Output:
# 0 1 1 2 3 5 8 13 21 34

# fungsi fibonaci() yang juga merupakan penerapan dari fungsi rekursif. 
# Bilangan fibonaci adalah bilangan yang memiliki suku awal 0 atau 1 dan suku-suku 
# berikutnya merupakan penjumlahan dari dua suku sebelumnya.
# Pengguna memasukan batas deret bilangan fibonaci yang nilainya di tampung pada variabel x.
# Untuk menampilkan deret kita perlu menggunakan perulangan for. 
# yang akan mencetak setiap nilai yang di proses dalam fungsi fibonaci().