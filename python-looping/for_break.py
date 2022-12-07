# statement break
# menggunakan pernyataan break kita dapat menghentikan perulangan sebelum perulangan melewati semua item atau element.

for i in range(5):
    print("stop looping")
    break

# menggunakan tipe data list
for i in ['alice', 'carl', 'eliot', 'geral']:
    # print(i)
    if i == 'eliot':
        print(i, "ditemukan")
        print("stop looping")
        break
    else:
        print(i)

# menggunakan fungsi bawaan python range()
for i in range(1, 10):
    # print(i)
    if i == 3:
        print("stop looping")
        break
    print(i)

# 1
# 2
# stop looping

# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan range() kunjungi folder_name: "Fungsi-Bawaan/fungsi_range.py"
