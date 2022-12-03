# unpacking/membongkar Function

# Kita juga bisa menggunakan fitur packing/mengemas dan unpacking/membongkar 
# Python saat mendefinisikan dan memanggil fungsi. 
# Ini adalah kasus penggunaan pengepakan dan pembongkaran yang cukup berguna dan populer dengan Python.
# Di bagian ini, kita akan membahas dasar-dasar cara menggunakan packing dan unpacking dalam fungsi Python 
# baik dalam definisi fungsi atau dalam pemanggilan fungsi.

# Mendefinisikan Fungsi Dengan * dan **
# menggunakan operator * dan ** di fungsi Python.
# Ini akan memungkinkan kita memanggil fungsi dengan sejumlah variabel 
# argumen posisi (*) atau dengan sejumlah variabel argumen kata kunci, atau keduanya.
def fungsi(x, *args, **kwargs):
    print(x)
    print(args)
    print(kwargs)
fungsi('hello', ('world', 20, False), {'nama':'alice'}, email='alice@gmail.com')
# hello
# (('world', 20, False), {'nama': 'alice'})
# {'email': 'alice@gmail.com'}

fungsi(*['hello', 'world'], **{'nama':'alice'})
# hello
# ('world',)
# {'nama': 'alice'}
