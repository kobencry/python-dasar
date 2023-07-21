# Berikut adalah contoh mencari nilai terbesar dan terkecil menggunakan rekursif
def num_max(arr):
    nilai_terbesar = arr[0]
    #print(f"{len(arr)} > 1: {len(arr) > 1}")
    if len(arr) > 1:
        row = num_max(arr[1:])
        #print(row)
        #print(f"{row} > {nilai_terbesar}: {row > nilai_terbesar}")

        if row > nilai_terbesar:
            nilai_terbesar = row
    #print(f"{arr} -> {nilai_terbesar}")
    
    return nilai_terbesar

angka = [0, 20, 100, -10, 3]

print(num_max(angka))
# Output:
# 100

angka = [20]
print(num_max(angka))
# Output:
# 20