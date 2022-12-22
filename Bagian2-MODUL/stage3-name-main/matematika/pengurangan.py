'''Module pengurangan'''
def kurang(x, y):
    print('ini adalah fungsi kurang dari modul pengurangan')
    print(f'nilai __name__ pada modul pengurangan.py -> {__name__}')
    return x - y
print(kurang(100,5)) # 95
