lista1 = list(range(4, 11))
lista2 = [3, 5, 7, 9]

set1 = set(lista1)
set2 = set(lista2)

print(set1)
print(set2)

if len(lista2) == len(set2):
    print('não tem duplicadas')
else:
    print('duplicadas')

print(f'Set 2 = {set2}')
print(f'Set 1 = {set1}')

set3 = {4, 5, 6, 7, 9}
print(type(set3))

print(f'Union {set2.union(set1)}')
print(f'Interseção {set2.intersection(set1)}')
print(f' Difference {set2.difference(set1)}')
print(f' Difference {set1.difference(set2)}')
print(f' Symmetric Difference {set2.symmetric_difference(set1)}')

if 9 in set2:
    print('encontrei')
else:
    print('não tem hahaha')

set2.add(25)
set1.add(14)
print(set2)
print(set1)


tupla1 = (3, 5, 13, 290)
lista3 = [260, 220, 240]
set2.update(tupla1)

print(set2)
set2.update(lista3)
print(set2)

set2.add(200)
print(set2)
set2.remove(200)
print(set2)

set2.discard(210)
print(set2)

set2.pop()
print(set2)

set3 = set(range(1, 10))

print(set3)

# set2.clear()
# set2 = {}
print(set2)

for i in set2:
    print(i)