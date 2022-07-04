
r = int(input('digite seu numero: '))
g = int(input('digite seu numero: '))
b = int(input('digite seu numero: '))
if 0 > r > 255:
    print('errado')

elif 0 > g > 255:
    print('errado')

elif 0 > b > 255:
    print('errado')

print(f'#{r:02x}{g:02x}{b:02x}')





