# Pernyataan bersyarat dengan python

# Inilah yang akan Anda pelajari dalam tutorial ini: 
# Anda akan menemukan struktur kontrol Python pertama Anda, pernyataan if.

# Di dunia nyata, kita umumnya harus mengevaluasi informasi di sekitar kita 
# dan kemudian memilih satu atau lain tindakan berdasarkan apa yang kita amati.
# contoh tindakan di dunia nyata:
# Jika cuacanya bagus, maka saya akan bermain bola.
# (Tersirat bahwa jika cuacanya tidak bagus, maka saya tidak akan bermain bola.)

# Statement if
# Dalam program Python, pernyataannya if adalah bagaimana Anda melakukan pengambilan keputusan semacam ini.
# Ini memungkinkan eksekusi bersyarat dari suatu pernyataan atau sekelompok pernyataan berdasarkan nilai ekspresi.

# Syntax
# if <kondisi>:
#      <expresi>

# <kondisi> adalah ekspresi yang dievaluasi dalam konteks Boolean, seperti yang dibahas di bagian operator python di folder_name: "python-operator"
# <expresi> adalah pernyataan Python yang valid, yang harus diberi indentasi(baris yang menjorok ke dalam).

# jika <kondisi> True/Benar (dievaluasi ke nilai yang "True"), maka <expresi> di jalankan.
# jika <kondisi> False/Salah, maka <expresi> dilewati dan tidak dieksekusi.

x = 10
y = 20
# contoh menggunakan operator comparison/perbandingan 
# jika x lebih kecil dari y, maka jalankan <expresi> "passed"
if x < y:
    print("passed")     # isi pesannya boleh apa saja
# * apakah 10 lebih kecil dari 20, True
# * jika hasilnya True, jalankan <expresi> "passed"
# print(x < y)    # True

if x > y:
    print("statemen ini dilewati dan tidak dieksekusi")
# * apakah 10 lebih besar dari 20, False
# * jika hasilnya False, maka <expresi> dilewati dan tidak dieksekusi.
# print(x > y)    # False

# Catatan: pernyataan if jika hasil Boolean True, <expresi> akan di jalankan.
if x: # ini disebut dengan truthy
    print("passed") # passed
print(bool(x))      # True


# contoh menggunakan boolean True
if True: # ini disebut dengan truthy
    print("passed") # passed

# contoh menggunakan boolean False
if False: # ini disebut dengan falsy
    print("statement ini dilewati dan tidak dieksekusi")

# jika anda memiliki satu <expresi> untuk dieksekusi, 
# anda dapat meletakkannya pada satu baris kode yang sama dengan pernyataan if.
# Syntax
# if <kondisi>: <expresi>
if x < y: print("passed")   # passed

# jika anda memiliki lebih dari satu <expresi> untuk dieksekusi,
# anda dapat meletakkannya pada satu baris kode yang sama dengan pernyataan if.
# Syntax
# if <kondisi>: <expresi_1>; <expresi_2>; <expresi_3>; ...dst
# pisahkan dengan titik koma;
if x < y: print("passed"); print("hello world"); print(True);
# "teknik ini dikenal sebagai operator ternary atau conditional expressions/ekspresi bersyarat."

# kode ini setara dengan yang diatas:
#if x < y:
#    print("passed")
#    print("hello world")
#    print(True)

#=================================================================================


# Statement elif
# Dalam program python, pernyataan elif adalah cara python untuk mengatakan 
# "jika kondisi sebelumnya tidak benar, maka coba kondisi ini (elif)".

# Syntax
# if <kondisi>:
#       <expresi>
# elif <kondisi>:
#       <expresi>

if x > y:   # False
    print("statemen ini dilewati dan tidak dieksekusi")
elif x < y: # True
    print("passed") # passed
# apakah x lebih besar dari y, False
# apakah x lebih kecil dari y, True
# * jika hasilnya True, jalankan <expresi> "passed"

# menggunakan lebih dari satu elif
nama = "alice"
if nama == 'geral':     # False
    print("hello geral")
