# Fungsi Rekursif untuk Menghitung Bilangan Berpangkat
def pangkat(x, y):
    if y == 0:
        return 1
    else:
        return (x * pangkat(x, y - 1))
    
print(pangkat(5, 2))
# Output:
# 25