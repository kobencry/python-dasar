'''Module penjumlahan'''
def tambah(x, y):
    print('ini adalah fungsi tambah dari modul penjumlahan')
    print(f'nilai __name__ pada modul penjumlahan.py -> {__name__}')
    return x + y

if __name__=="__main__":
    print(tambah(2, 3)) # 5