elif nama == 'carl':    # False
    print("hello carl")
elif nama == 'eliot':   # False
    print("hello eliot")
elif nama == 'alice':   # True
    print("hello alice")
elif nama == 'bert':    # kode ini belum dibaca oleh program
    print("hello bert")


#=================================================================================


# Statement else
# Dalam program python, pernyataan else adalah menangkap apapun yang tidak
# tertangkap oleh kondisi sebelumnya

# Syntax
# if <kondisi>:
#      <expresi>
# elif <kondisi>:
#      <expresi>
# else:
#      <expresi>
nama = "python"
if nama == 'carl':      # False
    print("hello carl")
elif nama == 'eliot':   # False
    print("hello eliot")
else:   # jika kondisi diatas False, eksekusi <expresi> ini
    print("hello world")
# apakah 'python' sama dengan 'carl', False
# apakah 'python' sama dengan 'eliot', False
# jadi kita beralih ke kondisi else jalankan <expresi> 'hello world'

# menggunakan if else
dataku = ['alice', 'carl', 'eliot']
if "python" in dataku:  # False
    print("passed")
else:
    print("failed")
# apakah 'python' ada di dalam dataku, False
# jika pernyataan if False, program beralih ke kondisi else jalankan <expresi> 'failed'

# Jika Anda hanya memiliki satu pernyataan untuk dieksekusi, satu untuk if, dan
# satu lagi untuk else, Anda dapat meletakkan semuanya pada satu baris yang sama.
# Syntax
# <expresi_1> if <kondisi> else <expresi_2>
x = 10
y = 20
print("passed") if x < y else print("failed")   # passed
# kode ini setara dengan yang diatas
# if <kondisi>:
#       <expresi_1>
# else:
#       <expresi_2>

# Anda juga dapat memiliki beberapa pernyataan lain di baris yang sama.
# menggunakan pernyataan if else satu baris, dengan 3 kondisi
# Syntax
# <expresi_1> if <kondisi_1> else <expresi_2> if <kondisi_2> else <expresi_3>
nama = 'python'
# nama = 'xxx'
print('hello alice') if nama == 'alice' else print('hello python') if nama == 'python' else print('hello world')
# hello python

# kode ini setara dengan yang diatas
# nama = 'python'
# # nama = 'xxx'
# if nama == 'alice':
#     print("hello alice")
# else:
#     if nama == 'python':
#         print('hello python')
#     else:
#         print("hello world")

# Statement if elif else dengan satu baris
nama = 'python'
if nama == 'alice': print("hello alice")
elif nama == 'carl': print("hello carl"); print("statement carl");
elif nama == 'eliot': print("-------------"); print("hello eliot"); print("------------------");
else: print("hello world")  # hello world
# Sementara semua ini berfungsi, dan penerjemah mengizinkannya, 
# umumnya tidak disarankan dengan alasan menyebabkan keterbacaan yang buruk, 
# terutama untuk pernyataan if yang rumit. PEP8 secara khusus merekomendasikan untuk tidak melakukannya.
# pep8: https://peps.python.org/pep-0008/#other-recommendations
# Seperti biasa, ini soal selera.

#=================================================================================

# menggunakan nested statement if/pernyataan if bersarang
# anda dapat memiliki if didalam if ini disebut if bersarang
nama = 'python'
if nama == 'python':
    nama = 'hello world'
    if nama == 'python':
        print('passed')
    else:
        print(nama)

# menggunakan keyword 'pass'
# pernyataan if tidak boleh kosong, tetapi jika karena alasan tertentu 
# Anda memiliki pernyataan if tanpa konten atau <expresi>, 
# masukkan <expresi> keyword 'pass' untuk menghindari kesalahan.
if 'python' != 'hello world':
    pass

# jika anda ingin mengetahui tentang operator python kunjungi folder_name: "python-operator"
# jika anda ingin mengetahui tentang fungsi bool() python kunjungi folder_name: "Fungsi-Bawaan/fungsi_bool.py"
