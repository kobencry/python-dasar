# -- Fungsi bawaan python --

# fungsi float() mengubah nilai yang ditentukan menjadi angka float.

# Syntax
# float(value)

# Nilai Parameter
# Parameter         Deskripsi
# value             Dibutuhkan. Angka, string, boolean True False yang dapat diubah menjadi angka float

s = "5"
i = 5
t = True
f = False
h = 0xff
o = 0o5
print(float(s)) # 5.0
print(float(i)) # 5.0
print(float(t)) # 1.0
print(float(f)) # 0.0
print(float(h)) # 255.0
print(float(o)) # 5.0

print(float(5 + 2)) # 7.0
print(float(2**5))  # 32.0
print(float(10/2))  # 5.0

# Tahukah Anda float("NaN") dan float("inf") ada di Python?
# NaN != NaN. Sedangkan inf == inf. Tapi kenapa?

print(float('NaN') == float('NaN')) # False
print(float('inf') == float('inf')) # True

# Apa itu NaN dan Inf?
# Bagi mereka yang tidak terbiasa dengan notasi inf dan NaN, 
# masing-masing mereka berdiri untuk infinity dan bukan sebuah angka.

# Meskipun infinity dapat dianggap sebagai jumlah yang sangat sangat besar, ia tidak memiliki akhir.
# Kita dapat mendefinisikan infinity negatif sebagai -inf dan infinity positif inf. 
# Dalam matematika, sqrt(-1) dalam bilangan real atau 0/0 (nol di atas nol) memberikan angka yang tidak ditentukan, 
# yang dapat didefinisikan sebagai Nan. 
# Dalam ilmu data, Nan digunakan untuk mewakili nilai yang hilang dalam dataset.
# Jadi Nan pada dasarnya adalah placeholder untuk mewakili nilai yang tidak ditentukan atau hilang.

# Anda dapat membuat nilai Nan menggunakan tipe float.
# Karena ini bukan kata kunci yang ditentukan dengan Python, Anda harus meneruskannya 
# untuk float dalam format string (dalam tanda kutip).

# Satu hal yang layak disebutkan di sini adalah "Nan" tidak peka huruf besar/kecil.
# Jadi Anda dapat menggunakan format apa pun di bawah ini untuk membuat nilai "Nan".
# float("Nan")
# float("NAn")
# float("NAN")
# float("NaN")
# float("nAn")
# float("nAN")
# float("naN")
# float("nan")
# float("+nan")
# float("-nan")

# mari kita lihat tentang inf. 
# Anda dapat mendefinisikan nilai inf seperti yang Anda lakukan
# untuk mendefinisikan nilai Nan. Inf juga tidak peka huruf besar/kecil. 
# Anda dapat memilih salah satu dari mereka untuk dibuat
# float("Inf")
# float("INf")
# float("InF")
# float("INF")
# float("iNf")
# float("inF")
# float("iNF")
# float("inf")
# float("+inf")
# float("-inf")
# float("infinity")
# float("inFINity")

print(float("inf") + 1) # inf
print(float("inf") * 2) # inf
print(0 - float("inf")) # -inf
print(float("inf") * float("inf"))  # inf
print(float("inf") + float("inf"))  # inf
print(float("inf") - float("inf"))  # nan
print(float("inf") / float("inf"))  # nan
print(float("inf") > float("-inf")) # True
