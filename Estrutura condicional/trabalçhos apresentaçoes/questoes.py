# import requests
#
# #
# # QUESTAO 1
# r = requests.get('https://api-s-38ea2-default-rtdb.firebaseio.com/Escolas.json')
# print(r.json())
# for i in r.json():
#     if i.upper()[0] == ('S'):
#         print(i, r.json()[i], sep=' - ')
# #
# #
# # # QUESTAO 2
# r = requests.get('https://api-s-38ea2-default-rtdb.firebaseio.com/Escolas.json')
# print(r.json())
# for i in r.json():
#     if len(i) >= 8 and len(i) < 14:
#         print(f'{i} Grande - {r.json()[i]}')
#     elif len(i) >= 14:
#       print(f'{i} Muito Grande - {r.json()[i]}')
#     elif len(i) < 8:
#       print(f'{i} Pequeno - {r.json()[i]}')

















# QUESTAO 3

# info = '{"henrique": "flamengo"}'
# troca = requests.post(f'https://times-5e780-default-rtdb.firebaseio.com/times/.json', data=info)
# print(troca)











# # QUESTAO 4
# cores = requests.get('https://cores-d86c6-default-rtdb.firebaseio.com/Cores.json')
#
# cor1 = int(input('01-Azul\n02-Amarelo\n04-Vermelho\n Digite aqui: '))
# cor2 = int(input('01-Azul\n02-Amarelo\n04-Vermelho\n Digite aqui: '))
#
# if cor1 == cor2:
#     cor = cor1
# else:
#     cor = cor1+cor2
#
# print(cores.json()[cor])


#
# CEP = requests.get('https://cep.awesomeapi.com.br/json/05424020')
#
# req = CEP.jason()
#
# for i in CEP.json():
#     print(i[req])


import pyautogui
from time import sleep

# while True:
#     print(pyautogui.position())
#     sleep(2)
#     break

# pyautogui.moveTo(100, 100)


# pyautogui.moveRel(100, 100)

# pyautogui.click()
# pyautogui.doubleclick()
# pyautogui.tripleclick()
# pyautogui.leftclick()
# pyautogui.rightclick()


# pyautogui.hotkey('win', 'r')
# pyautogui.keyDown('win')
# pyautogui.keyDown('r')
# pyautogui.keyUp('win')
# pyautogui.keyUp('r')

# pyautogui.press('win')
# pyautogui.write('calculadora', interval= 0.5)
# pyautogui.press('enter')

# with pyautogui.hold('win'):
#     pyautogui.press(['left', 'left', 'left'], interval= 0.25)


# pyautogui.hotkey('alt', 'tab')
# sleep(3)
# pyautogui.dragRel(220, 220, duration=2)

# with pyautogui.hold('alt'):
#     pyautogui.press('tab', presses=2, interval=1)

# pyautogui.alert(text='furei tua mae', title='Henrique comedor de casadas', button='OK')
# a = pyautogui.prompt(text='furei tua mae', title='Henrique comedor de casadas',default='', mask='*')
# a = pyautogui.password(text='furei tua mae', title='Henrique comedor de casadas',default='', mask='*')
# print(a)
# pyautogui.confirm(text='Henrique', title='Alerta', buttons=('OK', 'Cancel'))


# sleep(1.5)
# x = pyautogui.locateOnScreen('Capturar1.PNG')
# pyautogui.click(x)


# A1:
# pyautogui.hotkey('win')
# pyautogui.write('Bloco de notas', interval=0.2)
# pyautogui.press('Enter')
# sleep(2)
# pyautogui.write('henrique', interval= 0.2)




# A2
# C = input('digite uma conta: ')
# pyautogui.press('win')
# pyautogui.write('calculadora', interval= 0.1)
# pyautogui.press('enter')
#
# sleep(2)
# pyautogui.write(C)
# pyautogui.press('=')


# A3
# while True:
#     cont = -1
#

# pyautogui.moveTo(30, 400)
# pyautogui.click()
# sleep(1)
# pyautogui.write('Bom dia', interval= 0.1)
# pyautogui.press('enter')
# #



# PILOW
from PIL import Image, ImageDraw, ImageFont

# im = Image.open('gabigol.png')
# print(im.size)
# im = im.convert('1')
# im.show()
#
#
# im = Image.new('RGB', (150,150), (0,0,0))
# im.save('imagem.png')

# x, y = im.size
# for i in range(x):
#     for j in range(y):
#         if i < x //2:
#             im.putpixel((i,j), (255, 255, 255))
#
# im2 = ImageDraw.Draw(im)
# im2.ellipse((x//2-50, y//2-50, x//2+50, y//2+50), fill=(0, 0, 255))
# im.show()



# GETPIXEL = MOSTRA AS CORES QUE TEM NA IMAGEM
# PUTPIXEL = TROCA COR DA IMAGEM
# ELLIPSE = CIRCUOLO
# OUTLINE = COR DO CONTORNO
# SHOW = MOSTRA A IMAGEM
# GABRIEL = FAZ SEXO
# SIZE = TAMANHO DA IMAGEM
# RESIZE = REFAZ O TAMANHO DA IMAGEM
# THUMBNAIL = COMPRIME A IMAGEM
# ROTATE = ROTACIONA A IMAGEM
# OPEN = ABRE A IMAGEM
# PASTE = COLA UMA IMAGEM NA OUTRA
# SAVE = SALVA A IMAGEM NO DIRETORIO EXECUTADO
# FILL = DA A COR
# truetype = fonte da letra
# CONVERT = CONVERTE PRA ALGUM TIPO DE COR
#
# image = Image.open(r'joinha.png')
# draw = ImageDraw.Draw(image)
# font = ImageFont.truetype(r'C:\Windows\Fonts\ALGER', 50)
# texto = 'Brasil'
# draw.text((10, 10), texto, font=font, fill=(255, 0, 100))
# image.show()

#

# im = Image.new("RGB", (300,200), (255,255,255))
#
# im.save(r'henrique.png')
# draw = ImageDraw.Draw(im)
# font = ImageFont.truetype(r'C:\Windows\Fonts\ALGER', 50)
# texto = 'HENRIQUE'
# draw.text((10, 10), texto, font=font, fill=(255, 0, 100))
# im.show()
#
#
#
# im.show()

im = Image.new("RGB", (50,50), (255,0,0))
im2 = Image.save('joinha.png')
joinha = Image.open('joinha.png')
joinha = joinha.resize((150, 150))
tamanho_x, tamanho_y, = joinha.size


im.show()






