# Menghitung deret aritmatika atau jumlah dari bilangan berturut-turut
# dengan fungsi rekursif
def aritmatika(n):
    if n == 1:
        return n
    else:
        return (n + aritmatika(n - 1))

print(aritmatika(5))
# Output:
# 15