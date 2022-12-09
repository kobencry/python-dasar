# statemen continue
# menggunakan pernyataan continue kita dapat menghentikan iterasi loop saat ini, 
# dan melanjutkan dengan iterasi berikutnya.

i = 0
while i < 5:
    # i = i + 1
    # kode ini setara dengan diatas
    i += 1
    if i == 3:
        print('lanjutkan looping')
        continue 
    print(i)
# 1
# 2
# lanjutkan looping
# 4
# 5

# menggunakan fungsi bawaan python input()
while True:
    user_input = input('tekan ([y]es/[n]ext): ')
    
    if user_input in ('y', 'n', 'yes', 'next'):
        print('lanjutkan looping')
        continue

    # tambahkan kode statement break untuk berhenti dari looping
    elif user_input in ('q', 'e', 'quit', 'exit'):
        print('stop looping')
        break
    
    else:
        print(user_input)

# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan input() kunjungi folder_name: "Fungsi-Bawaan/fungsi_input.py"
