# Menghitung Bilangan Faktorial Dengan Fungsi Rekursif di Python
def faktorial(n):
    # print(n)
    if n == 1:
        return 1

    else:
        return n * faktorial(n - 1)

print(faktorial(5))
# Output:
# 120