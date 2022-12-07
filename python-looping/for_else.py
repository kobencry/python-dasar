# statement else
# keyword/kata kunci else dalam sebuah for loop menentukan blok kode yang akan dieksekusi ketika looping selesai.

for i in range(1, 3 + 1): # mencetak dimulai dari 1 - 3
    print('hello world')
else:
    print('akhir dari program.')
# hello world
# hello world
# hello world
# akhir dari program.

listku = ['alice', 'carl', 'eliot']
for nama in listku:
    print(nama)
else:
    print("program looping selesai.")
# alice
# carl
# eliot
# program looping selesai.

# Catatan: Blok else TIDAK akan dieksekusi jika perulangan dihentikan oleh sebuah statement break.
for i in range(1, 5):
    if i == 3:
        print(i, 'statement break')
        break
    print(i)
else:
    print("statement else tidak di jalankan")
# 1
# 2
# 3 statement break
