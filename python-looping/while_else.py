# statement else
# menggunakan pernyataan else kita dapat menjalankan blok kode satu kali ketika kondisi tidak lagi True.

i = 0
while i < 5:
    print(i)
    # i = i + 1
    # kode ini setara dengan diatas
    i += 1

else:
    print("akhir dari while loop")
# 0
# 1
# 2
# 3
# 4
# akhir dari while loop

# Catatan: Blok else TIDAK akan dieksekusi jika perulangan dihentikan oleh sebuah statement break.

listku = ['alice', 'hello', 'world', 'carl']
while len(listku):
    hapus = listku.pop()
    
    if hapus == 'hello':
        print('stop looping')
        break
    else:
        print(hapus)

else:   # statement else tidak dieksekusi
    print("akhir dari while loop")

print('selesai')

# carl
# world
# stop looping
# selesai

# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan len() kunjungi folder_name: "Fungsi-Bawaan/fungsi_len.py"
