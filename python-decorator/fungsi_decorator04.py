# Dalam fungsi decorator, Anda dapat menggunakan keyword "print" dan "return" secara bersamaan 
# dengan memahami cara kerja decorator dan mengelola nilai kembali yang dihasilkan. 

# Berikut ini adalah contoh penggunaan print dan return secara bersamaan di dalam fungsi decorator:

# contoh 1
def func_luar(func_lain):
    def func_dalam(*args, **kwargs):
        result = func_lain(*args, **kwargs)
        return result
    return func_dalam

@func_luar
def main(x, y):
    print(x)
    return y

main(5, 50)
# Ouput:
# 5

print(main(100, 200))
# Output:
# 100
# 200

# contoh 2
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Sebelum eksekusi fungsi")
        result = func(*args, **kwargs)
        print("Setelah eksekusi fungsi")
        return result
    return wrapper

@decorator
def tambah(a, b):
    print("Sedang menjumlahkan...")
    return a + b

output = tambah(2, 3)
print("Hasil:", output)