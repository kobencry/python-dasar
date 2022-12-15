# menggunakan default argument
def func1(nama, usia, kondisi=False):
    if kondisi == True:
        print(f"nama: {nama} usia: {usia}")
    else:
        print("failed")
# memanggil fungsi
func1('alice', 23, True)
# nama: alice usia: 23

#===============================================================================

# menggunakan *args dan **kwargs argument
def func2(*data1, **data2):
    # jika tipe data1 adalah tuple
    if type(data1) == tuple:
        for x in data1:
            print(x)
    # jika kondisi atas tidak terpenuhi jalankan statemen else
    else:
        for y in data2:
            print(y)
# memanggil fungsi
func2('hello', 'world', nama='alice', usia=23)
# hello
# world

func2(nama='eliot', usia=23)

#===============================================================================

# menggunakan annotations/anotasi argumen
def func3(nama:str, usia:int, ipk:float) -> str:
    return f"nama:{nama} usia:{usia} ipk:{ipk}"
# penjelasan dari argumen anotasi diatas
# * nama tipe string
# * usia tipe integer
# * ipk tipe float
# * kembalikan dengan tipe string
print(func3.__annotations__)
# {'nama': <class 'str'>, 'usia': <class 'int'>, 'ipk': <class 'float'>, 'return': <class 'str'>}

print(func3('alice', 23, 2.5))
# nama:alice usia:23 ipk:2.5

# kita bisa memasukan semua argumen tipe string
print(func3('carl', '22', '3.5'))
# nama:carl usia:22 ipk:3.5

print(func3('hello', 2.5, 10))
# nama:hello usia:2.5 ipk:10

#===============================================================================

# menggunakan positional-only dan keyword-only argument
def func4(text, /, border="*", *, lebar=50):
    return f" {text} ".center(lebar, border)

print(func4('hello world'))
