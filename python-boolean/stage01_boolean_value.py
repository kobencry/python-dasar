# Python memiliki tipe data Boolean yang memiliki dua nilai, yaitu True dan False. 
# Ini berguna ketika kita ingin menentukan suatu kondisi atau membuat logika pada program.

# Nilai Boolean:
# Dalam pemrograman, Anda sering perlu mengetahui apakah suatu ekspresi adalah True atau False.
# Anda dapat mengevaluasi ekspresi apa pun dengan Python, dan mendapatkan salah satu dari dua jawaban, True atau False.
# Saat Anda membandingkan dua nilai, ekspresi dievaluasi dan Python mengembalikan jawaban Boolean:

print(type(True))   # <class 'bool'>
print(type(False))  # <class 'bool'>

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
# Sebagai contoh, jika Anda ingin menganalisis suatu halaman dalam sebuah buku untuk 
# melihat bagian dari halaman yang berisi kata "the", fakta bahwa True setara dengan 1 dan False setara dengan 0 bisa sangat membantu.

books = "Mastering the Basics of Python"
print('the' in books)
