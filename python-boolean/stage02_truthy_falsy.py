# "Truthy" dan "Falsy" adalah istilah yang digunakan untuk mengacu pada objek-objek 
# yang memiliki nilai boolean True atau False di Python. 
# Sebuah objek bisa dikatakan "truthy" jika memiliki nilai boolean True dan 
# dapat digunakan sebagai kondisi yang benar (True). 
# Sebaliknya, objek "falsy" memiliki nilai boolean False dan bisa digunakan sebagai kondisi yang salah (False).

# menggunakan fungsi-bawaan bool() pada python untuk memeriksa apakah nilai boolean bernilai True atau False.

# Contoh objek-objek "truthy" di Python adalah: 
# tipe data boolean: True
# tipe data numerik: -10, -1, 1, 1.0, 2.05, 5j, 0x01, 0b01, 0o01 dll.
# tipe data koleksi: "0", [0, 1, 2], ('a','b', 'c'), {'1', 2, 0.1}, {1:'a', 2:'b', 3:'c'}, range(1), frozenset(1, 'a')
print(bool(True))   # True
print(bool(-10))    # True
print(bool(1))      # True

num_list = [-1, -1.05, 1.0, 2.05, 5j, 0x01, 0b01, 0o01]
for i in num_list:
    print(bool(i))
# semua outputnya adalah True

listku = [0, 0.1, 0]
print(bool(listku))
# Output:
# True

tupleku = ('', 0, 0.20)
print(bool(tupleku))
# Output:
# True

setku = {False, None, 0}
print(bool(setku))
# Output:
# True

dictku = {False:0, None:0}
print(bool(dictku))
# Output:
# True

rangeku = range(10)
print(bool(rangeku))
# Output:
# True

stringku = "0"
print(bool(stringku))
# Output:
# True

# Contoh objek-objek "falsy" di Python adalah:
# tipe data boolean: False, None
# tipe data numerik: 0, 0.1, 0.25, 0j
# tipe data koleksi: "", [], (), set(), {}, range(0) frozenset()
print(bool(False))  # False
print(bool(None))   # False
print(bool(0))      # False

num_list = [0, 0.0, 0j, 0x00, 0o00, 0b00]
for i in num_list:
    print(bool(i))
# semua outputnya False

koleksi_list = ['', [], (), set(), {}, range(0), frozenset()]
for i in koleksi_list:
    print(bool(i))
# semua outputnya False

# menggunakan tipe data string
x = "hello world"
if x: # ini disebut truthy
    print("truthy")
else:
    print("falsy")
# Ouput:
# truthy

y = ""
if y: # ini disebut falsy
    print("truthy")
else:
    print("falsy")
# Output:
# falsy

# menggunakan tipe data numerik
x = 1
if x:
    print("truthy")
else:
    print("falsy")
# Output:
# truthy

y = 0
if y:
    print("truthy")
else:
    print("falsy")
# Output:
# falsy

def passed():
    pass
print(bool(passed))
# Output:
# True

# Menghindari Exception/Pengecualian
# Misalkan Anda telah mendefinisikan dua variabel x dan y, dan Anda ingin mengetahuinya
# bahwa 1 dibagi dengan 0 akan menampilkan pesan error: "ZeroDivisionError: division by zero"
x = 0
y = 1
print(x != 0 and (y / x) > 0)
# Output:
# False

# Dalam hal ini, jika "x" bernilai 0, ekspresi x != 0 akan langsung bernilai false, 
# dan evaluasi akan berhenti di sana. 
# Konsekuensinya, (y / x) tidak perlu dievaluasi dan tidak akan terjadi kesalahan.
# Di sini juga disebutkan bahwa kita bisa lebih singkat lagi dengan memperlakukan "x" sendiri sebagai falsy jika bernilai 0. 
# Kita tidak perlu melakukan perbandingan eksplisit dengan x != 0.

print(x and (y / x) > 0)
# Output:
# 0