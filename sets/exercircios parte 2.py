a = open('Candidato A.txt', 'r').read().splitlines()
b = open('Candidato B.txt', 'r').read().splitlines()

total_votes = a + b
print(f'Total votes: {len(total_votes)}')
print(f'votes in A {len(a)}')
print(f'votes in B: {len(b)}')

print(f"Votaram nos dois candidatos: {len(set(a).intersection(set(b)))}")

votop = 108 - len(set(a).intersection(set(b)))
print(f'{votop} pessoas votaram e {100 - votop} pessoas não votaram')


print(f'Candidato A {len(set(a))}')
print(f'Candidato B {len(set(b))}')

if len(set(a)) > len(set(b)):
    print('Candidato A venceu')
elif len(set(a)) < len(set(b)):
    print('Candidato B venceu')
else:
    print('então tu é burrao')





