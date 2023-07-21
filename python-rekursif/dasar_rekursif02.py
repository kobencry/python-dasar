# Sebuah fungsi rekursif terdiri dari dua elemen penting: 
# basis rekursif (base case) dan pemanggilan rekursif. 
# Basis rekursif adalah kondisi yang menentukan kapan rekursif harus berhenti,
# sedangkan pemanggilan rekursif adalah pemanggilan fungsi itu sendiri dalam implementasi yang lebih kecil dari masalah.

# Berikut ini adalah contoh dasar dari fungsi rekursif:
def main(n):
    x = 1
    if x < n: # base case (basis dasar rekursif) kapan rekusif harus berhenti
        main(n - x) # pemanggilan fungsi rekursif

    print("perulangan ke", n)

main(5)
# Output:
# perulangan ke 1
# perulangan ke 2
# perulangan ke 3
# perulangan ke 4
# perulangan ke 5

# Berikut ini adalah contoh implementasi fungsi rekursif yang meniru fungsi for loop dalam Python:
def for_loop(start, stop, step=1):
    print("hello world", start)

    if start >= stop: # base case (basis dasar rekursif) kapan rekursif harus berhenti
        # statemen "return" berguna untuk 
        # mengembalikan nilai atau menghentikan eksekusi fungsi
        return
    
    else:
        for_loop(start + step, stop, step) # pemanggilan fungsi rekursif

for_loop(1, 5)
# Output:
# hello world 1
# hello world 2
# hello world 3
# hello world 4
# hello world 5

for_loop(0, 8, 2)
# Output:
# hello world 0
# hello world 2
# hello world 4
# hello world 6
# hello world 8