# -- Fungsi bawaan python --

# https://docs.python.org/3/library/functions.html?highlight=built-function-float#float
# https://docs.python.org/3/library/stdtypes.html?highlight=float#float.fromhex

# fungsi float() mengubah nilai yang ditentukan menjadi angka float.

# Syntax
# float(value)

# Nilai Parameter
# Parameter         Deskripsi
# value             Dibutuhkan. Angka, string, boolean True False, inf, Nan yang dapat diubah menjadi angka float

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

print(float(+123))  # 123.0
print(float(-123))  # -123.0
print(float(1e-003))    # 0.001
print(float(+1E6))  # 1000000.0

# method tambahan di fungsi float()
#----------------------------------

# float.as_integer_ratio()
# Mengembalikan sepasang bilangan bulat yang rasionya sama persis dengan float asli dan dengan penyebut positif.
print(1.5.as_integer_ratio())   # (3, 2)

# mengubah desimal ke pecahan
def bilangan_pecahan(nilai_decimal):
    y = nilai_decimal.as_integer_ratio()
    return y
x = bilangan_pecahan(1.5)
print(x[0], "/", x[1])  # 3 / 2

# float.is_integer()
# Kembalikan True jika instance float terbatas dengan nilai integral, dan False jika sebaliknya.
print(3.0.is_integer())     # True
print(3.1.is_integer())     # False
print(5.0.is_integer())     # True
print(5.123.is_integer())   # False


# mengubah nilai float ke hexa
print(float.hex(2.5))   # 0x1.4000000000000p+1
print(float.hex(5.0))   # 0x1.4000000000000p+2
print(float.hex(16.0))  # 0x1.0000000000000p+4

# mengubah nilai hexa ke float
# [sign]['0x'] integer ['.' fraction]['p' exponen]
print(float.fromhex('0x1.5af526p24'))   # 22738214.0
print(float.fromhex('0xfed01'))         # 1043713.0
print(float.fromhex('0x3.a7p10'))       # 3740.0


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
