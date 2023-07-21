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