'''Module penjumlahan'''
def tambah(x,y):
    return x + y

def menambahkan(*args):
    hasil = 0
    for i in args:
        hasil += i
    return hasil
