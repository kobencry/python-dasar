# Berikut ini adalah contoh implementasi rekursif pada penambahan item ke dalam sebuah list:
def add_items(item, item_baru):
    if len(item) == 0: # base case
        return [item_baru]
    
    else:
        # pemanggilan fungsi rekursif

        # list terurut secara terbalik
        # return add_items(item[1:], item_baru) + [item[0]]
        
        # list terurut 
        return sorted(add_items(item[1:], item_baru) + [item[0]])



listku = [1, 2, 3, 4]
x = 5

print(add_items(listku, x))
# Output:
# [1, 2, 3, 4, 5]

nama = ['carl', 'alice']
y = "eliot"
print(add_items(nama, y))
# Output:
# ['alice', 'carl', 'eliot']