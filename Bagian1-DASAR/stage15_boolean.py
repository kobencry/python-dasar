# python nilai boolean
# Dalam pemrograman, Anda sering perlu mengetahui apakah ekspresi itu True/Benar atau False/Salah.
# Anda dapat mengevaluasi ekspresi apa pun dengan Python, dan mendapatkan salah satu dari dua jawaban,
# True/Benar atau False/Salah.
# Saat Anda membandingkan dua nilai, ekspresi dievaluasi dan Python mengembalikan nilai Boolean:

# menggunakan operator perbandingan
print(3 > 2)    # True
print(3 == 2)   # False
print(3 < 2)    # False

# menggunakan pernyataan if mengembalikan nilai boolean True atau False
x = 3
y = 2

if x > y:
    # jika pernyataan if bernilai boolean True
    # jalankan block di bawah ini
    print("passed")

# menggunakan fungsi bool()
# fungsi bool() memungkinkan Anda untuk mengevaluasi nilai apa pun, dan memberi Anda True atau False sebagai nilainya
x = "hello world"
y = 10
print(bool(x))  # True
print(bool(y))  # True
print(bool("")) # False
print(bool(0))  # False

# menggunakan fungsi dapat mengembalikan nilai boolean True atau False
def fungsi_true():
    return True

def fungsi_false():
    return False

print(fungsi_true())    # True
print(fungsi_false())   # False

# Python juga memiliki banyak fungsi bawaan yang mengembalikan nilai boolean,
# seperti fungsi isinstance(), yang dapat digunakan untuk menentukan apakah 
# suatu objek bertipe data tertentu
x = 10
y = "hello world"
print(isinstance(x, int))   # True
print(isinstance(y, str))   # True

# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan bool() kunjungi folder_name: "Fungsi-Bawaan/fungsi_bool.py"
# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan isinstance() kunjungi folder_name: "Fungsi-Bawaan/fungsi_isinstance.py"
