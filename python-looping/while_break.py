# statement break
# menggunakan pernyataan break kita dapat menghentikan perulangan meskipun kondisi while bernilai True.

while True:
    print("stop looping")
    break
# stop looping

i = 0
while i < 5:
    print(i)
    if i == 3:
        print("stop looping")
        break
    # i = i + 1
    # kode ini setara dengan diatas
    i += 1
# 0
# 1
# 2
# 3
# stop looping

# menggunakan fungsi bawaan python input()
while True:
    user_input = input("tekan ([q]uit/[e]xit): ")
    
    if user_input in ('q', 'e', 'Q', 'E', 'quit', 'exit'):
        print("stop looping")
        break
    
    else:
        print(user_input)

# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan input() kunjungi folder_name: "Fungsi-Bawaan/fungsi_input.py"
