# Python memiliki tipe data Boolean yang memiliki dua nilai, yaitu True dan False. 
# Ini berguna ketika kita ingin menentukan suatu kondisi atau membuat logika pada program.

# Nilai Boolean:
# Dalam pemrograman, Anda sering perlu mengetahui apakah suatu ekspresi adalah True atau False.
# Anda dapat mengevaluasi ekspresi apa pun dengan Python, dan mendapatkan salah satu dari dua jawaban, True atau False.
# Saat Anda membandingkan dua nilai, ekspresi dievaluasi dan Python mengembalikan jawaban Boolean:

print(type(True))   # <class 'bool'>
print(type(False))  # <class 'bool'>

# Boolean sebagai angka:
# Pada Python, Boolean dikategorikan sebagai tipe data numerik. 
# Artinya, mereka diperlakukan seperti angka untuk semua tujuan. 
# Dengan kata lain, Anda bisa mengaplikasikan operasi aritmatika pada Boolean,
# dan juga bisa membandingkannya dengan angka.

print(True == 1)    # True
print(False == 0)   # True

print(True + True + True) # 3

print(True + 5 + (False / True))    # 6.0

# Penggunaan Boolean sebagai nilai numerik jarang digunakan, namun ada satu teknik yang mungkin berguna.
# Karena True setara dengan 1 dan False setara dengan 0, 
# menambahkan Boolean bersama-sama adalah cara cepat untuk menghitung jumlah nilai True. 
# Ini bisa sangat berguna saat Anda perlu menghitung jumlah item yang memenuhi suatu kondisi.
# Sebagai contoh, jika Anda ingin menganalisis suatu nama dalam sebuah data mahasiswa 
# melihat bagian dari nama yang berisi kata "ali", fakta bahwa True setara dengan 1 dan False setara dengan 0 bisa sangat membantu.

data_mahasiswa = """\
nama, usia, alamat 
ali, 23, jakarta
boby, 20, bandung
alice, 25, tangerang
carl, 22, surabaya
falic, 26, jakarta  
""".splitlines()
print(len(data_mahasiswa))

total = sum("alice" in baris.lower() for baris in data_mahasiswa) / len(data_mahasiswa)
print(total, f"{total:.3f}")

