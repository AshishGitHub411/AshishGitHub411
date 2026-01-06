lst = ['Apple', 'Guava', 'Mango', 'Banna', 'Kiwi']
 
print("Length of list:",len(lst))
print("First element:",lst(0))
print("Last element:",lst(-1))

lst.append('Papaya')
print("Updated List:",(lst))

lst.remove('Guava')
print("Updated List:",(lst))

lst.sort()
print("Updated List:",(lst))

lst.reverse()
print("Reversed List:",(lst))

print("Multiplication on list :",lst*2)

lst = lst[:4]
print("Sliced list:", lst)

lst.clear()
print("Updated List :", lst)