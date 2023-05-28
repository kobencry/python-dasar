# Magic method __pos__ adalah method khusus dalam Python 
# yang digunakan untuk mengimplementasikan operasi positif (non-negatif) dari sebuah objek.
# method ini memungkinkan Anda untuk mendefinisikan perilaku objek ketika diaplikasikan operasi positif menggunakan operator +.

# method __pos__ harus mengembalikan hasil positif dari objek tersebut. 
# method ini dipanggil ketika Anda menggunakan operator + pada instance objek yang Anda buat.

# Berikut adalah contoh penggunaan method __pos__:

from collections import Counter

class Positif:
    def __init__(self, nilai):
        self.nilai = Counter(nilai)

    def __pos__(self):
        return +self.nilai

x = Positif({'coffe': 20, 'drink': 0, 'salt': -5})
print(+x)
# Output:
# Counter({'coffe': 20})

# Perlu dicatat bahwa implementasi __pos__ pada kelas dapat bervariasi 
# tergantung pada kebutuhan dan logika yang ingin Anda terapkan pada objek Anda.
# Contoh di atas hanya merupakan salah satu contoh sederhana dari penggunaan method __pos__.
